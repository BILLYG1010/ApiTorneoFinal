from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class TorneoBase(BaseModel):
    nombre: str
    descripcion: str
    fecha_inicio: datetime
    fecha_fin: datetime
    inscripcion_inicio: datetime
    inscripcion_fin: datetime
    estado_id: Optional[int]
    reglamento_id: Optional[int]
    participantes_por_equipo: int
    tiene_limite_equipos: bool
    max_equipos: int
    puntos_ganado: int
    puntos_empatado: int
    puntos_perdido: int
    puntos_no_presentado: int
    limite_tarjetas_amarillas: int
    limite_tarjetas_rojas: int
    fase_grupos: bool
    numero_grupos: int
    portada: str

class TorneoCreate(TorneoBase):
    pass

class TorneoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    inscripcion_inicio: Optional[datetime] = None
    inscripcion_fin: Optional[datetime] = None
    estado_id: Optional[int] = None
    reglamento_id: Optional[int] = None
    participantes_por_equipo: Optional[int] = None
    tiene_limite_equipos: Optional[bool] = None
    max_equipos: Optional[int] = None
    puntos_ganado: Optional[int] = None
    puntos_empatado: Optional[int] = None
    puntos_perdido: Optional[int] = None
    puntos_no_presentado: Optional[int] = None
    limite_tarjetas_amarillas: Optional[int] = None
    limite_tarjetas_rojas: Optional[int] = None
    fase_grupos: Optional[bool] = None
    numero_grupos: Optional[int] = None
    portada: Optional[str] = None

class Torneo(TorneoBase):
    torneo_id: int
    created_at: datetime

    class Config:
        orm_mode = True
