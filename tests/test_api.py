from fastapi.testclient import TestClient
from App.main import app

client = TestClient(app)

def test_predict_endpoint():

emp_caract = {
  "genre": "M",
  "statut_marital": "Marié(e)",
  "departement": "Commercial",
  "poste": "Cadre Commercial",
  "domaine_etude": "Infra & Cloud",
  "frequence_deplacement": "Occasionnel",
  "heure_supplementaires": "false",
  "evolution_cat_evol": "hausse",
  "categorie_employe": "employe-experimente",
  "satisfaction_employee_nature_travail": 3,
  "nombre_participation_pee": 0,
  "ecart_note_evaluation": 1,
  "revenu_mensuel": 10609,
  "distance_domicile_travail": 1,
  "satisfaction_globale": 2.00,
  "niveau_education": 2,
  "note_evaluation_actuelle": 3,
  "satisfaction_employee_equipe": 3,
  "age": 37,
  "revenu_par_annee_experience_interne": 9093,
  "satisfaction_employee_equilibre_pro_perso": 1,
  "nombre_experiences_precedentes": 5,
  "annees_dans_l_entreprise": 14,
  "nb_formations_suivies": 2,
  "revenu_par_annee_experience_totale": 7488,
  "ratio_sans_promotion": 0,
  "satisfaction_employee_environnement": 1,
  "exp_hors_entreprise": 3,
  "mobilite_promotion": -10,
  "annees_depuis_la_derniere_promotion": 11}

response = client.post("/predict", json = emp_caract)

assert response.status_code == 200
assert "prediction" in response.json()
assert "probabilite_depart" in response.json()