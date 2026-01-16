from App.database import Base, SQLALCHEMY_AVAILABLE

if SQLALCHEMY_AVAILABLE: 
    from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey 
    from sqlalchemy.sql import func

    class Input(Base):
        __tablename__ = "inputs"

        id = Column(Integer, primary_key=True, index=True)
        genre = Column(String)
        statut_marital = Column(String)
        departement = Column(String)
        poste = Column(String)
        domaine_etude = Column(String)
        frequence_deplacement = Column(String)
        heure_supplementaires = Column(Boolean)
        evolution_cat_evol = Column(String)
        categorie_employe = Column(String)
        satisfaction_employee_nature_travail = Column(Integer)
        nombre_participation_pee = Column(Integer)
        ecart_note_evaluation = Column(Integer)
        revenu_mensuel = Column(Integer)
        distance_domicile_travail = Column(Integer)
        satisfaction_globale = Column(Float)
        niveau_education = Column(Integer)
        note_evaluation_actuelle = Column(Integer)
        satisfaction_employee_equipe = Column(Integer)
        age = Column(Integer)
        revenu_par_annee_experience_interne = Column(Integer)
        satisfaction_employee_equilibre_pro_perso = Column(Integer)
        nombre_experiences_precedentes = Column(Integer)
        annees_dans_l_entreprise = Column(Integer)
        nb_formations_suivies = Column(Integer)
        revenu_par_annee_experience_totale = Column(Integer)
        ratio_sans_promotion = Column(Integer)
        satisfaction_employee_environnement = Column(Integer)
        exp_hors_entreprise = Column(Integer)
        mobilite_promotion = Column(Integer)
        annees_depuis_la_derniere_promotion = Column(Integer)

        created_at = Column(DateTime(timezone=True), server_default=func.now())

    class Predictions(Base):
        __tablename__ = "predictions"
        id = Column(Integer, primary_key=True, index=True)
        input_id = Column(Integer, ForeignKey("inputs.id"))

        prediction_label = Column(String)
        prediction_proba = Column(Float)
        model_version = Column(String)

        created_at = Column(DateTime(timezone=True), server_default=func.now())
else: 
    Input = None 
    Predictions = None