from sqlalchemy import Column, Integer, String, Text, Boolean
from app.database import Base

class Reglamento(Base):
    __tablename__ = "reglamento"

    reglamento_id = Column(Integer, primary_key=True, index=True)
    nombre        = Column(String(100), nullable=False)
    descripcion   = Column(Text, nullable=False)
    activo        = Column(Boolean, nullable=False, default=True)
