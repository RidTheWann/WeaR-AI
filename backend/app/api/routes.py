"""
WeaR Ai - API Routes
REST API endpoints for the chat interface.
"""

import json
from typing import AsyncIterator
from uuid import UUID

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.core.agent import run_agent, get_agent
from app.core.llm import get_model_router
from app.models.schemas import (
    ChatRequest,
    ChatResponse,
    HealthResponse,
    ErrorResponse,
    Message,
    MessageRole,
    StreamEvent,
)
from app import __version__


router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        version=__version__,
    )


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Send a message to WeaR Ai and get a response.
    
    This endpoint supports both streaming and non-streaming modes.
    For streaming, set `stream: true` in the request.
    """
    if request.stream:
        return StreamingResponse(
            _stream_response(request),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )
    
    # Non-streaming response
    try:
        result = await run_agent(
            message=request.message,
            conversation_id=str(request.conversation_id) if request.conversation_id else None,
        )
        
        return ChatResponse(
            conversation_id=UUID(result["conversation_id"]),
            message=Message(
                role=MessageRole.ASSISTANT,
                content=result["answer"],
            ),
            tool_calls=[],
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def _stream_response(request: ChatRequest) -> AsyncIterator[str]:
    """Stream response using Server-Sent Events."""
    try:
        # Send thinking indicator
        yield _format_sse(StreamEvent(event="thinking", data="Processing your request..."))
        
        # Run the agent
        result = await run_agent(
            message=request.message,
            conversation_id=str(request.conversation_id) if request.conversation_id else None,
        )
        
        # Stream the answer in chunks (simulated for now)
        answer = result["answer"]
        chunk_size = 10  # Characters per chunk
        
        for i in range(0, len(answer), chunk_size):
            chunk = answer[i:i + chunk_size]
            yield _format_sse(StreamEvent(event="token", data=chunk))
        
        # Send completion event
        yield _format_sse(StreamEvent(
            event="done",
            data={
                "conversation_id": result["conversation_id"],
                "iterations": result["iterations"],
            },
        ))
        
    except Exception as e:
        yield _format_sse(StreamEvent(event="error", data=str(e)))


def _format_sse(event: StreamEvent) -> str:
    """Format a StreamEvent as an SSE message."""
    data = event.data if isinstance(event.data, str) else json.dumps(event.data)
    return f"event: {event.event}\ndata: {data}\n\n"


@router.post("/chat/simple")
async def chat_simple(request: ChatRequest):
    """
    Simplified chat endpoint that doesn't use the full agent.
    Good for quick responses without tool use.
    """
    router = get_model_router()
    
    messages = [
        {"role": "system", "content": "You are WeaR Ai, a helpful AI assistant."},
        {"role": "user", "content": request.message},
    ]
    
    try:
        response = await router.generate(messages)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/models")
async def list_models():
    """List available models and current configuration."""
    from app.config import get_settings
    settings = get_settings()
    
    return {
        "current_provider": settings.llm_provider,
        "current_model": getattr(settings, f"{settings.llm_provider}_model", "unknown"),
        "available_providers": ["ollama", "groq", "together", "openai", "vllm"],
    }
