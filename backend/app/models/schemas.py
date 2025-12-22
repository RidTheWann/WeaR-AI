"""
WeaR Ai - Pydantic Schemas
Request/Response models for the API.
"""

from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, field_serializer


class MessageRole(str, Enum):
    """Message role in conversation."""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL = "tool"


class ToolCall(BaseModel):
    """Represents a tool call made by the agent."""
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    arguments: dict[str, Any] = Field(default_factory=dict)
    result: str | None = None


class Message(BaseModel):
    """A single message in a conversation."""
    id: UUID = Field(default_factory=uuid4)
    role: MessageRole
    content: str
    tool_calls: list[ToolCall] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    @field_serializer('id')
    def serialize_id(self, value: UUID) -> str:
        return str(value)
    
    @field_serializer('created_at')
    def serialize_created_at(self, value: datetime) -> str:
        return value.isoformat()


class Conversation(BaseModel):
    """A conversation session."""
    id: UUID = Field(default_factory=uuid4)
    title: str | None = None
    messages: list[Message] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# ===========================================
# API Request/Response Models
# ===========================================

class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    message: str = Field(..., min_length=1, max_length=32000)
    conversation_id: UUID | None = None
    stream: bool = True
    use_tools: bool = True
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "Explain quantum computing in simple terms",
                    "stream": True,
                    "use_tools": True,
                }
            ]
        }
    }


class ChatResponse(BaseModel):
    """Response model for chat endpoint (non-streaming)."""
    conversation_id: UUID
    message: Message
    tool_calls: list[ToolCall] = Field(default_factory=list)


class StreamEvent(BaseModel):
    """Server-Sent Event for streaming responses."""
    event: str  # "token", "tool_start", "tool_end", "thinking", "done", "error"
    data: str | dict[str, Any]


class AgentThought(BaseModel):
    """Represents agent's internal reasoning step."""
    step: int
    thought: str
    action: str | None = None
    action_input: dict[str, Any] | None = None
    observation: str | None = None


class HealthResponse(BaseModel):
    """Health check response."""
    status: str = "healthy"
    version: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ErrorResponse(BaseModel):
    """Error response model."""
    error: str
    detail: str | None = None
    code: str | None = None
