from App.database import engine
from App.database import Base

Base.metadata.create_all(bind=engine)

print("Tables créées avec succès")
