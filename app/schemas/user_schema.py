from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

class UsuarioCreate(BaseModel):
    usuario: str
    contrasenia: str
    nombre: str
    apellido: str
    email: EmailStr
    fecha_nacimiento: date
    rol_id: Optional[int] = None  # opcional si puede ser null

class UsuarioLogin(BaseModel):
    usuario: str
    contrasenia: str

class UsuarioResponse(BaseModel):
    usuario_id: int
    usuario: str
    email: EmailStr
    nombre: str
    apellido: str
    fecha_nacimiento: date
    fecha_creacion: date
    ultimo_inicio_sesion: datetime
    estado: bool
    rol_id: Optional[int]

    model_config = {
        "from_attributes": True
    }
