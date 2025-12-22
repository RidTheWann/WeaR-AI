"""Basic health check tests for WeaR Ai backend."""

import pytest
from fastapi.testclient import TestClient


def test_app_imports():
    """Test that the main app module can be imported."""
    from app.main import app
    assert app is not None


def test_root_endpoint():
    """Test the root endpoint returns app info."""
    from app.main import app
    
    client = TestClient(app)
    response = client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "WeaR Ai"
    assert data["status"] == "running"
    assert "version" in data

