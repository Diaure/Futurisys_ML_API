from App.predict import predict_employee
from tests.sample_payload import valid_payload

def test_model_end_to_end():
    result = predict_employee(valid_payload)

    assert "Prediction" in result
    assert "Probabilite_depart" in result
    assert 0 <= result["Probabilite_depart"] <= 1
