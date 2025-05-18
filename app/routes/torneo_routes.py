from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.torneo_schema import Torneo, TorneoCreate, TorneoUpdate
from app.crud.torneo_crud import (
    get_torneos, get_torneo, create_torneo,
    update_torneo, delete_torneo
)
from app.database import SessionLocal

router = APIRouter(prefix="/torneos", tags=["Torneos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Torneo])
def read_torneos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_torneos(db, skip=skip, limit=limit)

@router.get("/{torneo_id}", response_model=Torneo)
def read_torneo(torneo_id: int, db: Session = Depends(get_db)):
    db_torneo = get_torneo(db, torneo_id)
    if not db_torneo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Torneo no encontrado")
    return db_torneo

@router.post("/", response_model=Torneo, status_code=status.HTTP_201_CREATED)
def create_new_torneo(torneo: TorneoCreate, db: Session = Depends(get_db)):
    return create_torneo(db, torneo)

@router.put("/{torneo_id}", response_model=Torneo)
def update_existing_torneo(
    torneo_id: int,
    torneo: TorneoUpdate,
    db: Session = Depends(get_db)
):
    updated = update_torneo(db, torneo_id, torneo)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Torneo no encontrado")
    return updated

@router.delete("/{torneo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_torneo(torneo_id: int, db: Session = Depends(get_db)):
    success = delete_torneo(db, torneo_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Torneo no encontrado")
    return
