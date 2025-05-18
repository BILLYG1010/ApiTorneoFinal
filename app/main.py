from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importamos get_db si lo usan los routers
from app.database import Base, engine, get_db  
from app.config import settings

# Importamos TODOS los modelos para que create_all los registre
from app.models import (
    user_model,
    rol_model,
    torneo_model,
    estado_model,
    reglamento_model,
)

# Creamos las tablas
Base.metadata.create_all(bind=engine)

# Instanciamos FastAPI
app = FastAPI(title="API Torneos")

# Endpoint mínimo para diagnóstico
@app.get("/ping", tags=["Health"])
def ping():
    return {"msg": "pong"}

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montamos las rutas (después del ping)
from app.routes import auth_routes, torneo_routes, estado_routes, reglamento_routes

app.include_router(auth_routes.router)
app.include_router(torneo_routes.router)
app.include_router(estado_routes.router)
app.include_router(reglamento_routes.router)
