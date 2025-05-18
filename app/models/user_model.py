# models/usuario.py
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Usuario(Base):
    __tablename__ = "usuario"

    usuario_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario = Column(String(50), nullable=False, unique=True)
    contrasenia = Column(String(200), nullable=False)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    fecha_creacion = Column(Date, nullable=False)
    ultimo_inicio_sesion = Column(DateTime, nullable=False)
    estado = Column(Boolean, nullable=False)
    rol_id = Column(Integer, ForeignKey("rol.rol_id"))

    rol = relationship("Rol", back_populates="usuarios")
