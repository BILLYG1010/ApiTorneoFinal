from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.reglamento_schema import Reglamento, ReglamentoCreate
from app.crud.reglamento_crud import get_reglamentos, get_reglamento, create_reglamento
from app.database import get_db

router = APIRouter(prefix="/reglamentos", tags=["Reglamentos"])

@router.get("/", response_model=List[Reglamento])
def read_reglamentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_reglamentos(db, skip, limit)

@router.get("/{reglamento_id}", response_model=Reglamento)
def read_reglamento(reglamento_id: int, db: Session = Depends(get_db)):
    r = get_reglamento(db, reglamento_id)
    if not r:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reglamento no encontrado")
    return r

@router.post("/", response_model=Reglamento, status_code=status.HTTP_201_CREATED)
def create_new_reglamento(reglamento: ReglamentoCreate, db: Session = Depends(get_db)):
    return create_reglamento(db, reglamento)
