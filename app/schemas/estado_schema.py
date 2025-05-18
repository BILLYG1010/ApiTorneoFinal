from pydantic import BaseModel

class EstadoBase(BaseModel):
    nombre: str
    descripcion: str

class EstadoCreate(EstadoBase):
    pass

class Estado(EstadoBase):
    estado_id: int

    class Config:
        orm_mode = True
