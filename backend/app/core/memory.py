"""
WeaR Ai - RAG Memory System
Vector-based memory for long-term context retrieval.
"""

import hashlib
from datetime import datetime, timezone
from typing import Any

import httpx
from pydantic import BaseModel

from app.config import get_settings


class MemoryEntry(BaseModel):
    """A single memory entry."""
    id: str
    content: str
    metadata: dict[str, Any] = {}
    embedding: list[float] | None = None
    created_at: datetime = datetime.now(timezone.utc)


class VectorMemory:
    """Vector database memory using Qdrant."""
    
    COLLECTION_NAME = "wear_ai_memory"
    
    def __init__(self, url: str | None = None, api_key: str | None = None):
        settings = get_settings()
        self.url = (url or settings.qdrant_url).rstrip("/")
        self.api_key = api_key or settings.qdrant_api_key
        self.client = httpx.AsyncClient(
            base_url=self.url,
            headers={"api-key": self.api_key} if self.api_key else {},
            timeout=30.0,
        )
        self._embedding_model = None
    
    async def initialize(self) -> None:
        """Initialize the vector collection if it doesn't exist."""
        try:
            # Check if collection exists
            response = await self.client.get(f"/collections/{self.COLLECTION_NAME}")
            if response.status_code == 404:
                await self._create_collection()
        except httpx.HTTPError:
            await self._create_collection()
    
    async def _create_collection(self) -> None:
        """Create the vector collection."""
        await self.client.put(
            f"/collections/{self.COLLECTION_NAME}",
            json={
                "vectors": {
                    "size": 384,  # Default for all-MiniLM-L6-v2
                    "distance": "Cosine",
                },
            },
        )
    
    def _get_embedding_model(self):
        """Lazy load the embedding model."""
        if self._embedding_model is None:
            from sentence_transformers import SentenceTransformer
            settings = get_settings()
            self._embedding_model = SentenceTransformer(settings.embedding_model)
        return self._embedding_model
    
    def _generate_id(self, content: str) -> str:
        """Generate a unique ID for content."""
        return hashlib.md5(content.encode()).hexdigest()
    
    async def embed(self, text: str) -> list[float]:
        """Generate embedding for text."""
        model = self._get_embedding_model()
        embedding = model.encode(text, convert_to_numpy=True)
        return embedding.tolist()
    
    async def store(
        self,
        content: str,
        metadata: dict[str, Any] | None = None,
        conversation_id: str | None = None,
    ) -> str:
        """Store a memory entry."""
        entry_id = self._generate_id(content + str(datetime.now(timezone.utc).timestamp()))
        embedding = await self.embed(content)
        
        payload = {
            "content": content,
            "created_at": datetime.now(timezone.utc).isoformat(),
            **(metadata or {}),
        }
        if conversation_id:
            payload["conversation_id"] = conversation_id
        
        await self.client.put(
            f"/collections/{self.COLLECTION_NAME}/points",
            json={
                "points": [
                    {
                        "id": entry_id,
                        "vector": embedding,
                        "payload": payload,
                    }
                ],
            },
        )
        
        return entry_id
    
    async def search(
        self,
        query: str,
        limit: int = 5,
        conversation_id: str | None = None,
        score_threshold: float = 0.5,
    ) -> list[dict]:
        """Search for relevant memories."""
        query_embedding = await self.embed(query)
        
        filter_conditions = None
        if conversation_id:
            filter_conditions = {
                "must": [
                    {"key": "conversation_id", "match": {"value": conversation_id}}
                ]
            }
        
        response = await self.client.post(
            f"/collections/{self.COLLECTION_NAME}/points/search",
            json={
                "vector": query_embedding,
                "limit": limit,
                "with_payload": True,
                "score_threshold": score_threshold,
                **({"filter": filter_conditions} if filter_conditions else {}),
            },
        )
        
        if response.status_code != 200:
            return []
        
        results = response.json().get("result", [])
        return [
            {
                "id": r["id"],
                "score": r["score"],
                "content": r["payload"].get("content", ""),
                "metadata": {k: v for k, v in r["payload"].items() if k != "content"},
            }
            for r in results
        ]
    
    async def get_context(
        self,
        query: str,
        conversation_id: str | None = None,
        max_tokens: int = 2000,
    ) -> str:
        """Get relevant context for a query."""
        memories = await self.search(query, limit=10, conversation_id=conversation_id)
        
        if not memories:
            return ""
        
        # Build context string
        context_parts = ["**Relevant Context from Memory:**\n"]
        current_length = 0
        
        for memory in memories:
            content = memory["content"]
            if current_length + len(content) > max_tokens * 4:  # Rough char estimate
                break
            context_parts.append(f"- {content}")
            current_length += len(content)
        
        return "\n".join(context_parts)


# Global memory instance
_memory: VectorMemory | None = None


async def get_memory() -> VectorMemory:
    """Get the global memory instance."""
    global _memory
    if _memory is None:
        _memory = VectorMemory()
        await _memory.initialize()
    return _memory
