from fastapi import APIRouter, Depends, Request, HTTPException
from app.core.security import decode_token
from app.crud.user_crud import get_user_by_username
from app.database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

