from pydantic import BaseModel

class ReglamentoBase(BaseModel):
    nombre: str
    descripcion: str
    activo: bool

class ReglamentoCreate(ReglamentoBase):
    pass

class Reglamento(ReglamentoBase):
    reglamento_id: int

    class Config:
        orm_mode = True
