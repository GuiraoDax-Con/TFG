from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Monsters
from ..schemas import MonsterCreate, MonsterResponse

# Crear subrouters
router = APIRouter()

## Rutas para "monsters"
@router.get("/monsters", response_model=list[MonsterResponse])
def get_monsters(db: Session = Depends(get_db)):
    return db.query(Monsters).all()

# Ruta para obtener un monstruo por su ID
@router.get("/monsters/{monster_id}", response_model=MonsterResponse)
def get_monster(monster_id: int, db: Session = Depends(get_db)):
    monster = db.query(Monsters).filter(Monsters.id == monster_id).first()
    if not monster:
        raise HTTPException(status_code=404, detail="Monstruo no encontrado")
    return monster

# Ruta para obtener un monstruo por su nombre
@router.get("/monsters/{monster_name}", response_model=MonsterResponse)
def get_monster_by_name(monster_name: str, db: Session = Depends(get_db)):
    monster = db.query(Monsters).filter(Monsters.name == monster_name).first()
    if not monster:
        raise HTTPException(status_code=404, detail="Monstruo no encontrado")
    return monster

@router.post("/monsters", response_model=MonsterResponse)
def create_monster(monster: MonsterCreate, db: Session = Depends(get_db)):
    db_monster = Monsters(**monster.dict())  # Convertir el modelo de Pydantic a un diccionario
    db.add(db_monster)
    db.commit()
    db.refresh(db_monster)
    return db_monster

@router.delete("/monsters/{monster_id}")
def delete_monster(monster_id: int, db: Session = Depends(get_db)):
    monster = db.query(Monsters).filter(Monsters.id == monster_id).first()
    if not monster:
        raise HTTPException(status_code=404, detail="Monstruo no encontrado")
    db.delete(monster)
    db.commit()
    return {"detail": "Monstruo eliminado"}