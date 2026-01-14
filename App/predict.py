import joblib
import pandas as pd
from App.schemas import EmployeeFeatures
import json
from pathlib import Path
from huggingface_hub import hf_hub_download

MODEL_REPO = "Diaure/xgb_model"

# Variables chargées
model = None
classes_mapping = None
Features = list(EmployeeFeatures.model_fields.keys())



# Chargement des fichiers: fonction pour charger le modèle, le mapping afin de permettre à l'API de démarrer m^me si les éléments ne sont pas présents
def files_load():
    global model, classes_mapping

    if model is None:
        chemin_model = Path(hf_hub_download(repo_id=MODEL_REPO, filename="modele_final_xgb.joblib"))
        # if not chemin_model.exists():
        #     raise RuntimeError("Eléments du modèle introuvable.")
        model =joblib.load(chemin_model)

    if classes_mapping is None:
        chemin_mapping = Path(hf_hub_download(repo_id=MODEL_REPO, filename="mapping_classes.json"))
        # if not chemin_mapping.exists():
        #     raise RuntimeError("Mapping des classes introuvable.")
        with open(chemin_mapping) as f:
            classes_mapping = json.load(f)

# Fonction prédiction
def predict_employee(data: dict):
    files_load()

    df = pd.DataFrame([data])[Features]

    print("Colonnes API :", df.columns.tolist()) 
    print("Nombre colonnes API :", len(df.columns))
    
    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]

    return {
        "Prediction": classes_mapping[str(pred)],
        "Probabilite_depart": float(proba)
    }
