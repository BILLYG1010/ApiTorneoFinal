# app/schemas/etiqueta_schema.py
from pydantic import BaseModel

class EtiquetaBase(BaseModel):
    nombre: str

class EtiquetaRelacion(EtiquetaBase):
    torneo_id: int

class TorneosPorEtiqueta(BaseModel):
    torneos: list[int]  # opcional: si quieres devolver sólo IDs 
    # o bien usa List[Torneo] si devuelves objetos completos

    class Config:
        orm_mode = True
