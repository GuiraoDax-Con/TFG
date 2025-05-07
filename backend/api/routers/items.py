from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Items
from ..schemas import ItemCreate, ItemResponse

# Crear subrouters
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

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Items(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item