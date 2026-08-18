from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_create_checksum() -> None:
    response = client.post("/checksum", json={"text": "hello"})

    assert response.status_code == 200
    assert response.json() == {
        "checksum": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    }


def test_create_checksum_rejects_invalid_unicode() -> None:
    response = client.post(
        "/checksum",
        content=b'{"text":"\\ud800"}',
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_unicode"
