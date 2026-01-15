from App.database import engine, Base

if engine is None: 
    print("DB désactivée : aucune table créée.") 
else: 
    Base.metadata.create_all(bind=engine) 
    print("Tables créées avec succès")
