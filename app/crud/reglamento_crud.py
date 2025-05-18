from sqlalchemy.orm import Session
from typing import List
from app.models.reglamento_model import Reglamento
from app.schemas.reglamento_schema import ReglamentoCreate

def get_reglamentos(db: Session, skip: int = 0, limit: int = 100) -> List[Reglamento]:
    return db.query(Reglamento).offset(skip).limit(limit).all()

def get_reglamento(db: Session, reglamento_id: int) -> Reglamento | None:
    return db.query(Reglamento).filter(Reglamento.reglamento_id == reglamento_id).first()

def create_reglamento(db: Session, regl_in: ReglamentoCreate) -> Reglamento:
    db_regl = Reglamento(**regl_in.dict())
    db.add(db_regl)
    db.commit()
    db.refresh(db_regl)
    return db_regl
