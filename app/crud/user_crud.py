from sqlalchemy.orm import Session
from app.models.user_model import Usuario
from app.core.security import hash_password
import datetime

from app.schemas.user_schema import UsuarioCreate

def get_user_by_username(db: Session, username: str):
    return db.query(Usuario).filter(Usuario.usuario == username).first()

def create_user(db: Session, user: UsuarioCreate):
    db_user = Usuario(
        usuario=user.usuario,
        contrasenia=hash_password(user.contrasenia),
        nombre=user.nombre,
        apellido=user.apellido,
        email=user.email,
        fecha_nacimiento=user.fecha_nacimiento,
        fecha_creacion=datetime.date.today(),
        ultimo_inicio_sesion=datetime.datetime.utcnow(),
        estado=True,
        rol_id=user.rol_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
