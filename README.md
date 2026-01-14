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

## CI/CD et Déploiement

Ce projet met en œuvre une approche CI/CD complète, séparant:
- l’intégration continue (**CI**): garantir la qualité du code
- le déploiement continu (**CD**): rendre l’API accessible publiquement

### `Intégration Continue (CI) – GitHub Actions`

L’intégration continue est assurée via GitHub Actions.

À chaque **push** sur les branches de travail et à chaque **pull request** vers **`develop`**,
le pipeline exécute automatiquement les étapes suivantes :
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

Le déploiement repose sur un Dockerfile, qui définit :
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
- Documentation interactive (Swagger UI) :
https://diaure-futurisys-ml-api.hf.space/docs. Ele permet de:
  - visualiser les endpoints
  - tester directement l’endpoint `/predict`
  - voir les schémas d’entrée et de sortie.

### `Endpoint principal`
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

### `Documentation des endpoints`

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
- **CI/CD** : GitHub Actions, Hugging Face
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
│   ├── test_api.py  # Test automatisé API Pytest
|
├── .gitignore       # Nettoyage du dépôt
├── Dockerfile       # Reproduction du dépôt
├── poetry.lock      # Nettoyage du dépôt
├── pyproject.toml   # Librairies dépendances ML
├── README.md        # Présentation du projet
└── requirements.txt # Librairies dépendances API
```
