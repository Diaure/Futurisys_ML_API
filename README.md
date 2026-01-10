--- 
title: Futurisys 
ML API emoji: 🚀 
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
learning en production en appliquant les bonnes pratiques d’ingénierie logicielle :
versionnage, tests, base de données et automatisation.



## Objectifs du projet
- Déployer un modèle de machine learning via une API REST
- Rendre le modèle accessible de manière fiable et documentée
- Mettre en place une architecture maintenable et évolutive
- Appliquer un workflow Git professionnel
- Préparer une base solide pour un déploiement en production


## Périmètre fonctionnel
Le projet inclut :
- Une API développée avec **FastAPI**
- L’exposition d’un modèle de machine learning via des endpoints REST
- Une base de données **PostgreSQL** pour stocker les entrées/sorties du modèle
- Des tests unitaires et fonctionnels avec **Pytest**
- Un pipeline **CI/CD** pour automatiser les tests et le déploiement
- Une documentation technique claire

## CI/CD et qualité du code

Ce projet utilise une pipeline d’intégration continue (CI) via GitHub Actions.

À chaque push sur les branches de travail et à chaque pull request vers `develop`,
le pipeline exécute automatiquement les étapes suivantes :
- installation d’un environnement Python 3.11 isolé
- installation des dépendances définies dans le projet
- exécution des tests unitaires via pytest

L’objectif est de garantir que :
- le projet reste installable
- les transformations et composants (chargement du modèle, prédiction) ne régressent pas
- toute fusion vers la branche `develop` est validée automatiquement

## Architecture de l’API

L’API est développée avec **FastAPI** et repose sur :
- un schéma d’entrée validé avec **Pydantic**
- un préprocesseur entraîné et sauvegardé
- un modèle de machine learning sérialisé avec **joblib**

Les artefacts du modèle sont stockés dans le dossier `App/model/` :
- `preprocesseur_fitted.joblib`
- `model_final_xgb.joblib`
- `mapping_classes.json`

## Lancer l’API en local

Depuis la racine du projet :

```bash
uvicorn App.main:app --reload --log-level debug
```
L’API est alors accessible à l’adresse  http://127.0.0.1:8000/

La documentation interactive à http://127.0.0.1:8000/docs

### Endpoint principal
`POST /predict`

Cet endpoint reçoit les caractéristiques d’un employé et retourne :

- une prédiction lisible ("Reste" ou "Part")
- la probabilité associée au départ

Exemple de réponse :
```json
{
  "Prediction": "Part",
  "Probabilite_depart": 0.795678996
}
```
Les données d’entrée sont validées automatiquement avant l’appel au modèle,
garantissant la cohérence avec les variables utilisées lors de l’entraînement.

## Documentation des endpoints

L’API expose un endpoint principal de prédiction.

**POST /predict**
  - Description : retourne une prédiction de départ d’un employé
  - Validation des données : Pydantic
  - Réponses possibles :
    - 200 : prédiction valide
    - 422 : données invalides

## Stack technique
- **Langage** : Python
- **API** : FastAPI
- **Machine Learning** : scikit-learn
- **Base de données** : PostgreSQL
- **Tests** : Pytest, pytest-cov
- **CI/CD** : GitHub Actions
- **Versionnage** : Git / GitHub



## Structure du projet
```text
futurisys_ml-api/
├── github/workflows
│   ├── ci.yml       # Description des évènement déclenchants des tests
├── app/             # Code applicatif principal
│   ├── main.py      # Point d’entrée de l’API
│   ├── predict.py   # Application du modèle
│   ├── schemas.py   # Validation des données (Pydantic)
│   ── model/                            # Elements du modèle
│   ├── mapping_classes.json             # Correspondances des classes
│   ├── modele_final_xgb.joblib          # Modèle final avec hyperparamètres
│   ├── preprocesseur_fitted.joblib      # Pipeline entrainé
|
├── scripts/         # Scripts bd (BD, données)
├── tests/           # Tests unitaires, fonctionnels
│   ├── test_api.py      # Test automatisé de l'API via Pytest
|
├── .gitignore       # Nettoyage du dépôt
├── pyproject.toml   # Librairies des modules entrainement ML
├── README.md        # Présentation du projet
└── requirements.txt # Librairies des modules dispensables API
```
