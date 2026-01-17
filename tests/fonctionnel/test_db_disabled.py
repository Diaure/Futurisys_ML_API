import os
from App.predict import predict_employee
from tests.sample_payload import valid_payload

def test_db_disabled(monkeypatch):
    # Simule l'environnement Hugging Face
    monkeypatch.setenv("SPACE_ID", "ci")

    result = predict_employee(valid_payload)

    assert "Prediction" in result
    assert "Probabilite_depart" in result
