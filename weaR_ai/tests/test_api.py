"""
Pytest API tests for weaR AI backend
"""
from fastapi.testclient import TestClient
from api.api import app

client = TestClient(app)

def test_health():
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_chat_completions():
    response = client.post("/v1/chat/completions", json={"messages": []})
    assert response.status_code == 200
    assert "choices" in response.json()
