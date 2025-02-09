from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_valid_integer():
    response = client.get("/api/classify-number?number=371")
    assert response.status_code == 200
    assert response.json()["number"] == 371
    assert "armstrong" in response.json()["properties"]

def test_negative_number():
    response = client.get("/api/classify-number?number=-5")
    assert response.status_code == 200
    assert response.json()["number"] == -5
    assert response.json()["is_prime"] == is_prime(5)  # Check absolute value

def test_floating_point_number():
    response = client.get("/api/classify-number?number=3.14")
    assert response.status_code == 200
    assert response.json()["number"] == 3.14
    assert response.json()["is_prime"] is None  # Non-integer, so no prime check

def test_invalid_input():
    response = client.get("/api/classify-number?number=abc")
    assert response.status_code == 400
