from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import Items, Monsters
from .schemas import ItemCreate, ItemResponse, MonsterCreate, MonsterResponse

router = APIRouter()

## Rutas para "items"
@router.get("/items", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return db.query(Items).all()

# Ruta para obtener un item por su ID
@router.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Items).filter(Items.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item

# Ruta para obtener un item por su nombre
@router.get("/items/{item_Name}", response_model=ItemResponse)
def get_item_by_name(item_Name: str, db: Session = Depends(get_db)):
    item = db.query(Items).filter(Items.Name == item_Name).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item

@router.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Items(**item.dict())  # Convertir el modelo de Pydantic a un diccionario
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Items).filter(Items.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    db.delete(item)
    db.commit()
    return {"detail": "Item eliminado"}



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