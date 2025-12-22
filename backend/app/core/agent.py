"""
WeaR Ai - LangGraph ReAct Agent
Core agent implementation using the ReAct (Reasoning + Acting) pattern.
"""

import json
import re
from typing import Annotated, Any, TypedDict
from uuid import uuid4

from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)

from app.config import get_settings
from app.core.llm import get_model_router
from app.core.memory import get_memory
from app.core.prompts import SYSTEM_PROMPT, REACT_PROMPT, SELF_CORRECTION_PROMPT
from app.tools.base import get_tool_registry, ToolOutput
from app.tools.web_search import WebSearchTool
from app.tools.code_executor import CodeExecutorTool


# ===========================================
# Agent State Definition
# ===========================================

class AgentState(TypedDict):
    """State maintained throughout agent execution."""
    messages: Annotated[list, add_messages]
    current_thought: str
    current_action: str
    current_action_input: dict[str, Any]
    observation: str
    iteration: int
    max_iterations: int
    final_answer: str | None
    should_continue: bool
    conversation_id: str
    memory_context: str


# ===========================================
# Agent Node Functions
# ===========================================

async def retrieve_memory(state: AgentState) -> AgentState:
    """Retrieve relevant context from memory."""
    try:
        memory = await get_memory()
        
        # Get the last user message
        last_user_msg = None
        for msg in reversed(state["messages"]):
            if isinstance(msg, HumanMessage):
                last_user_msg = msg.content
                break
        
        if last_user_msg:
            context = await memory.get_context(
                query=last_user_msg,
                conversation_id=state.get("conversation_id"),
            )
            state["memory_context"] = context
    except Exception:
        state["memory_context"] = ""
    
    return state


async def reason(state: AgentState) -> AgentState:
    """ReAct reasoning step - determine what action to take."""
    settings = get_settings()
    router = get_model_router()
    registry = get_tool_registry()
    
    # Build the prompt with tool descriptions
    tools_desc = registry.get_tools_description()
    react_prompt = REACT_PROMPT.format(tools_description=tools_desc)
    
    # Build messages
    messages = [
        {"role": "system", "content": f"{SYSTEM_PROMPT}\n\n{react_prompt}"},
    ]
    
    # Add memory context if available
    if state.get("memory_context"):
        messages.append({
            "role": "system",
            "content": state["memory_context"],
        })
    
    # Add conversation history
    for msg in state["messages"]:
        if isinstance(msg, HumanMessage):
            messages.append({"role": "user", "content": msg.content})
        elif isinstance(msg, AIMessage):
            messages.append({"role": "assistant", "content": msg.content})
        elif isinstance(msg, ToolMessage):
            messages.append({
                "role": "user",
                "content": f"Observation: {msg.content}",
            })
    
    # Add iteration context
    if state["iteration"] > 0:
        messages.append({
            "role": "user",
            "content": f"[Iteration {state['iteration'] + 1}/{state['max_iterations']}] Continue your reasoning:",
        })
    
    # Generate response
    response = await router.generate(messages)
    
    # Parse ReAct response
    thought, action, action_input = _parse_react_response(response)
    
    state["current_thought"] = thought
    state["current_action"] = action
    state["current_action_input"] = action_input
    state["iteration"] += 1
    
    # Check if we have a final answer
    if action.lower() == "final answer" or action.lower() == "final_answer":
        state["final_answer"] = action_input.get("answer", str(action_input))
        state["should_continue"] = False
    else:
        state["should_continue"] = state["iteration"] < state["max_iterations"]
    
    # Add the AI message
    state["messages"].append(AIMessage(content=response))
    
    return state


async def execute_action(state: AgentState) -> AgentState:
    """Execute the selected tool action."""
    if not state["should_continue"]:
        return state
    
    action = state["current_action"]
    action_input = state["current_action_input"]
    
    registry = get_tool_registry()
    tool = registry.get(action)
    
    if tool is None:
        observation = f"Error: Unknown tool '{action}'. Available tools: {', '.join(t.name for t in registry.list_tools())}"
    else:
        try:
            result: ToolOutput = await tool.execute(**action_input)
            observation = result.result
        except Exception as e:
            observation = f"Error executing tool: {str(e)}"
    
    state["observation"] = observation
    state["messages"].append(
        ToolMessage(content=observation, tool_call_id=str(uuid4()))
    )
    
    return state


async def self_correct(state: AgentState) -> AgentState:
    """Optional self-correction step to validate response quality."""
    if state["final_answer"] is None:
        return state
    
    settings = get_settings()
    
    # Only run self-correction if enabled and we have a final answer
    if not settings.debug:  # Skip in production for speed
        return state
    
    router = get_model_router()
    
    # Get original question
    original_question = ""
    for msg in state["messages"]:
        if isinstance(msg, HumanMessage):
            original_question = msg.content
            break
    
    # Build correction prompt
    correction_prompt = SELF_CORRECTION_PROMPT.format(
        response=state["final_answer"],
        question=original_question,
    )
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": correction_prompt},
    ]
    
    try:
        correction = await router.generate(messages)
        
        # Check if correction suggests changes
        if "incorrect" in correction.lower() or "should be" in correction.lower():
            # Update the final answer with corrected version
            state["final_answer"] = f"{state['final_answer']}\n\n---\n*Self-correction applied:* {correction}"
    except Exception:
        pass  # Silently fail self-correction
    
    return state


async def store_memory(state: AgentState) -> AgentState:
    """Store the interaction in memory for future retrieval."""
    try:
        memory = await get_memory()
        
        # Get the question and answer
        question = ""
        for msg in state["messages"]:
            if isinstance(msg, HumanMessage):
                question = msg.content
                break
        
        answer = state.get("final_answer", "")
        
        if question and answer:
            # Store the Q&A pair
            await memory.store(
                content=f"Q: {question}\nA: {answer[:500]}",  # Truncate long answers
                metadata={"type": "qa_pair"},
                conversation_id=state.get("conversation_id"),
            )
    except Exception:
        pass  # Silently fail memory storage
    
    return state


def should_continue(state: AgentState) -> str:
    """Determine if the agent should continue reasoning."""
    if not state["should_continue"]:
        return "end"
    if state["current_action"].lower() in ("final answer", "final_answer"):
        return "end"
    return "execute"


# ===========================================
# Helper Functions
# ===========================================

def _parse_react_response(response: str) -> tuple[str, str, dict]:
    """Parse a ReAct format response into components."""
    thought = ""
    action = ""
    action_input = {}
    
    # Extract thought
    thought_match = re.search(r"Thought:\s*(.+?)(?=Action:|$)", response, re.DOTALL)
    if thought_match:
        thought = thought_match.group(1).strip()
    
    # Extract action
    action_match = re.search(r"Action:\s*(.+?)(?=Action Input:|$)", response, re.DOTALL)
    if action_match:
        action = action_match.group(1).strip()
    
    # Extract action input
    input_match = re.search(r"Action Input:\s*(.+?)$", response, re.DOTALL)
    if input_match:
        input_str = input_match.group(1).strip()
        
        # Try to parse as JSON
        try:
            # Handle JSON in code blocks
            if "```" in input_str:
                json_match = re.search(r"```(?:json)?\s*(.+?)\s*```", input_str, re.DOTALL)
                if json_match:
                    input_str = json_match.group(1)
            
            action_input = json.loads(input_str)
        except json.JSONDecodeError:
            # If not JSON, treat as plain text answer
            action_input = {"answer": input_str}
    
    return thought, action, action_input


# ===========================================
# Agent Graph Builder
# ===========================================

def create_agent_graph() -> StateGraph:
    """Create the LangGraph agent workflow."""
    # Initialize tools
    registry = get_tool_registry()
    registry.register(WebSearchTool())
    registry.register(CodeExecutorTool())
    
    # Build the graph
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("retrieve_memory", retrieve_memory)
    workflow.add_node("reason", reason)
    workflow.add_node("execute", execute_action)
    workflow.add_node("self_correct", self_correct)
    workflow.add_node("store_memory", store_memory)
    
    # Define edges
    workflow.set_entry_point("retrieve_memory")
    workflow.add_edge("retrieve_memory", "reason")
    
    # Conditional edge after reasoning
    workflow.add_conditional_edges(
        "reason",
        should_continue,
        {
            "execute": "execute",
            "end": "self_correct",
        },
    )
    
    # After execution, go back to reasoning
    workflow.add_edge("execute", "reason")
    
    # After self-correction, store memory and end
    workflow.add_edge("self_correct", "store_memory")
    workflow.add_edge("store_memory", END)
    
    return workflow.compile()


# Global agent instance
_agent = None


def get_agent():
    """Get the compiled agent graph."""
    global _agent
    if _agent is None:
        _agent = create_agent_graph()
    return _agent


async def run_agent(
    message: str,
    conversation_id: str | None = None,
    conversation_history: list | None = None,
) -> dict:
    """Run the agent with a user message."""
    settings = get_settings()
    agent = get_agent()
    
    # Build initial state
    messages = conversation_history or []
    messages.append(HumanMessage(content=message))
    
    initial_state: AgentState = {
        "messages": messages,
        "current_thought": "",
        "current_action": "",
        "current_action_input": {},
        "observation": "",
        "iteration": 0,
        "max_iterations": settings.max_iterations,
        "final_answer": None,
        "should_continue": True,
        "conversation_id": conversation_id or str(uuid4()),
        "memory_context": "",
    }
    
    # Run the agent
    final_state = await agent.ainvoke(initial_state)
    
    return {
        "answer": final_state.get("final_answer", "I couldn't generate a response."),
        "thoughts": [
            final_state.get("current_thought", ""),
        ],
        "conversation_id": final_state.get("conversation_id"),
        "iterations": final_state.get("iteration", 0),
    }
