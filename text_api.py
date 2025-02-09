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
    assert response.status_code == 200  # Negative numbers are valid
    assert response.json()["number"] == -5

def test_floating_point_number():
    response = client.get("/api/classify-number?number=3.14")
    assert response.status_code == 400  # Floating-point numbers are invalid

def test_invalid_input():
    response = client.get("/api/classify-number?number=abc")
    assert response.status_code == 400  # Non-numeric input is invalid
