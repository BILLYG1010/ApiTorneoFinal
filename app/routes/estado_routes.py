from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.estado_schema import Estado, EstadoCreate
from app.crud.estado_crud import get_estados, get_estado, create_estado
from app.database import get_db

router = APIRouter(prefix="/estados", tags=["Estados"])

@router.get("/", response_model=List[Estado])
def read_estados(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_estados(db, skip, limit)

@router.get("/{estado_id}", response_model=Estado)
def read_estado(estado_id: int, db: Session = Depends(get_db)):
    e = get_estado(db, estado_id)
    if not e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado no encontrado")
    return e

@router.post("/", response_model=Estado, status_code=status.HTTP_201_CREATED)
def create_new_estado(estado: EstadoCreate, db: Session = Depends(get_db)):
    return create_estado(db, estado)
