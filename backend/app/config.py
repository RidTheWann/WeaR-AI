"""
WeaR Ai - Configuration Management
Pydantic Settings for type-safe environment configuration.
"""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    
    # ===========================================
    # LLM Provider Configuration
    # ===========================================
    llm_provider: Literal["ollama", "vllm", "groq", "together", "openai"] = "ollama"
    
    # Ollama
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.1:70b"
    
    # vLLM
    vllm_base_url: str = "http://localhost:8000"
    vllm_model: str = "meta-llama/Llama-3.1-70B-Instruct"
    
    # Groq
    groq_api_key: str = ""
    groq_model: str = "llama-3.1-70b-versatile"
    
    # Together AI
    together_api_key: str = ""
    together_model: str = "meta-llama/Llama-3.1-405B-Instruct-Turbo"
    
    # OpenAI-compatible
    openai_api_key: str = ""
    openai_base_url: str = "https://api.openai.com/v1"
    
    # ===========================================
    # Tool API Keys
    # ===========================================
    tavily_api_key: str = ""
    serper_api_key: str = ""
    
    # ===========================================
    # Database Configuration
    # ===========================================
    database_url: str = "postgresql+asyncpg://postgres:password@localhost:5432/wear_ai"
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: str = ""
    redis_url: str = "redis://localhost:6379/0"
    
    # ===========================================
    # Application Settings
    # ===========================================
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True
    secret_key: str = Field(default="change-me-in-production")
    cors_origins: list[str] = ["http://localhost:3000"]
    
    # Embedding
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    
    # Agent Settings
    max_iterations: int = 10  # Max ReAct loops
    temperature: float = 0.7
    max_tokens: int = 4096
    
    @property
    def is_production(self) -> bool:
        return not self.debug


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
