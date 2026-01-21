# tests/functional/test_predict_endpoint.py

from fastapi.testclient import TestClient
from App.main import app
from tests.sample_payload import valid_payload

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/predict", json=valid_payload)
    assert response.status_code == 200

    body = response.json()
    assert "Prediction" in body
    assert "Probabilite_depart" in body
    assert isinstance(body["Probabilite_depart"], float)
