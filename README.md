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
├── app/             # Code applicatif principal
│   ├── main.py      # Point d’entrée de l’API
|
├── tests/           # Tests unitaires, fonctionnels
├── scripts/         # Scripts bd (BD, données)
├── requirements.txt # Librairies env.
├── README.md        # Présentation du projet
└── .gitignore       # Nettoyage du dépôt
