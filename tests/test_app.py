"""Automated tests for the Flask app — our CI quality gate.

Run with:  pytest -v
"""
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    """The home page should return HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_has_title(client):
    """The page should contain our heading text."""
    response = client.get("/")
    assert b"Flask app" in response.data


def test_health_endpoint(client):
    """The /health endpoint should report status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_unknown_route_404(client):
    """An unknown route should return 404, not crash."""
    response = client.get("/does-not-exist")
    assert response.status_code == 404
