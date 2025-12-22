"""
WeaR Ai - Tool Base Class
Abstract interface for agent tools.
"""

from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field


class ToolInput(BaseModel):
    """Base class for tool inputs."""
    pass


class ToolOutput(BaseModel):
    """Standard tool output format."""
    success: bool = True
    result: str
    data: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None


class BaseTool(ABC):
    """Abstract base class for all WeaR Ai tools."""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Unique tool name."""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Tool description for the agent."""
        pass
    
    @property
    @abstractmethod
    def parameters_schema(self) -> dict:
        """JSON schema for tool parameters."""
        pass
    
    @abstractmethod
    async def execute(self, **kwargs) -> ToolOutput:
        """Execute the tool with given parameters."""
        pass
    
    def to_openai_function(self) -> dict:
        """Convert to OpenAI function calling format."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters_schema,
            },
        }
    
    def to_react_description(self) -> str:
        """Get description for ReAct prompt."""
        return f"{self.name}: {self.description}"


class ToolRegistry:
    """Registry for managing available tools."""
    
    def __init__(self):
        self._tools: dict[str, BaseTool] = {}
    
    def register(self, tool: BaseTool) -> None:
        """Register a tool."""
        self._tools[tool.name] = tool
    
    def get(self, name: str) -> BaseTool | None:
        """Get a tool by name."""
        return self._tools.get(name)
    
    def list_tools(self) -> list[BaseTool]:
        """List all registered tools."""
        return list(self._tools.values())
    
    def get_tools_description(self) -> str:
        """Get formatted description of all tools for prompts."""
        descriptions = []
        for tool in self._tools.values():
            params = ", ".join(
                f"{k}: {v.get('type', 'any')}"
                for k, v in tool.parameters_schema.get("properties", {}).items()
            )
            descriptions.append(f"- {tool.name}({params}): {tool.description}")
        return "\n".join(descriptions)
    
    def get_openai_functions(self) -> list[dict]:
        """Get all tools in OpenAI function format."""
        return [tool.to_openai_function() for tool in self._tools.values()]


# Global registry
_registry: ToolRegistry | None = None


def get_tool_registry() -> ToolRegistry:
    """Get the global tool registry."""
    global _registry
    if _registry is None:
        _registry = ToolRegistry()
    return _registry
