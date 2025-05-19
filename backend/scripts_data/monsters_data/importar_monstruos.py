import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError

# Conexión a la base de datos
URL_DATABASE = 'mysql+pymysql://dm:1235@localhost:3306/laguarida'

try:
    engine = create_engine(URL_DATABASE)
    connection = engine.connect()
    print("✅ Conexión con la base de datos establecida correctamente.")
except SQLAlchemyError as e:
    print("❌ Error al conectar con la base de datos:")
    print(e)
    exit()

Session = sessionmaker(bind=engine)
session = Session()

# Declarar modelo
Base = declarative_base()

class Monsters(Base):
    __tablename__ = "monsters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    size = Column(String(100))
    type = Column(String(100))
    tag = Column(String(100))
    alignment = Column(String(70))
    cr = Column(String(70))
    sourceBook = Column(String(50))
    img = Column(String(255), nullable=True)


# Eliminar todos los registros de la tabla Monsters
try:
    session.query(Monsters).delete()
    session.commit()
    print("🗑️ Todos los registros de la tabla 'monsters' han sido eliminados.")
except Exception as e:
    print(f"❌ Error al eliminar los datos existentes: {e}")
    session.rollback()


# Diccionarios de traducción
alignment_translation = {
    "Lawful good": "Legal bueno", "Neutral good": "Neutral bueno", "Chaotic good": "Caótico bueno",
    "Lawful neutral": "Legal neutral", "Neutral": "Neutral", "Chaotic neutral": "Caótico neutral",
    "Lawful evil": "Legal maligno", "Neutral evil": "Neutral maligno", "Chaotic evil": "Caótico maligno",
    "Unaligned": "No alineado"
}
type_translation = {
    "Aberration": "Aberración", "Beast": "Bestia", "Celestial": "Celestial", "Construct": "Constructo",
    "Dragon": "Dragón", "Elemental": "Elemental", "Fey": "Feérico", "Fiend": "Demoníaco",
    "Giant": "Gigante", "Humanoid": "Humanoide", "Monstrosity": "Monstruosidad",
    "Ooze": "Moco", "Plant": "Planta", "Undead": "No muerto"
}
tag_translation = {
    "Shapechanger": "Cambiaformas", "Fire Genasi": "Genasi de fuego", "Air Genasi": "Genasi de aire",
    "Water Genasi": "Genasi de agua", "Earth Genasi": "Genasi de tierra"
}
size_translation = {
    "Tiny": "Diminuto", "Small": "Pequeño", "Medium": "Mediano", "Large": "Grande",
    "Huge": "Enorme", "Gargantuan": "Colosal"
}

def traducir(valor, diccionario):
    if pd.isna(valor):
        return None
    valor = str(valor).strip()
    return diccionario.get(valor, valor)

try:
    # Leer Excel
    df = pd.read_excel("Complete_Monster_List_-_public.xlsx")
    print("📥 Archivo Excel cargado correctamente.")

    # Traducir columnas
    df['alignment'] = df['Alignment'].apply(lambda x: traducir(x, alignment_translation))
    df['type'] = df['Type'].apply(lambda x: traducir(x, type_translation))
    df['tag'] = df['Tag'].apply(lambda x: traducir(x, tag_translation))
    df['size'] = df['Size'].apply(lambda x: traducir(x, size_translation))
    df['cr'] = df['CR']
    df['sourceBook'] = df['Source book']
    df['name'] = df['Name']

    # Insertar en la base de datos si no existe ya
    for i, row in df.iterrows():
        nombre = row['name']
        print(f"🔎 Revisando monstruo {i+1}: {nombre}...")

        existente = session.query(Monsters).filter(Monsters.name == nombre).first()
        if existente:
            print(f"⚠️ Monstruo '{nombre}' ya existe. Saltando.")
            continue

        monstruo = Monsters(
            name=nombre,
            size=row['size'],
            type=row['type'],
            tag=row['tag'],
            alignment=row['alignment'],
            cr=row['cr'],
            sourceBook=row['sourceBook'],
            img=None
        )
        session.add(monstruo)
        print(f"✅ Insertado: {nombre}")

        session.commit()
        print("✅ Todos los monstruos del Excel han sido insertados correctamente.")

    # Monstruos personalizados
    monstruos_personalizados = [
        Monsters(id=2441, name='Gran Goblin', size='Pequeño', type='Humanoide', tag='Goblinoide',
                    alignment='Legal Malvado', cr='1/2', sourceBook='Reglas Basicas', img=''),
        Monsters(id=2440, name='Goblin Chaman', size='Pequeño', type='Humanoide', tag='Goblinoide',
                    alignment='Caótico Neutral', cr='4', sourceBook='Los Secretos de DarkKerous', img=''),
        Monsters(id=2442, name='Capitan Goblin', size='Pequeño', type='Humanoide', tag='Goblinoide',
                    alignment='Neutral Malvado', cr='3', sourceBook='Los Secretos de DarkKerous', img=''),
        Monsters(id=2443, name='General Goblin', size='Mediano', type='Humanoide', tag='Goblinoide',
                    alignment='Caótico Malvado', cr='4', sourceBook='Los Secretos de DarkKerous', img='')
    ]

    session.add_all(monstruos_personalizados)
    session.commit()
    print("✅ Monstruos personalizados agregados correctamente.")

except Exception as e:
    print("❌ Ocurrió un error durante el procesamiento:")
    print(e)

finally:
    session.close()
    connection.close()
    print("🔒 Conexión cerrada.")
