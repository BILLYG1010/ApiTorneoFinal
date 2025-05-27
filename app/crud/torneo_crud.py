from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.torneo_model import Torneo
from app.schemas.torneo_schema import TorneoCreate, TorneoUpdate
from sqlalchemy import text
from app.database import engine


def get_torneos(db: Session, skip: int = 0, limit: int = 100) -> List[Torneo]:
    return db.query(Torneo).offset(skip).limit(limit).all()

def get_torneo(db: Session, torneo_id: int) -> Optional[Torneo]:
    return db.query(Torneo).filter(Torneo.torneo_id == torneo_id).first()

def create_torneo(db: Session, torneo_in: TorneoCreate) -> Torneo:
    db_torneo = Torneo(**torneo_in.dict())
    db.add(db_torneo)
    db.commit()
    db.refresh(db_torneo)
    return db_torneo

def update_torneo(db: Session, torneo_id: int, torneo_in: TorneoUpdate) -> Optional[Torneo]:
    db_torneo = get_torneo(db, torneo_id)
    if not db_torneo:
        return None
    for field, value in torneo_in.dict(exclude_unset=True).items():
        setattr(db_torneo, field, value)
    db.commit()
    db.refresh(db_torneo)
    return db_torneo

def delete_torneo(db: Session, torneo_id: int) -> bool:
    db_torneo = get_torneo(db, torneo_id)
    if not db_torneo:
        return False
    db.delete(db_torneo)
    db.commit()
    return True





def relacionar_etiqueta_torneo(
    db: Session,
    nombre_etiqueta: str,
    torneo_id: int
) -> None:
    """
    Llama a sp_relacionar_etiqueta_torneo(nombre, torneo_id)
    """
    sql = text("CALL sp_relacionar_etiqueta_torneo(:nombre, :torneo_id)")
    db.execute(sql, {"nombre": nombre_etiqueta, "torneo_id": torneo_id})
    db.commit()



def get_torneos_por_etiqueta_sp(nombre_etiqueta: str) -> List[Torneo]:
    """
    Ejecuta el SP usando raw_connection para evitar
    problemas de cursores pendientes, y mapea
    cada fila a una instancia de Torneo.
    """
    conn = engine.raw_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        # Llama al SP
        cursor.callproc("sp_get_torneos_por_etiqueta", [nombre_etiqueta])

        # Recupera cada result set (debería haber sólo uno)
        rows = []
        for result in cursor.stored_results():
            rows.extend(result.fetchall())

        # Mapea a objetos ORM sin añadirlos a la sesión
        torneos = [Torneo(**row) for row in rows]
        return torneos

    finally:
        cursor.close()
        conn.close()
