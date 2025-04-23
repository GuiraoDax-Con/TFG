from pydantic import BaseModel
from typing import Optional

# Modelo de Pydantic para Items
class ItemBase(BaseModel):
    Name: str
    Price: str
    AC: Optional[str] = None
    Damage: Optional[str] = None
    Weight: Optional[str] = None
    Type: Optional[str] = None
    Properties: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True  # Esto permite que Pydantic trabaje con objetos de SQLAlchemy

# Modelo de Pydantic para Monsters
class MonsterBase(BaseModel):
    name: str
    size: str
    type: str
    tag:Optional[str] = None
    alignment: Optional[str] = None
    cr: Optional[str] = None
    sourceBook: Optional[str] = None

class MonsterCreate(MonsterBase):
    pass

class MonsterResponse(MonsterBase):
    id: int

    class Config:
        orm_mode = True 