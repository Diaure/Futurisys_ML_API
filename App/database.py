import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
<<<<<<< HEAD
=======

# Tentative d'import SQLAlchemy uniquement si disponible 
try: 
    SQLALCHEMY_AVAILABLE = True 
except ModuleNotFoundError: 
    SQLALCHEMY_AVAILABLE = False
>>>>>>> 730f23d8af257943c5e13570e1fab5a743e559e7

load_dotenv()

# Détection si on est en CI (GitHub Actions) ou en test 
IS_CI = os.getenv("CI") == "true"
IS_PYTEST = "pytest" in os.getenv("PYTHONPATH", "") or os.getenv("PYTEST_CURRENT_TEST") is not None 
<<<<<<< HEAD

SKIP_DB = IS_CI or IS_PYTEST
=======
IS_HF = os.getenv("SPACE_ID") is not None # Hugging Face 

SKIP_DB = IS_CI or IS_PYTEST or IS_HF or not SQLALCHEMY_AVAILABLE
>>>>>>> 730f23d8af257943c5e13570e1fab5a743e559e7

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "test_db")

DATABASE_URL = (f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"f"@{DB_HOST}:{DB_PORT}/{DB_NAME}")

<<<<<<< HEAD
Base = declarative_base()
=======
Base = declarative_base() if SQLALCHEMY_AVAILABLE else None
>>>>>>> 730f23d8af257943c5e13570e1fab5a743e559e7

if not SKIP_DB:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

else: 
    engine = None 
    SessionLocal = None