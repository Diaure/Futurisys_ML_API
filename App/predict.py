import joblib
import pandas as pd
from App.schemas import EmployeeFeatures
import json


model = joblib.load("App/model/modele_final_xgb.joblib")

FEATURES = list(EmployeeFeatures.model_fields.keys())
with open("App/model/mapping_classes.json") as f: 
    CLASS_MAPPING = json.load(f)

def predict_employee(data: dict):
    df = pd.DataFrame([data])[FEATURES]

    print("Colonnes API :", df.columns.tolist()) 
    print("Nombre colonnes API :", len(df.columns))
    
    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]

    return {
        "Prediction": CLASS_MAPPING[str(pred)],
        "Probabilite_depart": float(proba)
    }
