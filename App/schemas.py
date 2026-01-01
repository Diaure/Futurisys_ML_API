from pydantic import BaseModel
from typing import Optional

class EmployeeFeatures(BaseModel):
    genre: str
    statut_marital: str
    departement: str
    poste: str
    domaine_etude: str
    frequence_deplacement: str
    heure_supplementaires: bool
    evolution_cat_evol: str
    categorie_employe: str

    satisfaction_employee_nature_travail: int
    nombre_participation_pee: int
    ecart_note_evaluation: int
    revenu_mensuel: int
    distance_domicile_travail: int
    satisfaction_globale: float
    niveau_education: int
    note_evaluation_actuelle: int
    satisfaction_employee_equipe: int
    age: int
    revenu_par_annee_experience_interne: int
    satisfaction_employee_equilibre_pro_perso: int
    nombre_experiences_precedentes: int
    annees_dans_l_entreprise: int
    nb_formations_suivies: int
    revenu_par_annee_experience_totale: int
    ratio_sans_promotion: int
    satisfaction_employee_environnement: int
    exp_hors_entreprise: int
    mobilite_promotion: int
    annees_depuis_la_derniere_promotion: int
