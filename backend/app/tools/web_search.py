"""
WeaR Ai - Web Search Tool
Search the web using Tavily or Serper API.
"""

import httpx
from typing import Any

from app.tools.base import BaseTool, ToolOutput
from app.config import get_settings


class WebSearchTool(BaseTool):
    """Search the web for current information."""
    
    @property
    def name(self) -> str:
        return "web_search"
    
    @property
    def description(self) -> str:
        return "Search the web for current information. Use this when you need up-to-date information or facts you're not certain about."
    
    @property
    def parameters_schema(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query",
                },
                "max_results": {
                    "type": "integer",
                    "description": "Maximum number of results to return (default: 5)",
                    "default": 5,
                },
            },
            "required": ["query"],
        }
    
    async def execute(self, query: str, max_results: int = 5, **kwargs) -> ToolOutput:
        """Execute web search."""
        settings = get_settings()
        
        try:
            # Try Tavily first
            if settings.tavily_api_key:
                return await self._search_tavily(query, max_results, settings.tavily_api_key)
            # Fall back to Serper
            elif settings.serper_api_key:
                return await self._search_serper(query, max_results, settings.serper_api_key)
            else:
                return ToolOutput(
                    success=False,
                    result="No search API configured. Please set TAVILY_API_KEY or SERPER_API_KEY.",
                    error="missing_api_key",
                )
        except Exception as e:
            return ToolOutput(
                success=False,
                result=f"Search failed: {str(e)}",
                error=str(e),
            )
    
    async def _search_tavily(self, query: str, max_results: int, api_key: str) -> ToolOutput:
        """Search using Tavily API."""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.tavily.com/search",
                json={
                    "api_key": api_key,
                    "query": query,
                    "max_results": max_results,
                    "include_answer": True,
                    "include_raw_content": False,
                },
                timeout=30.0,
            )
            response.raise_for_status()
            data = response.json()
        
        # Format results
        results = []
        if answer := data.get("answer"):
            results.append(f"**Summary:** {answer}\n")
        
        for i, result in enumerate(data.get("results", []), 1):
            title = result.get("title", "No title")
            url = result.get("url", "")
            content = result.get("content", "")[:500]
            results.append(f"{i}. **{title}**\n   URL: {url}\n   {content}\n")
        
        formatted = "\n".join(results) if results else "No results found."
        
        return ToolOutput(
            success=True,
            result=formatted,
            data={"raw_results": data.get("results", [])},
        )
    
    async def _search_serper(self, query: str, max_results: int, api_key: str) -> ToolOutput:
        """Search using Serper API."""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://google.serper.dev/search",
                headers={"X-API-KEY": api_key},
                json={"q": query, "num": max_results},
                timeout=30.0,
            )
            response.raise_for_status()
            data = response.json()
        
        # Format results
        results = []
        
        # Answer box if available
        if answer_box := data.get("answerBox"):
            if snippet := answer_box.get("snippet") or answer_box.get("answer"):
                results.append(f"**Quick Answer:** {snippet}\n")
        
        # Organic results
        for i, result in enumerate(data.get("organic", [])[:max_results], 1):
            title = result.get("title", "No title")
            link = result.get("link", "")
            snippet = result.get("snippet", "")
            results.append(f"{i}. **{title}**\n   URL: {link}\n   {snippet}\n")
        
        formatted = "\n".join(results) if results else "No results found."
        
        return ToolOutput(
            success=True,
            result=formatted,
            data={"raw_results": data.get("organic", [])},
        )
