from fastapi import APIRouter, Depends, HTTPException, Response,Request
from sqlalchemy.orm import Session
from app.core.security import verify_password, create_access_token, decode_token
from app.crud.user_crud import create_user, get_user_by_username
from app.database import SessionLocal
from app.schemas.user_schema import UsuarioCreate, UsuarioLogin, UsuarioResponse

router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UsuarioCreate, db: Session = Depends(get_db)):
    if get_user_by_username(db, user.usuario):
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    return create_user(db, user)

@router.post("/login")
def login(user_data: UsuarioLogin, response: Response, db: Session = Depends(get_db)):
    user = get_user_by_username(db, user_data.usuario)
    if not user or not verify_password(user_data.contrasenia, user.contrasenia):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    token = create_access_token(data={"sub": user.usuario})
    
    # Aquí se envía el token como cookie
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        max_age=3600,  # 1 hora
        samesite="Lax",
        secure=False  # Cambia a True si usas HTTPS
    )
    
    return {"message": "Login correcto"}




@router.get("/me", response_model=UsuarioResponse)
def get_current_user(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="No autenticado")

    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")

    user = get_user_by_username(db, payload.get("sub"))
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user    # devuelve el ORM, FastAPI lo serializa según UsuarioResponse


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"detail": "Sesión cerrada"}