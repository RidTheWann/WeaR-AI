"""
WeaR Ai - LLM Router
Model-agnostic interface supporting multiple LLM providers.
"""

import json
from abc import ABC, abstractmethod
from typing import AsyncIterator

import httpx
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage

from app.config import Settings, get_settings


class LLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    @abstractmethod
    async def generate(
        self,
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ) -> str:
        """Generate a response from the model."""
        pass
    
    @abstractmethod
    async def stream(
        self,
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ) -> AsyncIterator[str]:
        """Stream a response from the model."""
        pass


class OllamaProvider(LLMProvider):
    """Ollama local model provider."""
    
    def __init__(self, base_url: str, model: str):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.client = httpx.AsyncClient(timeout=120.0)
    
    async def generate(
        self,
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ) -> str:
        response = await self.client.post(
            f"{self.base_url}/api/chat",
            json={
                "model": self.model,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": temperature,
                    "num_predict": max_tokens,
                },
            },
        )
        response.raise_for_status()
        return response.json()["message"]["content"]
    
    async def stream(
        self,
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ) -> AsyncIterator[str]:
        async with self.client.stream(
            "POST",
            f"{self.base_url}/api/chat",
            json={
                "model": self.model,
                "messages": messages,
                "stream": True,
                "options": {
                    "temperature": temperature,
                    "num_predict": max_tokens,
                },
            },
        ) as response:
            async for line in response.aiter_lines():
                if line:
                    data = json.loads(line)
                    if content := data.get("message", {}).get("content"):
                        yield content


class GroqProvider(LLMProvider):
    """Groq cloud provider (fast inference)."""
    
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model
        self.client = httpx.AsyncClient(
            base_url="https://api.groq.com/openai/v1",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=60.0,
        )
    
    async def generate(
        self,
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ) -> str:
        response = await self.client.post(
            "/chat/completions",
            json={
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
            },
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    
    async def stream(
        self,
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ) -> AsyncIterator[str]:
        async with self.client.stream(
            "POST",
            "/chat/completions",
            json={
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "stream": True,
            },
        ) as response:
            async for line in response.aiter_lines():
                if line.startswith("data: ") and line != "data: [DONE]":
                    data = json.loads(line[6:])
                    if content := data["choices"][0]["delta"].get("content"):
                        yield content


class TogetherProvider(LLMProvider):
    """Together AI cloud provider."""
    
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model
        self.client = httpx.AsyncClient(
            base_url="https://api.together.xyz/v1",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=120.0,
        )
    
    async def generate(
        self,
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ) -> str:
        response = await self.client.post(
            "/chat/completions",
            json={
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
            },
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    
    async def stream(
        self,
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ) -> AsyncIterator[str]:
        async with self.client.stream(
            "POST",
            "/chat/completions",
            json={
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "stream": True,
            },
        ) as response:
            async for line in response.aiter_lines():
                if line.startswith("data: ") and line != "data: [DONE]":
                    data = json.loads(line[6:])
                    if content := data["choices"][0]["delta"].get("content"):
                        yield content


class ModelRouter:
    """Routes requests to the appropriate LLM provider."""
    
    def __init__(self, settings: Settings | None = None):
        self.settings = settings or get_settings()
        self._provider: LLMProvider | None = None
    
    @property
    def provider(self) -> LLMProvider:
        """Get or create the LLM provider based on settings."""
        if self._provider is None:
            self._provider = self._create_provider()
        return self._provider
    
    def _create_provider(self) -> LLMProvider:
        """Create the appropriate provider based on settings."""
        match self.settings.llm_provider:
            case "ollama":
                return OllamaProvider(
                    base_url=self.settings.ollama_base_url,
                    model=self.settings.ollama_model,
                )
            case "groq":
                return GroqProvider(
                    api_key=self.settings.groq_api_key,
                    model=self.settings.groq_model,
                )
            case "together":
                return TogetherProvider(
                    api_key=self.settings.together_api_key,
                    model=self.settings.together_model,
                )
            case _:
                # Default to Ollama
                return OllamaProvider(
                    base_url=self.settings.ollama_base_url,
                    model=self.settings.ollama_model,
                )
    
    def get_langchain_llm(self) -> ChatOpenAI:
        """Get a LangChain-compatible LLM instance."""
        match self.settings.llm_provider:
            case "ollama":
                return ChatOpenAI(
                    base_url=f"{self.settings.ollama_base_url}/v1",
                    api_key="ollama",  # Ollama doesn't need a key
                    model=self.settings.ollama_model,
                    temperature=self.settings.temperature,
                    max_tokens=self.settings.max_tokens,
                )
            case "groq":
                return ChatOpenAI(
                    base_url="https://api.groq.com/openai/v1",
                    api_key=self.settings.groq_api_key,
                    model=self.settings.groq_model,
                    temperature=self.settings.temperature,
                    max_tokens=self.settings.max_tokens,
                )
            case "together":
                return ChatOpenAI(
                    base_url="https://api.together.xyz/v1",
                    api_key=self.settings.together_api_key,
                    model=self.settings.together_model,
                    temperature=self.settings.temperature,
                    max_tokens=self.settings.max_tokens,
                )
            case _:
                return ChatOpenAI(
                    base_url=self.settings.openai_base_url,
                    api_key=self.settings.openai_api_key,
                    temperature=self.settings.temperature,
                    max_tokens=self.settings.max_tokens,
                )
    
    async def generate(self, messages: list[dict], **kwargs) -> str:
        """Generate a response."""
        return await self.provider.generate(
            messages,
            temperature=kwargs.get("temperature", self.settings.temperature),
            max_tokens=kwargs.get("max_tokens", self.settings.max_tokens),
        )
    
    async def stream(self, messages: list[dict], **kwargs) -> AsyncIterator[str]:
        """Stream a response."""
        async for token in self.provider.stream(
            messages,
            temperature=kwargs.get("temperature", self.settings.temperature),
            max_tokens=kwargs.get("max_tokens", self.settings.max_tokens),
        ):
            yield token


# Global router instance
_router: ModelRouter | None = None


def get_model_router() -> ModelRouter:
    """Get the global model router instance."""
    global _router
    if _router is None:
        _router = ModelRouter()
    return _router
