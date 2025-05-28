from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine, get_db  
from app.config import settings
from app.models import (
    user_model,
    rol_model,
    torneo_model,
    estado_model,
    reglamento_model,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Torneos", debug=True)

origins = [
    "http://localhost:4200",                # Angular local dev
    "http://localhost:3000",                # Otro puerto típico (React)
    "http://127.0.0.1:4200",                # Variante local
    "https://tornesomesoamericana.com",     # Tu dominio real
    "https://www.tornesomesoamericana.com"  # Con www, si aplica
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping", tags=["Health"])
def ping():
    return {"msg": "pong"}

from app.routes import auth_routes, torneo_routes, estado_routes, reglamento_routes

app.include_router(auth_routes.router)
app.include_router(torneo_routes.router)
app.include_router(estado_routes.router)
app.include_router(reglamento_routes.router)
