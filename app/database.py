from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carga .env y pisa variables del sistema si existen
load_dotenv(override=True)

# Lee la URL correcta
url = os.getenv("DATABASE_URL")
print("▶️ DATABASE_URL =", url)

# Crea el engine usando esa URL
engine = create_engine(
    url,
    pool_pre_ping=True,
    echo=True
)

# SessionLocal y Base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Generador de sesiones para tus rutas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
