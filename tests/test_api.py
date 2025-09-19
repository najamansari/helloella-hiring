import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.logic import get_or_create_transform_id

client = TestClient(app)


class TestApi:
    def test_create_payload_success(self):
        response = client.post("/payload", json={
            "list_1": ["first", "third"],
            "list_2": ["second", "fourth"]
        })
        assert response.status_code == 200

        response_json = response.json()
        assert "id" in response_json
        assert response_json["id"] == "dc282d12ccacdd7cdd6e4bdc88268fde8c115829"

    def test_create_payload_failure(self):
        response = client.post("/payload", json={
            "list_1": ["first", "third", "fifth"],
            "list_2": ["second", "fourth"]
        })
        assert response.status_code == 400

        response_json = response.json()
        assert "detail" in response_json
        assert response_json["detail"] == "Lists must be of same length"

def test_get_payload():
    get_response = client.get("/payload/testing-123")
    assert get_response.status_code == 200
    assert get_response.json()["payload"] == [
        "testing", "one", "two", "three"
    ]
