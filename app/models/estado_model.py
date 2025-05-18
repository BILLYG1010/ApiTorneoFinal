from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Estado(Base):
    __tablename__ = "estado"

    estado_id   = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
