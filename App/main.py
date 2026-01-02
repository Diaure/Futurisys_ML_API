from fastapi import FastAPI
from App.schemas import EmployeeFeatures
from App.predict import predict_employee

app = FastAPI(
    title = "Futurisys ML API",
    description = "API de prédiction du départ des employés",
    version="0.1.0"
)

@app.post("/predict")
def predict(data: EmployeeFeatures):
    """
    Prédit la probabilité de départ d'un employé à partir de ses caractéristiques.
    """
    return predict_employee(data.model_dump())
