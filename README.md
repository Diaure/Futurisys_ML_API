---
title: Futurisys ML API
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---


# Futurisys – Déploiement d’un modèle de Machine Learning via API

## Contexte
**Futurisys** est une entreprise innovante souhaitant rendre ses modèles de machine learning
opérationnels et accessibles via une API performante.

Ce projet correspond à un **Proof of Concept (POC)** visant à déployer un modèle de machine
learning en production en appliquant les bonnes pratiques d’ingénierie logicielle: versionnage, tests, base de données et automatisation.


## Objectifs du projet
- Déployer un modèle de machine learning via une API REST
- Rendre le modèle accessible de manière fiable et documentée
- Mettre en place une architecture maintenable et évolutive
- Appliquer un workflow Git professionnel
- Préparer une base solide pour un déploiement en production


## Périmètre fonctionnel
Le projet inclut:
- Une API développée avec **FastAPI**
- L’exposition d’un modèle de machine learning via des endpoints REST
- Une base de données **PostgreSQL** pour stocker les entrées/sorties du modèle
- Des tests unitaires et fonctionnels avec **Pytest**
- Un pipeline **CI/CD** pour automatiser les tests et le déploiement
- Une documentation technique claire

## CI/CD et Déploiement

Ce projet met en œuvre une approche CI/CD complète, séparant:
- l’intégration continue (**CI**): garantir la qualité du code
- le déploiement continu (**CD**): rendre l’API accessible publiquement

### `Intégration Continue (CI) – GitHub Actions`

L’intégration continue est assurée via GitHub Actions.

À chaque **push** sur les branches de travail et à chaque **pull request** vers **`develop`**,
le pipeline exécute automatiquement les étapes suivantes:
- installation d’un environnement Python 3.11 isolé
- installation des dépendances définies dans le projet
- exécution des tests automatisés avec Pytest

L’objectif est de:
- vérifier que le projet est installable
- garantir que l’API démarre correctement
- valider le chargement du modèle et le endpoint /*`predict`*
- éviter toute régression avant fusion vers **`develop`**.

### `Déploiement Continu (CD) – Hugging Face Spaces`

Le déploiement de l’API est réalisé sur Hugging Face Spaces qui permet:

- d’héberger gratuitement des applications ML
- de déployer une API Dockerisée
- d’exposer un service accessible publiquement sans gérer de serveur

Dans ce projet, Hugging Face est utilisé comme plateforme de démonstration et de mise à disposition de l’API.

Le déploiement repose sur un Dockerfile, qui définit:
- l’image Python utilisée (Python 3.11)
- l’installation des dépendances
- le lancement de l’API avec Uvicorn

Il garantit la reproductibilité de l'environnement lors de l'exécution de l'API.

A noter que les ***fichiers binaires*** ne sont pas stochés dans le dépôt GiHub principal pour les raisons suivantes:
- Hugging Face bloque les push Git contenant des fichiers binaires lourds
- Git n’est pas conçu pour versionner des artefacts ML volumineux.

Pour contourner la situation, dans le projet, les artefacts sont stockés dans un Space Hugging Face dédié, séparé du code. Lors du démarrage de lAPI:
- le code télécharge dynamiquement les artefacts via huggingface_hub
- l’API peut démarrer même si les fichiers ne sont pas présents localement


### `Lancer l’API en local`

L’API est déployée publiquement sur Hugging Face Spaces.

- URL de l’API :
https://diaure-futurisys-ml-api.hf.space
- Documentation interactive (Swagger UI):
https://diaure-futurisys-ml-api.hf.space/docs. Ele permet de:
  - visualiser les endpoints
  - tester directement l’endpoint `/predict`
  - voir les schémas d’entrée et de sortie.

### `Endpoint principal`
`POST /predict`

Cet endpoint reçoit les caractéristiques d’un employé et retourne:

- une prédiction lisible ("Reste" ou "Part")
- la probabilité associée au départ

Exemple de réponse:
```json
{
  "Prediction": "Part",
  "Probabilite_depart": 0.795678996
}
```
Les données d’entrée sont validées automatiquement avant l’appel au modèle,
garantissant la cohérence avec les variables utilisées lors de l’entraînement.

### `Documentation des endpoints`

L’API expose un endpoint principal de prédiction.

**POST /predict**
  - Description : retourne une prédiction de départ d’un employé
  - Validation des données: Pydantic
  - Réponses possibles:
    - 200: prédiction valide
    - 422: données invalides

## Base de données et traçabilité des prédictions
### `Objectifs`

L’intégration d’une base de données PostgreSQL permet d’inscrire le projet dans une logique MLOps et de répondre à plusieurs objectifs clés:
- assurer la traçabilité complète des prédictions du modèle
- conserver l’historique des données d’entrée utilisateur
- stocker les résultats de prédiction (label, probabilité, version du modèle)
- préparer une architecture compatible avec un déploiement en production.

### `Méthodologie utilisée`
- **PostgreSQL** a été retenu pour:
  - sa robustesse et sa fiabilité
  - sa compatibilité native avec SQLAlchemy
  - son usage courant en environnement professionnel

- **SQLAlchemy** est utilisé comme couche d’abstraction:
  - gestion centralisée de la connexion à la base
  - cohérence entre le schéma Python et la base SQL

Les identifiants de connexion sont stockés dans des variables d’environnement (`.env`) afin d’éviter toute exposition de secrets dans le dépôt Git.

### `Modélisation de la base de données`
La base de données repose sur trois tables distinctes, chacune ayant un rôle précis.
1. `employees_dataset - Dataset de référence`
Il contient le dataset final nettoyé et préparé lors de l'entraînement du modèle en incluant l'ensemble des **32 deatures** du modèle. Il sert de:
  - référence de schéma
  - source de validation
  - base documentaire du modèle

C'est une table qui n'est jamais alimentée par l'utilisateur.

```python
load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "dataset_final.csv")

df = pd.read_csv(csv_path, encoding="latin-1")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"f"@{DB_HOST}:{DB_PORT}/{DB_NAME}")

engine = create_engine(DATABASE_URL)

df.to_sql("employees_dataset", engine, if_exists="replace", index=False)
```

2. `inputs - Entrées utilisateur`
  - Enregistre chaque requête utilisateur envoyée à l'endpoint `/predict`
  - Contient exactement les features attendues par le modèle
  - Structure strictement alignée avec le schéma Pydandic(`EmployeeFeatures`)
  - Permet:
    - l'audit des predictions
    - l'analyse à posteriori
    - la reproductibilité des résultats.
```python
class Input(Base):
    __tablename__ = "inputs"

    id = Column(Integer, primary_key=True, index=True)
    genre = Column(String)
    statut_marital = Column(String)
    departement = Column(String)
    poste = Column(String)
```

3. `predictions - Résultats du modèle`
  - Continet:
    - le label de prédiction
    - la probabilité associée
  - Reliée à `inputs` via une clé étrangère
  - Garantit une trçabilité complète.
```python
class Predictions(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    input_id = Column(Integer, ForeignKey("inputs.id"))

    prediction_label = Column(String)
    prediction_proba = Column(Float)
    model_version = Column(String)
```

### `Interaction API <> Base de données`
Lors d’un appel à l’endpoint `POST /predict`:
- les données utilisateur sont validées via **Pydantic**
- les entrées sont enregistrées dans la table **inputs**
- le modèle est exécuté
- la prédiction est enregistrée dans la table **predictions**
- la réponse est retournée à l’utilisateur.

## Stack technique
- **Langage**: Python
- **API**: FastAPI
- **Machine Learning**: scikit-learn
- **Base de données**: PostgreSQL
- **Tests**: Pytest, pytest-cov
- **CI/CD**: GitHub Actions
- **Versionnage**: Git / GitHub


## Structure du projet
```text
futurisys_ml-api/
├── github/workflows
│   ├── ci.yml       # Description des évènement déclenchants des tests
├── app/             # Code applicatif principal
│   ├── database.py  # Point de connexion à la base PostgreSQL
│   ├── main.py      # Point d’entrée de l’API
│   ├── model.py     # Définition des tables de la database
│   ├── predict.py   # Application du modèle
│   ├── schemas.py   # Validation des données (Pydantic)
│   ── model/                            # Elements du modèle
│   ├── mapping_classes.json             # Correspondances des classes
│   ├── modele_final_xgb.joblib          # Modèle final avec hyperparamètres
│   ├── preprocesseur_fitted.joblib      # Pipeline entrainé
|
├── scripts/                   # Scripts bd (BD, données)
│   ├── create_tables.py       # Créaton des tables définies dans model.py
│   ├── dataset_final.csv      # Data final
│   ├── insert_dataset.py      # Code chargement de la table dataset_final
├── tests/               # Tests unitaires, fonctionnels
│   ├── test_api.py      # Test automatisé de l'API via Pytest
|
├── .env             # Stockage des variables sensibles et de configuration
├── .gitignore       # Nettoyage du dépôt
├── pyproject.toml   # Librairies des modules entrainement ML
├── README.md        # Présentation du projet
└── requirements.txt # Librairies des modules dispensables API
```
