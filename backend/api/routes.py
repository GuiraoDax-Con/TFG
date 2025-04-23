from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import Items, Monsters

router = APIRouter()

# Rutas para "items"
@router.get("/items")
def get_items(db: Session = Depends(get_db)):
    return db.query(Items).all()

@router.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Items).filter(Items.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item

@router.post("/items")
def create_item(item: Items, db: Session = Depends(get_db)):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Items).filter(Items.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    db.delete(item)
    db.commit()
    return {"detail": "Item eliminado"}

# Rutas para "monsters"
@router.get("/monsters")
def get_monsters(db: Session = Depends(get_db)):
    return db.query(Monsters).all()

@router.get("/monsters/{monster_id}")
def get_monster(monster_id: int, db: Session = Depends(get_db)):
    monster = db.query(Monsters).filter(Monsters.id == monster_id).first()
    if not monster:
        raise HTTPException(status_code=404, detail="Monstruo no encontrado")
    return monster

@router.post("/monsters")
def create_monster(monster: Monsters, db: Session = Depends(get_db)):
    db.add(monster)
    db.commit()
    db.refresh(monster)
    return monster

@router.delete("/monsters/{monster_id}")
def delete_monster(monster_id: int, db: Session = Depends(get_db)):
    monster = db.query(Monsters).filter(Monsters.id == monster_id).first()
    if not monster:
        raise HTTPException(status_code=404, detail="Monstruo no encontrado")
    db.delete(monster)
    db.commit()
    return {"detail": "Monstruo eliminado"}