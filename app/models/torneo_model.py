from sqlalchemy import (
    Column, Integer, String, Text, DateTime, Boolean, ForeignKey, func
)
from app.database import Base

class Torneo(Base):
    __tablename__ = "torneo"

    torneo_id               = Column(Integer, primary_key=True, index=True)
    nombre                  = Column(String(100), nullable=False)
    descripcion             = Column(Text, nullable=False)
    fecha_inicio            = Column(DateTime, nullable=False)
    fecha_fin               = Column(DateTime, nullable=False)
    inscripcion_inicio      = Column(DateTime, nullable=False)
    inscripcion_fin         = Column(DateTime, nullable=False)
    estado_id               = Column(Integer, ForeignKey("estado.estado_id"), nullable=True)
    reglamento_id           = Column(Integer, ForeignKey("reglamento.reglamento_id"), nullable=True)
    participantes_por_equipo= Column(Integer, nullable=False)
    tiene_limite_equipos    = Column(Boolean, nullable=False)
    max_equipos             = Column(Integer, nullable=False)
    puntos_ganado           = Column(Integer, nullable=False)
    puntos_empatado         = Column(Integer, nullable=False)
    puntos_perdido          = Column(Integer, nullable=False)
    puntos_no_presentado    = Column(Integer, nullable=False)
    limite_tarjetas_amarillas = Column(Integer, nullable=False)
    limite_tarjetas_rojas   = Column(Integer, nullable=False)
    fase_grupos             = Column(Boolean, nullable=False)
    numero_grupos           = Column(Integer, nullable=False)
    created_at              = Column(DateTime, server_default=func.now(), nullable=False)
    portada                 = Column(Text, nullable=False)
