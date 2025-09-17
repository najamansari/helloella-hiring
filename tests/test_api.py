import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_payload():
    response = client.post("/payload", json={
        "list_1": ["first", "second"],
        "list_2": ["third", "fourth"]
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_payload():
    get_response = client.get("/payload/testing-123")
    assert get_response.status_code == 200
    assert get_response.json()["payload"] == [
        "testing", "one", "two", "three"
    ]
