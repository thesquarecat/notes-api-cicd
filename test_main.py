import pytest
from fastapi.testclient import TestClient
from main import app, notes

# reset in-memory data between tests so they can't affect each other
@pytest.fixture(autouse=True)
def reset_notes():
    notes.clear()
    yield

client = TestClient(app)

def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "broken", "service": "notes-api"}  # intentional break

def test_create_and_fetch_note():
    created = client.post("/notes", json={"text": "learn CI/CD"})
    assert created.status_code == 201
    note_id = created.json()["id"]

    fetched = client.get(f"/notes/{note_id}")
    assert fetched.status_code == 200
    assert fetched.json()["text"] == "learn CI/CD"

def test_unknown_note_returns_404():
    response = client.get("/notes/999")
    assert response.status_code == 404

def test_list_starts_empty():
    response = client.get("/notes")
    assert response.status_code == 200
    assert response.json() == []
