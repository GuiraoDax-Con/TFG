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
    img = Column(String(255), nullable=True)  # Nueva columna para la URL o ruta de la imagen


# Eliminar todos los registros de la tabla Monsters
try:
    session.query(Items).delete()
    session.commit()
    print("🗑️ Todos los registros de la tabla 'monsters' han sido eliminados.")
except Exception as e:
    print(f"❌ Error al eliminar los datos existentes: {e}")
    session.rollback()


# Diccionarios de Items
dnd_items_part_1 = [
    {"Name": "Garrote", "Price": "1 pl", "CA": "", "Damage": "1d4 Contundente", "Peso": "0,9 kg", "Type": "Armas Cuerpo a Cuerpo Simples", "Properties": "Ligera"},
    {"Name": "Daga", "Price": "2 po", "CA": "", "Damage": "1d4 Perforante", "Peso": "0,45 kg", "Type": "Armas Cuerpo a Cuerpo Simples", "Properties": "Ligera, Finura, Arrojadiza (6/18 m)"},
    {"Name": "Gran garrote", "Price": "2 pl", "CA": "", "Damage": "1d8 Contundente", "Peso": "4,5 kg", "Type": "Armas Cuerpo a Cuerpo Simples", "Properties": "A dos manos"},
    {"Name": "Hacha de mano", "Price": "5 po", "CA": "", "Damage": "1d6 Cortante", "Peso": "0,9 kg", "Type": "Armas Cuerpo a Cuerpo Simples", "Properties": "Ligera, Arrojadiza (6/18 m)"},
    {"Name": "Jabalina", "Price": "5 pl", "CA": "", "Damage": "1d6 Perforante", "Peso": "0,9 kg", "Type": "Armas Cuerpo a Cuerpo Simples", "Properties": "Arrojadiza (9/36 m)"},
    {"Name": "Martillo ligero", "Price": "2 po", "CA": "", "Damage": "1d4 Contundente", "Peso": "0,9 kg", "Type": "Armas Cuerpo a Cuerpo Simples", "Properties": "Ligera, Arrojadiza (6/18 m)"},
    {"Name": "Maza", "Price": "5 po", "CA": "", "Damage": "1d6 Contundente", "Peso": "2,25 kg", "Type": "Armas Cuerpo a Cuerpo Simples", "Properties": "-"},
    {"Name": "Bastón", "Price": "2 pl", "CA": "", "Damage": "1d6 Contundente", "Peso": "2,25 kg", "Type": "Armas Cuerpo a Cuerpo Simples", "Properties": "Versátil (1d8)"},
    {"Name": "Hoz", "Price": "1 po", "CA": "", "Damage": "1d4 Cortante", "Peso": "0,9 kg", "Type": "Armas Cuerpo a Cuerpo Simples", "Properties": "Ligera"},
    {"Name": "Lanza", "Price": "1 po", "CA": "", "Damage": "1d4 Perforante", "Peso": "1,35 kg", "Type": "Armas Cuerpo a Cuerpo Simples", "Properties": "Arrojadiza (6/18 m), Versátil (1d8)"},
    {"Name": "Ballesta ligera", "Price": "25 po", "CA": "", "Damage": "1d6 Perforante", "Peso": "2,25 kg", "Type": "Armas a Distancia Simples", "Properties": "Munición (24/96 m), Recarga, A dos manos"},
    {"Name": "Dardo", "Price": "5 pc", "CA": "", "Damage": "1d4 Perforante", "Peso": "0,11 kg", "Type": "Armas a Distancia Simples", "Properties": "Finura, Arrojadiza (6/18 m)"},
    {"Name": "Arco corto", "Price": "25 po", "CA": "", "Damage": "1d6 Perforante", "Peso": "0,9 kg", "Type": "Armas a Distancia Simples", "Properties": "Munición (24/96 m), A dos manos"},
    {"Name": "Honda", "Price": "1 pl", "CA": "", "Damage": "1d4 Contundente", "Peso": "-", "Type": "Armas a Distancia Simples", "Properties": "Munición (9/36 m)"},
    {"Name": "Hacha de batalla", "Price": "10 po", "CA": "", "Damage": "1d8 Cortante", "Peso": "1,8 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Versátil (1d10)"},
    {"Name": "Mangual", "Price": "10 po", "CA": "", "Damage": "1d8 Contundente", "Peso": "0,9 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "-"},
    {"Name": "Guja", "Price": "20 po", "CA": "", "Damage": "1d10 Cortante", "Peso": "2,7 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Pesada, Alcance, A dos manos"},
    {"Name": "Gran hacha", "Price": "30 po", "CA": "", "Damage": "1d12 Cortante", "Peso": "3,15 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Pesada, A dos manos"},
    {"Name": "Espadón", "Price": "50 po", "CA": "", "Damage": "2d6 Cortante", "Peso": "2,7 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Pesada, A dos manos"},
    {"Name": "Alabarda", "Price": "20 po", "CA": "", "Damage": "1d10 Cortante", "Peso": "2,7 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Pesada, Alcance, A dos manos"},
    {"Name": "Lanza de caballería", "Price": "10 po", "CA": "", "Damage": "1d12 Perforante", "Peso": "2,7 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Alcance, Especial"},
    {"Name": "Espada larga", "Price": "15 po", "CA": "", "Damage": "1d8 Cortante", "Peso": "1,35 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Versátil (1d10)"},
    {"Name": "Mazo", "Price": "10 po", "CA": "", "Damage": "2d6 Contundente", "Peso": "4,5 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Pesada, A dos manos"},
    {"Name": "Lucero del alba", "Price": "15 po", "CA": "", "Damage": "1d8 Perforante", "Peso": "1,8 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "-"},
    {"Name": "Pica", "Price": "5 po", "CA": "", "Damage": "1d10 Perforante", "Peso": "8,1 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Pesada, Alcance, A dos manos"},
    {"Name": "Estoque", "Price": "25 po", "CA": "", "Damage": "1d8 Perforante", "Peso": "0,9 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Finura"},
    {"Name": "Cimitarra", "Price": "25 po", "CA": "", "Damage": "1d6 Cortante", "Peso": "1,35 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Finura, Ligera"},
    {"Name": "Espada corta", "Price": "10 po", "CA": "", "Damage": "1d6 Cortante", "Peso": "0,9 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Finura, Ligera"},
    {"Name": "Tridente", "Price": "5 po", "CA": "", "Damage": "1d6 Perforante", "Peso": "2,25 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Arrojadiza (6/18 m), Versátil (1d8)"},
    {"Name": "Pico de guerra", "Price": "5 po", "CA": "", "Damage": "1d8 Perforante", "Peso": "0,9 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "-"},
    {"Name": "Martillo de guerra", "Price": "15 po", "CA": "", "Damage": "1d8 Contundente", "Peso": "0,9 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Versátil (1d10)"},
    {"Name": "Látigo", "Price": "2 po", "CA": "", "Damage": "1d4 Cortante", "Peso": "1,35 kg", "Type": "Armas Cuerpo a Cuerpo Marciales", "Properties": "Finura, Alcance"},
]
dnd_items_part_2 = [
    {"Name": "Cerbatana", "Price": "10 po", "CA": "", "Damage": "1 Perforante", "Peso": "0,45 kg", "Type": "Armas Marciales a Distancia", "Properties": "Munición (7,5/30 m), Recarga"},
    {"Name": "Ballesta de mano", "Price": "75 po", "CA": "", "Damage": "1d6 Perforante", "Peso": "1,35 kg", "Type": "Armas Marciales a Distancia", "Properties": "Munición (9/36 m), Recarga, Ligera"},
    {"Name": "Ballesta pesada", "Price": "50 po", "CA": "", "Damage": "1d10 Perforante", "Peso": "8,1 kg", "Type": "Armas Marciales a Distancia", "Properties": "Munición (30/120 m), Recarga, A dos manos, Pesada"},
    {"Name": "Arco largo", "Price": "50 po", "CA": "", "Damage": "1d8 Perforante", "Peso": "0,9 kg", "Type": "Armas Marciales a Distancia", "Properties": "Munición (45/180 m), Pesada, A dos manos"},
    {"Name": "Red", "Price": "1 po", "CA": "", "Damage": "", "Peso": "1,35 kg", "Type": "Armas Marciales a Distancia", "Properties": "Especial, Arrojadiza (1,5/4,5 m)"},
    
    {"Name": "Acolchada", "Price": "5 po", "CA": "11 + DES", "Damage": "", "Peso": "3,6 kg", "Type": "Armadura Ligera", "Properties": "Desventaja en Sigilo"},
    {"Name": "Cuero", "Price": "10 po", "CA": "11 + DES", "Damage": "", "Peso": "4,5 kg", "Type": "Armadura Ligera", "Properties": ""},
    {"Name": "Cuero tachonado", "Price": "45 po", "CA": "12 + DES", "Damage": "", "Peso": "5,9 kg", "Type": "Armadura Ligera", "Properties": ""},
    
    {"Name": "Piel", "Price": "10 po", "CA": "12 + DES (máx. 2)", "Damage": "", "Peso": "5,4 kg", "Type": "Armadura Media", "Properties": ""},
    {"Name": "Camisa de mallas", "Price": "50 po", "CA": "13 + DES (máx. 2)", "Damage": "", "Peso": "9 kg", "Type": "Armadura Media", "Properties": ""},
    {"Name": "Cota de escamas", "Price": "50 po", "CA": "14 + DES (máx. 2)", "Damage": "", "Peso": "20,4 kg", "Type": "Armadura Media", "Properties": "Desventaja en Sigilo"},
    {"Name": "Coraza", "Price": "400 po", "CA": "14 + DES (máx. 2)", "Damage": "", "Peso": "9 kg", "Type": "Armadura Media", "Properties": ""},
    {"Name": "Semiplaca", "Price": "750 po", "CA": "15 + DES (máx. 2)", "Damage": "", "Peso": "18 kg", "Type": "Armadura Media", "Properties": "Desventaja en Sigilo"},
    
    {"Name": "Armadura de anillas", "Price": "30 po", "CA": "14", "Damage": "", "Peso": "18 kg", "Type": "Armadura Pesada", "Properties": "Desventaja en Sigilo"},
    {"Name": "Cota de malla", "Price": "75 po", "CA": "16", "Damage": "", "Peso": "25 kg", "Type": "Armadura Pesada", "Properties": "Desventaja en Sigilo - Fuerza 13"},
    {"Name": "Armadura segmentada", "Price": "200 po", "CA": "17", "Damage": "", "Peso": "27 kg", "Type": "Armadura Pesada", "Properties": "Desventaja en Sigilo - Fuerza 15"},
    {"Name": "Armadura completa", "Price": "1500 po", "CA": "18", "Damage": "", "Peso": "29,5 kg", "Type": "Armadura Pesada", "Properties": "Desventaja en Sigilo - Fuerza 15"},
    
    {"Name": "Escudo", "Price": "10 po", "CA": "+2", "Damage": "", "Peso": "2,7 kg", "Type": "Escudo", "Properties": ""},
    
    # Municiones y componentes arcanos
    {"Name": "Flechas (20)", "Price": "1 po", "CA": "", "Damage": "", "Peso": "0,45 kg", "Type": "Munición", "Properties": ""},
    {"Name": "Agujas de cerbatana (50)", "Price": "1 po", "CA": "", "Damage": "", "Peso": "0,45 kg", "Type": "Munición", "Properties": ""},
    {"Name": "Virolas de ballesta (20)", "Price": "1 po", "CA": "", "Damage": "", "Peso": "0,68 kg", "Type": "Munición", "Properties": ""},
    {"Name": "Piedras de honda (20)", "Price": "4 pc", "CA": "", "Damage": "", "Peso": "0,68 kg", "Type": "Munición", "Properties": ""},
    
    {"Name": "Cristal", "Price": "10 po", "CA": "", "Damage": "", "Peso": "0,45 kg", "Type": "Foco Arcano", "Properties": ""},
    {"Name": "Orbe", "Price": "20 po", "CA": "", "Damage": "", "Peso": "1,35 kg", "Type": "Foco Arcano", "Properties": ""},
    {"Name": "Vara", "Price": "10 po", "CA": "", "Damage": "", "Peso": "0,9 kg", "Type": "Foco Arcano", "Properties": ""},
    {"Name": "Bastón", "Price": "5 po", "CA": "", "Damage": "", "Peso": "1,8 kg", "Type": "Foco Arcano", "Properties": ""},
    {"Name": "Varita", "Price": "10 po", "CA": "", "Damage": "", "Peso": "0,45 kg", "Type": "Foco Arcano", "Properties": ""},
    
    # Equipamiento de aventura
    {"Name": "Mochila", "Price": "2 po", "CA": "", "Damage": "", "Peso": "2,25 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Bolas de rodamiento (bolsa de 1000)", "Price": "1 po", "CA": "", "Damage": "", "Peso": "0,9 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Barril", "Price": "2 po", "CA": "", "Damage": "", "Peso": "31,5 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Cesta", "Price": "4 pl", "CA": "", "Damage": "", "Peso": "0,9 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Saco de dormir", "Price": "1 po", "CA": "", "Damage": "", "Peso": "3,2 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Campana", "Price": "1 po", "CA": "", "Damage": "", "Peso": "-", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Manta", "Price": "5 pl", "CA": "", "Damage": "", "Peso": "1,35 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Polea y cuerda", "Price": "1 po", "CA": "", "Damage": "", "Peso": "2,25 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Libro", "Price": "25 po", "CA": "", "Damage": "", "Peso": "2,25 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Botella de cristal", "Price": "2 po", "CA": "", "Damage": "", "Peso": "0,9 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Cubo", "Price": "5 pc", "CA": "", "Damage": "", "Peso": "0,9 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Trampas de pinchos (bolsa de 20)", "Price": "1 po", "CA": "", "Damage": "", "Peso": "0,9 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Vela", "Price": "1 pc", "CA": "", "Damage": "", "Peso": "-", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Estuche para virotes", "Price": "1 po", "CA": "", "Damage": "", "Peso": "0,45 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Estuche para mapas y pergaminos", "Price": "1 po", "CA": "", "Damage": "", "Peso": "0,45 kg", "Type": "Equipo de Aventura", "Properties": ""},
    {"Name": "Cadena (3 m)", "Price": "5 po", "CA": "", "Damage": "", "Peso": "4,5 kg", "Type": "Equipo de Aventura", "Properties": ""},
]
dnd_items_part_3 = [
  {"Name":"Tiza (1 pieza)", "Price":"1 pc", "CA":"null", "Damage":"null", "weight":"-", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Cofre", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"25 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Equipo de escalada", "Price":"25 po", "CA":"null", "Damage":"null", "weight":"12 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Ropa común", "Price":"5 pl", "CA":"null", "Damage":"null", "weight":"3 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Ropa de disfraz", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"4 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Ropa elegante", "Price":"15 po", "CA":"null", "Damage":"null", "weight":"6 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Ropa de viajero", "Price":"2 po", "CA":"null", "Damage":"null", "weight":"4 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Bolsa de componentes", "Price":"25 po", "CA":"null", "Damage":"null", "weight":"2 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Palanca", "Price":"2 po", "CA":"null", "Damage":"null", "weight":"5 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Rama de muérdago", "Price":"1 po", "CA":"null", "Damage":"null", "weight":"-", "Type":"Druidic Focus", "Properties":"null"},
  {"Name":"Tótem", "Price":"1 po", "CA":"null", "Damage":"null", "weight":"-", "Type":"Druidic Focus", "Properties":"null"},
  {"Name":"Bastón de madera", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"4 lb.", "Type":"Druidic Focus", "Properties":"null"},
  {"Name":"Varita de tejo", "Price":"10 po", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Druidic Focus", "Properties":"null"},
  {"Name":"Frasco o jarra", "Price":"1 po", "CA":"null", "Damage":"null", "weight":"4 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Frasco o jarra", "Price":"2 pc", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Gancho de escalada", "Price":"2 po", "CA":"null", "Damage":"null", "weight":"4 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Martillo", "Price":"1 po", "CA":"null", "Damage":"null", "weight":"3 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Mazo", "Price":"2 po", "CA":"null", "Damage":"null", "weight":"10 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Kit de curandero", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"3 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Amuleto", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Holy Symbol", "Properties":"null"},
  {"Name":"Emblema", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"-", "Type":"Holy Symbol", "Properties":"null"},
  {"Name":"Relicario", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"2 lb.", "Type":"Holy Symbol", "Properties":"null"},
  {"Name":"Agua bendita (frasco)", "Price":"25 po", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Reloj de arena", "Price":"25 po", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Trampa de caza", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"25 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Tinta (frasco de 1 onza)", "Price":"10 po", "CA":"null", "Damage":"null", "weight":"-", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Pluma", "Price":"2 pc", "CA":"null", "Damage":"null", "weight":"null", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Jarra o cántaro", "Price":"2 pc", "CA":"null", "Damage":"null", "weight":"4 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Escalera (3 metros)", "Price":"1 pl", "CA":"null", "Damage":"null", "weight":"25 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Lámpara", "Price":"5 pl", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Linterna de foco", "Price":"10 po", "CA":"null", "Damage":"null", "weight":"2 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Linterna cubierta", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"2 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Cerradura", "Price":"10 po", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Lupa", "Price":"100 po", "CA":"null", "Damage":"null", "weight":"-", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Grilletes", "Price":"2 po", "CA":"null", "Damage":"null", "weight":"6 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Equipo de comedor", "Price":"2 pl", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Espejo de acero", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"0.25 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Aceite (frasco)", "Price":"1 pl", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Papel (una hoja)", "Price":"2 pl", "CA":"null", "Damage":"null", "weight":"-", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Pergamino (una hoja)", "Price":"1 pl", "CA":"null", "Damage":"null", "weight":"-", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Perfume (frasco)", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"-", "Type":"Adventuring Gear", "Properties":"null"},
  {"Name":"Pico de minero", "Price":"2 po", "CA":"null", "Damage":"null", "weight":"10 lb.", "Type":"Adventuring Gear", "Properties":"null"}
]




def traducir(valor, diccionario):
    if pd.isna(valor):
        return None
    valor = str(valor).strip()
    return diccionario.get(valor, valor)

try:
    # Leer Excel
    df = pd.read_excel("Complete_Monster_List_-_public.xlsx")
    print("📥 Archivo Excel cargado correctamente.")

    # Insertar en la base de datos si no existe ya
    for i, row in df.iterrows():
        nombre = row['name']
        print(f"🔎 Revisando monstruo {i+1}: {nombre}...")


        monstruo = Items(
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


except Exception as e:
    print("❌ Ocurrió un error durante el procesamiento:")
    print(e)

finally:
    session.close()
    connection.close()
    print("🔒 Conexión cerrada.")
