# Importamos las clases necesarias de SQLAlchemy para definir modelos y relaciones
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from .database import Base

class Items(Base):
    __tablename__ = "items"  # Nombre de la tabla en la base de datos    
    
    id = Column(Integer, primary_key=True, index=True)  # ID del item, clave primaria
    Name = Column(String(100))
    Price = Column(String(30)) 
    AC = Column(String(100))
    Damage = Column(String(50))
    Weight = Column(String(10))
    Type = Column(String(50))
    Properties = Column(String(100))
    img = Column(LONGTEXT, nullable=True)  # Nueva columna para la URL o ruta de la imagen

class Monsters(Base):
    __tablename__ = "monsters"  # Nombre de la tabla en la base de datos
    
    id = Column(Integer, primary_key=True, index=True)  # ID del monstruo, clave primaria
    name = Column(String(100))  # Nombre del monstruo
    size = Column(String(100))  # Tamaño del monstruo
    type = Column(String(100))
    tag = Column(String(100))
    alignment = Column(String(70)) 
    cr= Column(String(70)) # CR (Challenge Rating) del monstruo
    sourceBook = Column(String(200))
    img = Column(LONGTEXT, nullable=True)   # Nueva columna para la URL o ruta de la imagen
