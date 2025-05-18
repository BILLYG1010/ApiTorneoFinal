# models/rol.py
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Rol(Base):
    __tablename__ = "rol"

    rol_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    estado = Column(Boolean, nullable=False)

    usuarios = relationship("Usuario", back_populates="rol")
