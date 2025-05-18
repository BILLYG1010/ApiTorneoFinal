from sqlalchemy.orm import Session
from typing import List
from app.models.estado_model import Estado
from app.schemas.estado_schema import EstadoCreate

def get_estados(db: Session, skip: int = 0, limit: int = 100) -> List[Estado]:
    return db.query(Estado).offset(skip).limit(limit).all()

def get_estado(db: Session, estado_id: int) -> Estado | None:
    return db.query(Estado).filter(Estado.estado_id == estado_id).first()

def create_estado(db: Session, estado_in: EstadoCreate) -> Estado:
    db_estado = Estado(**estado_in.dict())
    db.add(db_estado)
    db.commit()
    db.refresh(db_estado)
    return db_estado
