import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError

# Conexión a la base de datos
URL_DATABASE = 'mysql+pymysql://root:WTZkbrdMGDhBOEjeEFILRWmzfZMvxQUW@centerbeam.proxy.rlwy.net:28820/railway?charset=utf8mb4'

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

    # Reinicia el autoincremental
    session.execute('ALTER TABLE items AUTO_INCREMENT = 1')
    session.commit()
    print("🔄 Autoincremental reiniciado a 1.")
except Exception as e:
    print(f"❌ Error al eliminar los datos existentes: {e}")
    session.rollback()


# Diccionarios de Items
dnd_items_part_1 = [
    {"Name": "Garrote", "Price": "1 pl", "CA": "", "Damage": "1d4 Contundente", "Peso": "0,9 kg", "Type": "Arma Cuerpo a Cuerpo Simple", "Properties": "Ligera"},
    {"Name": "Daga", "Price": "2 po", "CA": "", "Damage": "1d4 Perforante", "Peso": "0,45 kg", "Type": "Arma Cuerpo a Cuerpo Simple", "Properties": "Ligera, Finura, Arrojadiza (20/60 pies)"},
    {"Name": "Gran garrote", "Price": "2 pl", "CA": "", "Damage": "1d8 Contundente", "Peso": "4,5 kg", "Type": "Arma Cuerpo a Cuerpo Simple", "Properties": "A dos manos"},
    {"Name": "Hacha de mano", "Price": "5 po", "CA": "", "Damage": "1d6 Cortante", "Peso": "0,9 kg", "Type": "Arma Cuerpo a Cuerpo Simple", "Properties": "Ligera, Arrojadiza (20/60 pies)"},
    {"Name": "Jabalina", "Price": "5 pl", "CA": "", "Damage": "1d6 Perforante", "Peso": "0,9 kg", "Type": "Arma Cuerpo a Cuerpo Simple", "Properties": "Arrojadiza (30/120 pies)"},
    {"Name": "Martillo ligero", "Price": "2 po", "CA": "", "Damage": "1d4 Contundente", "Peso": "0,9 kg", "Type": "Arma Cuerpo a Cuerpo Simple", "Properties": "Ligera, Arrojadiza (20/60 pies)"},
    {"Name": "Maza", "Price": "5 po", "CA": "", "Damage": "1d6 Contundente", "Peso": "2,25 kg", "Type": "Arma Cuerpo a Cuerpo Simple", "Properties": "-"},
    {"Name": "Bastón", "Price": "2 pl", "CA": "", "Damage": "1d6 Contundente", "Peso": "2,25 kg", "Type": "Arma Cuerpo a Cuerpo Simple", "Properties": "Versátil (1d8)"},
    {"Name": "Hoz", "Price": "1 po", "CA": "", "Damage": "1d4 Cortante", "Peso": "0,9 kg", "Type": "Arma Cuerpo a Cuerpo Simple", "Properties": "Ligera"},
    {"Name": "Lanza", "Price": "1 po", "CA": "", "Damage": "1d4 Perforante", "Peso": "1,35 kg", "Type": "Arma Cuerpo a Cuerpo Simple", "Properties": "Arrojadiza (20/60 pies), Versátil (1d8)"},
    {"Name": "Ballesta ligera", "Price": "25 po", "CA": "", "Damage": "1d6 Perforante", "Peso": "2,25 kg", "Type": "Arma a Distancia Simple", "Properties": "Munición (80/320 pies), Recarga, A dos manos"},
    {"Name": "Dardo", "Price": "5 pc", "CA": "", "Damage": "1d4 Perforante", "Peso": "0,11 kg", "Type": "Arma a Distancia Simple", "Properties": "Finura, Arrojadiza (20/60 pies)"},
    {"Name": "Arco corto", "Price": "25 po", "CA": "", "Damage": "1d6 Perforante", "Peso": "0,9 kg", "Type": "Arma a Distancia Simple", "Properties": "Munición (80/320 pies), A dos manos"},
    {"Name": "Honda", "Price": "1 pl", "CA": "", "Damage": "1d4 Contundente", "Peso": "-", "Type": "Arma a Distancia Simple", "Properties": "Munición (30/120 pies)"},
    {"Name": "Hacha de batalla", "Price": "10 po", "CA": "", "Damage": "1d8 Cortante", "Peso": "1,8 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Versátil (1d10)"},
    {"Name": "Mangual", "Price": "10 po", "CA": "", "Damage": "1d8 Contundente", "Peso": "0,9 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "-"},
    {"Name": "Guja", "Price": "20 po", "CA": "", "Damage": "1d10 Cortante", "Peso": "2,7 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Pesada, Alcance, A dos manos"},
    {"Name": "Gran hacha", "Price": "30 po", "CA": "", "Damage": "1d12 Cortante", "Peso": "3,15 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Pesada, A dos manos"},
    {"Name": "Espadón", "Price": "50 po", "CA": "", "Damage": "2d6 Cortante", "Peso": "2,7 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Pesada, A dos manos"},
    {"Name": "Alabarda", "Price": "20 po", "CA": "", "Damage": "1d10 Cortante", "Peso": "2,7 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Pesada, Alcance, A dos manos"},
    {"Name": "Lanza de caballería", "Price": "10 po", "CA": "", "Damage": "1d12 Perforante", "Peso": "2,7 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Alcance, Especial"},
    {"Name": "Espada larga", "Price": "15 po", "CA": "", "Damage": "1d8 Cortante", "Peso": "1,35 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Versátil (1d10)"},
    {"Name": "Mazo", "Price": "10 po", "CA": "", "Damage": "2d6 Contundente", "Peso": "4,5 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Pesada, A dos manos"},
    {"Name": "Lucero del alba", "Price": "15 po", "CA": "", "Damage": "1d8 Perforante", "Peso": "1,8 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "-"},
    {"Name": "Pica", "Price": "5 po", "CA": "", "Damage": "1d10 Perforante", "Peso": "8,1 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Pesada, Alcance, A dos manos"},
    {"Name": "Estoque", "Price": "25 po", "CA": "", "Damage": "1d8 Perforante", "Peso": "0,9 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Finura"},
    {"Name": "Cimitarra", "Price": "25 po", "CA": "", "Damage": "1d6 Cortante", "Peso": "1,35 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Finura, Ligera"},
    {"Name": "Espada corta", "Price": "10 po", "CA": "", "Damage": "1d6 Cortante", "Peso": "0,9 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Finura, Ligera"},
    {"Name": "Tridente", "Price": "5 po", "CA": "", "Damage": "1d6 Perforante", "Peso": "2,25 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Arrojadiza (20/60 pies), Versátil (1d8)"},
    {"Name": "Pico de guerra", "Price": "5 po", "CA": "", "Damage": "1d8 Perforante", "Peso": "0,9 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "-"},
    {"Name": "Martillo de guerra", "Price": "15 po", "CA": "", "Damage": "1d8 Contundente", "Peso": "0,9 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Versátil (1d10)"},
    {"Name": "Látigo", "Price": "2 po", "CA": "", "Damage": "1d4 Cortante", "Peso": "1,35 kg", "Type": "Arma Cuerpo a Cuerpo Marciale", "Properties": "Finura, Alcance"},
]
dnd_items_part_2 = [
    {"Name": "Cerbatana", "Price": "10 po", "CA": "", "Damage": "1 Perforante", "Peso": "0,45 kg", "Type": "Arma Marciale a Distancia", "Properties": "Munición (25/100 pies), Recarga"},
    {"Name": "Ballesta de mano", "Price": "75 po", "CA": "", "Damage": "1d6 Perforante", "Peso": "1,35 kg", "Type": "Arma Marciale a Distancia", "Properties": "Munición (30/120 pies), Recarga, Ligera"},
    {"Name": "Ballesta pesada", "Price": "50 po", "CA": "", "Damage": "1d10 Perforante", "Peso": "8,1 kg", "Type": "Arma Marciale a Distancia", "Properties": "Munición (100/400 pies), Recarga, A dos manos, Pesada"},
    {"Name": "Arco largo", "Price": "50 po", "CA": "", "Damage": "1d8 Perforante", "Peso": "0,9 kg", "Type": "Arma Marciale a Distancia", "Properties": "Munición (150/600 pies), Pesada, A dos manos"},
    {"Name": "Red", "Price": "1 po", "CA": "", "Damage": "", "Peso": "1,35 kg", "Type": "Arma Marciale a Distancia", "Properties": "Especial, Arrojadiza (5/15 pies)"},
    
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
    {"Name": "Cadena (10 pies)", "Price": "5 po", "CA": "", "Damage": "", "Peso": "4,5 kg", "Type": "Equipo de Aventura", "Properties": ""},
]
dnd_items_part_3 = [
  {"Name":"Tiza (1 pieza)", "Price":"1 pc", "CA":"null", "Damage":"null", "weight":"-", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Cofre", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"25 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Equipo de escalada", "Price":"25 po", "CA":"null", "Damage":"null", "weight":"12 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Ropa común", "Price":"5 pl", "CA":"null", "Damage":"null", "weight":"3 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Ropa de Disfraz", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"4 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Ropa elegante", "Price":"15 po", "CA":"null", "Damage":"null", "weight":"6 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Ropa de viajero", "Price":"2 po", "CA":"null", "Damage":"null", "weight":"4 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Bolsa de componentes", "Price":"25 po", "CA":"null", "Damage":"null", "weight":"2 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Palanca", "Price":"2 po", "CA":"null", "Damage":"null", "weight":"5 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Rama de muérdago", "Price":"1 po", "CA":"null", "Damage":"null", "weight":"-", "Type":"Foco Druidico", "Properties":"null"},
  {"Name":"Tótem", "Price":"1 po", "CA":"null", "Damage":"null", "weight":"-", "Type":"Foco Druidico", "Properties":"null"},
  {"Name":"Bastón de madera", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"4 lb.", "Type":"Foco Druidico", "Properties":"null"},
  {"Name":"Varita de tejo", "Price":"10 po", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Foco Druidico", "Properties":"null"},
  {"Name":"Frasco o jarra", "Price":"1 po", "CA":"null", "Damage":"null", "weight":"4 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Frasco o jarra", "Price":"2 pc", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Gancho de escalada", "Price":"2 po", "CA":"null", "Damage":"null", "weight":"4 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Martillo", "Price":"1 po", "CA":"null", "Damage":"null", "weight":"3 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Mazo", "Price":"2 po", "CA":"null", "Damage":"null", "weight":"10 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Kit de Curandero", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"3 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Amuleto", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Simbolo Sagrado", "Properties":"null"},
  {"Name":"Emblema", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"-", "Type":"Simbolo Sagrado", "Properties":"null"},
  {"Name":"Relicario", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"2 lb.", "Type":"Simbolo Sagrado", "Properties":"null"},
  {"Name":"Agua bendita (frasco)", "Price":"25 po", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Reloj de arena", "Price":"25 po", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Trampa de caza", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"25 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Tinta (frasco de 1 onza)", "Price":"10 po", "CA":"null", "Damage":"null", "weight":"-", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Pluma", "Price":"2 pc", "CA":"null", "Damage":"null", "weight":"null", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Jarra o cántaro", "Price":"2 pc", "CA":"null", "Damage":"null", "weight":"4 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Escalera (10 pies)", "Price":"1 pl", "CA":"null", "Damage":"null", "weight":"25 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Lámpara", "Price":"5 pl", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Linterna de foco", "Price":"10 po", "CA":"null", "Damage":"null", "weight":"2 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Linterna cubierta", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"2 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Cerradura", "Price":"10 po", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Lupa", "Price":"100 po", "CA":"null", "Damage":"null", "weight":"-", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Grilletes", "Price":"2 po", "CA":"null", "Damage":"null", "weight":"6 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Equipo de comedor", "Price":"2 pl", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Espejo de acero", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"0.25 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Aceite (frasco)", "Price":"1 pl", "CA":"null", "Damage":"null", "weight":"1 lb.", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Papel (una hoja)", "Price":"2 pl", "CA":"null", "Damage":"null", "weight":"-", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Pergamino (una hoja)", "Price":"1 pl", "CA":"null", "Damage":"null", "weight":"-", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Perfume (frasco)", "Price":"5 po", "CA":"null", "Damage":"null", "weight":"-", "Type":"Equipo de Aventura", "Properties":"null"},
  {"Name":"Pico de minero", "Price":"2 po", "CA":"null", "Damage":"null", "weight":"10 lb.", "Type":"Equipo de Aventura", "Properties":"null"}
]
dnd_items_part_4 = [
  {"Name":"Piedra de afilar", "Price":"1 pc", "AC":"null", "Damage":"null", "Weight":"1 lb.", "Type":"Equipo de Aventura"},
  {"Name":"Pergamino de conjuro nivel 0", "Price":"25 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Consumible - Pergamino"},
  {"Name":"Pergamino de conjuro nivel 1", "Price":"35 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Pergamino"},
  {"Name":"Pergamino de conjuro nivel 2", "Price":"280 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Pergamino"},
  {"Name":"Pergamino de conjuro nivel 3", "Price":"570 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Pergamino"},
  {"Name":"Pergamino de conjuro nivel 4", "Price":"2640 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Pergamino"},
  {"Name":"Pergamino de conjuro nivel 5", "Price":"5280 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Pergamino"},
  {"Name":"Pergamino de conjuro nivel 6", "Price":"15560 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Pergamino"},
  {"Name":"Pergamino de conjuro nivel 7", "Price":"26220 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Pergamino"},
  {"Name":"Pergamino de conjuro nivel 8", "Price":"52240 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Pergamino"},
  {"Name":"Pergamino de conjuro nivel 9", "Price":"253360 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Pergamino"},
  {"Name":"Pergamino de protección", "Price":"200 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Pergamino"},
  {"Name":"Pinturas maravillosas de Nolzur", "Price":"200 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Munición +1 (por unidad)", "Price":"15 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Arma"},
  {"Name":"Munición +2 (por unidad)", "Price":"50 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Arma"},
  {"Name":"Munición +3 (por unidad)", "Price":"250 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Arma"},
  {"Name":"Ungüento de Keoghtom (1 dosis)", "Price":"150 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Pluma mágica de Quaal - Ancla", "Price":"50 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Pluma mágica de Quaal - Abanico", "Price":"120 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Pluma mágica de Quaal - Látigo", "Price":"100 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Pluma mágica de Quaal - Pájaro", "Price":"1000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Pluma mágica de Quaal - Cisne barco", "Price":"300 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Pluma mágica de Quaal - Árbol", "Price":"200 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Baraja de ilusiones", "Price":"900 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Polvo de desaparición", "Price":"300 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Solvente universal", "Price":"300 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Polvo de sequedad (por pizca)", "Price":"100 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Pegamento soberano", "Price":"400 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Cuerno de explosión", "Price":"450 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Polvo de estornudos y asfixia", "Price":"400 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Flecha aniquiladora", "Price":"400 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Arma"},
  {"Name":"Perla de fuerza", "Price":"1000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Gema elemental", "Price":"600 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Collar de bolas de fuego (1 cuenta)", "Price":"300 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Collar de bolas de fuego (2 cuentas)", "Price":"500 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Collar de bolas de fuego (3 cuentas)", "Price":"1000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Collar de bolas de fuego (4 cuentas)", "Price":"1600 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Collar de bolas de fuego (5 cuentas)", "Price":"4000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Collar de bolas de fuego (6 cuentas)", "Price":"8000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Campana de apertura", "Price":"400 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Piedra de Ioun de absorción", "Price":"2400 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"},
  {"Name":"Piedra de Ioun de gran absorción", "Price":"30000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Consumible - Maravilloso"}
]
dnd_items_part_5 = [
    {"Name": "Gema de Brillo", "Price": "350 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Consumible - Maravilloso"},
    {"Name": "Vara de Absorción", "Price": "35,000 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Consumible - Vara"},
    {"Name": "Talismán del Mal Supremo", "Price": "62,000 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Consumible - Maravilloso"},
    {"Name": "Talismán del Bien Puro", "Price": "72,000 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Consumible - Maravilloso"},
    {"Name": "Túnica de Objetos Útiles", "Price": "300 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Consumible - Armadura"},
    {"Name": "Manual de Salud Corporal", "Price": "55,000 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Consumible - Maravilloso"},
    {"Name": "Manual de Ejercicio Rentable", "Price": "55,000 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Consumible - Maravilloso"},
    {"Name": "Manual de Rapidez de Acción", "Price": "55,000 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Consumible - Maravilloso"},
    {"Name": "Manual de Mente Aguda", "Price": "55,000 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Consumible - Maravilloso"},
    {"Name": "Manual de Glamour y Prestigio", "Price": "55,000 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Consumible - Maravilloso"},
    {"Name": "Manual de Previsión Prudente", "Price": "55,000 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Consumible - Maravilloso"},
    {"Name": "Yelmo de Comprensión de Idiomas", "Price": "500 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Globo de Deriva", "Price": "300 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Tridente del Mando de Peces", "Price": "400 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Gorra de Respiración Acuática", "Price": "400 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Botella de Humo Perpetuo", "Price": "200 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Carcaj de Ehlonna", "Price": "250 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Piedra de Ioun de Sostenimiento", "Price": "1,000 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Collar de Adaptación", "Price": "800 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Gafas de Visión Nocturna", "Price": "750 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Herraduras del Céfiro", "Price": "1,500 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Varita de Detección Mágica", "Price": "500 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Varita"},
    {"Name": "Varita de Secretos", "Price": "250 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Varita"},
    {"Name": "Guantes de Nado y Escalada", "Price": "500 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Mochila Útil de Heward", "Price": "350 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Cuerda de Escalada", "Price": "350 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Botas de los Elfos", "Price": "275 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"},
    {"Name": "Ojos de Observación Minuciosa", "Price": "150 gp", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso"}
]
dnd_items_part_6 = [
    {"Name": "Ojos del Águila", "Price": "250 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Grilletes Dimensionales", "Price": "1,500 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Raro"},
    {"Name": "Ojos de Encantamiento", "Price": "900 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Agujero Portátil", "Price": "4,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Raro"},
    {"Name": "Bolsa de Contención", "Price": "500 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común"},
    {"Name": "Botas de Levitación", "Price": "2,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Raro - Requiere vinculación"},
    {"Name": "Botas de Zancada y Salto", "Price": "400 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Capa de la Araña", "Price": "5,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Muy raro - Requiere vinculación"},
    {"Name": "Capa Élfica", "Price": "500 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Guantes de Latrocinio", "Price": "300 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común"},
    {"Name": "Sombrero de Disfraz", "Price": "1,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Herraduras de Velocidad", "Price": "500 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Raro"},
    {"Name": "Vara Inamovible", "Price": "200 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común"},
    {"Name": "Linterna Reveladora", "Price": "1,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común"},
    {"Name": "Periapto de Salud", "Price": "1,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común"},
    {"Name": "Periapto de Prueba contra el Veneno", "Price": "1,500 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Raro"},
    {"Name": "Zapatillas de Trepar Paredes", "Price": "500 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común"},
    {"Name": "Capa del Murciélago", "Price": "1,300 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Raro - Requiere vinculación"},
    {"Name": "Capa de la Mantarraya", "Price": "800 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común"},
    {"Name": "Capa del Charlatán", "Price": "1,250 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Raro"},
    {"Name": "Talismán de la Esfera", "Price": "20,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Legendario - Requiere vinculación"},
    {"Name": "Aparato de Kwalish", "Price": "10,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Legendario"},
    {"Name": "Botas de las Tierras Invernal", "Price": "350 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Barco Plegable", "Price": "5,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Raro"},
    {"Name": "Yelmo de Telepatía", "Price": "1,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Cubo de Fuerza", "Price": "5,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Raro - Requiere vinculación"},
    {"Name": "Vara de Dominio", "Price": "4,500 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Varita", "Properties": "Raro - Requiere vinculación"},
    {"Name": "Espejo de Trampa Vital", "Price": "18,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Muy raro"},
    {"Name": "Amuleto de Prueba contra Detección y Localización", "Price": "1,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Medallón de Pensamientos", "Price": "700 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Jarra de Alquimia", "Price": "450 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común"},
    {"Name": "Piedras de Envío", "Price": "200 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común"},
    {"Name": "Cubo de Portal", "Price": "40,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Legendario"},
    {"Name": "Bola de Cristal", "Price": "50,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Muy raro - Requiere vinculación"},
    {"Name": "Fortaleza Instantánea de Daern", "Price": "5,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Raro"},
    {"Name": "Capa de Invisibilidad", "Price": "50,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Legendario - Requiere vinculación"},
    {"Name": "Decantador de Agua Infinita", "Price": "500 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común"},
    {"Name": "Amuleto de los Planos", "Price": "90,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Muy raro - Requiere vinculación"},
    {"Name": "Gema de Visión", "Price": "800 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Raro - Requiere vinculación"},
    {"Name": "Anillo de Protección Mental", "Price": "2,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Anillo", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Anillo de Invisibilidad", "Price": "10,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Anillo", "Properties": "Legendario - Requiere vinculación"},
    {"Name": "Anillo de Visión de Rayos X", "Price": "3,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Anillo", "Properties": "Raro - Requiere vinculación"},
    {"Name": "Anillo de Telequinesis", "Price": "4,800 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Anillo", "Properties": "Muy raro - Requiere vinculación"},
    {"Name": "Anillo de Tres Deseos", "Price": "150,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Anillo", "Properties": "Legendario - Requiere vinculación"},
    {"Name": "Anillo de Mando Elemental del Aire", "Price": "35,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Anillo", "Properties": "Legendario"},
    {"Name": "Anillo de Mando Elemental de la Tierra", "Price": "31,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Anillo", "Properties": "Legendario - Requiere vinculación"},
    {"Name": "Anillo de Influencia Animal", "Price": "1,350 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Anillo", "Properties": "Raro"},
    {"Name": "Anillo de Natación", "Price": "300 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Anillo", "Properties": "Poco común"},
    {"Name": "Anillo de Salto", "Price": "500 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Anillo", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Anillo de Caminar sobre el Agua", "Price": "450 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Anillo", "Properties": "Poco común"},
    {"Name": "Anillo de Calor", "Price": "350 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Anillo", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Escoba Voladora", "Price": "2,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común"},
    {"Name": "Alas Voladoras", "Price": "5,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Raro - Requiere vinculación"},
    {"Name": "Botas Aladas", "Price": "4,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Poco común - Requiere vinculación"},
    {"Name": "Alfombra Voladora 3x5", "Price": "8,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Muy raro"},
    {"Name": "Alfombra Voladora 4x6", "Price": "16,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Muy raro"},
    {"Name": "Alfombra Voladora 5x7", "Price": "24,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Muy raro"},
    {"Name": "Alfombra Voladora 6x9", "Price": "32,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Maravilloso", "Properties": "Muy raro"},
    {"Name": "Vara de Resurrección", "Price": "50,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - No Combate - Vara", "Properties": "Legendario - Requiere sintonización"},
    {"Name": "Cabra de Marfil (Trabajo)", "Price": "400 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Invocación / Mascotas - Maravilloso", "Properties": "Raro"},
    {"Name": "Cabra de Marfil (Viaje)", "Price": "700 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Invocación / Mascotas - Maravilloso", "Properties": "Raro"},
    {"Name": "Cabra de Marfil (Terror)", "Price": "3,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Invocación / Mascotas - Maravilloso", "Properties": "Raro"},
    {"Name": "León Dorado", "Price": "600 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Invocación / Mascotas - Maravilloso", "Properties": "Raro"},
    {"Name": "Bastón de la Pitón", "Price": "200 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Invocación / Mascotas - Maravilloso", "Properties": "Poco común - Requiere sintonización"},
    {"Name": "Perro de Ónix", "Price": "500 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Invocación / Mascotas - Maravilloso", "Properties": "Raro"},
    {"Name": "Cuervo de Plata", "Price": "5,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Invocación / Mascotas - Maravilloso", "Properties": "Poco común"},
    {"Name": "Cuerno de Plata de Valhalla", "Price": "5,600 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Invocación / Mascotas - Maravilloso", "Properties": "Raro"},
    {"Name": "Elefante de Mármol", "Price": "800 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Invocación / Mascotas - Maravilloso", "Properties": "Raro"},
    {"Name": "Cuenco de Mando de Elementales de Agua", "Price": "8,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Invocación / Mascotas - Maravilloso", "Properties": "Raro"},
    {"Name": "Brasero de Mando de Elementales de Fuego", "Price": "8,000 po", "AC": "", "Damage": "", "Weight": "", "Type": "Magico - Invocación / Mascotas - Maravilloso", "Properties": "Raro"}
]
dnd_items_part_7 = [
    {"Name":"Incensario de Control de Elementales de Aire", "Price":"8.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Invocaciones / Mascotas - Maravilloso", "Properties":"Raro"},
    {"Name":"Piedra de Control de Elementales de Tierra", "Price":"8.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Invocaciones / Mascotas - Maravilloso", "Properties":"Raro"},
    {"Name":"Cuerno de Bronce de Valhalla", "Price":"8.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Invocaciones / Mascotas - Maravilloso", "Properties":"Raro"},
    {"Name":"Cuerno de Latón de Valhalla", "Price":"11.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Invocaciones / Mascotas - Maravilloso", "Properties":"Muy raro"},
    {"Name":"Cuerno de Hierro de Valhalla", "Price":"14.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Invocaciones / Mascotas - Maravilloso", "Properties":"Legendario"},
    {"Name":"Búho Serpentino", "Price":"8.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Invocaciones / Mascotas - Maravilloso", "Properties":"Raro"},
    {"Name":"Grifo de Bronce", "Price":"4.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Invocaciones / Mascotas - Maravilloso", "Properties":"Raro"},
    {"Name":"Mosca de Ébano", "Price":"6.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Invocaciones / Mascotas - Maravilloso", "Properties":"Raro"},
    {"Name":"Corcel de Obsidiana", "Price":"20.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Invocaciones / Mascotas - Maravilloso", "Properties":"Muy raro"},
    {"Name":"Armadura (+1)", "Price":"1.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Armadura", "Properties":"Raro"},
    {"Name":"Escudo (+1)", "Price":"500 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Armadura", "Properties":"Poco común"},
    {"Name":"Arma (+1)", "Price":"700 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Arma", "Properties":"Poco común"},
    {"Name":"Armadura (+2)", "Price":"5.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Armadura", "Properties":"Muy raro"},
    {"Name":"Escudo (+2)", "Price":"2.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Armadura", "Properties":"Raro"},
    {"Name":"Arma (+2)", "Price":"2.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Arma", "Properties":"Raro"},
    {"Name":"Armadura (+3)", "Price":"30.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Armadura", "Properties":"Legendario"},
    {"Name":"Escudo (+3)", "Price":"20.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Armadura", "Properties":"Legendario"},
    {"Name":"Arma (+3)", "Price":"8.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Arma", "Properties":"Muy raro"},
    {"Name":"Armadura de Adamantina", "Price":"Armadura + 500 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Armadura", "Properties":"Poco común"},
    {"Name":"Amuleto de la Salud", "Price":"3.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Maravilloso", "Properties":"Raro - Requiere vinculación"},
    {"Name":"Escudo Animado", "Price":"4.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Armadura", "Properties":"Muy raro - Requiere vinculación"},
    {"Name":"Armadura de la Invulnerabilidad", "Price":"50.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Armadura", "Properties":"Legendario - Requiere vinculación"},
    {"Name":"Armadura de Resistencia", "Price":"Armadura + 500 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Armadura", "Properties":"Raro - Requiere vinculación"},
    {"Name":"Escudo Atrapa-Flechas", "Price":"3.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Armadura", "Properties":"Raro - Requiere vinculación"},
    {"Name":"Cinturón de Fuerza de Gigante de Nubes", "Price":"50.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Maravilloso", "Properties":"Legendario - Requiere vinculación"},
    {"Name":"Cinturón del Linaje Enano", "Price":"3.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Maravilloso", "Properties":"Raro - Requiere vinculación"},
    {"Name":"Cinturón de Fuerza de Gigante de Fuego", "Price":"25.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Maravilloso", "Properties":"Muy raro - Requiere vinculación"},
    {"Name":"Cinturón de Fuerza de Gigante de Escarcha", "Price":"10.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Maravilloso", "Properties":"Muy raro - Requiere vinculación"},
    {"Name":"Cinturón de Fuerza de Gigante de Colina", "Price":"5.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Maravilloso", "Properties":"Raro - Requiere vinculación"},
    {"Name":"Cinturón de Fuerza de Gigante de Piedra", "Price":"10.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Maravilloso", "Properties":"Muy raro - Requiere vinculación"},
    {"Name":"Cinturón de Fuerza de Gigante de Tormenta", "Price":"Tu alma", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Maravilloso", "Properties":"Legendario - Requiere vinculación"},
    {"Name":"Botas de Velocidad", "Price":"800 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Maravilloso", "Properties":"Raro - Requiere vinculación"},
    {"Name":"Brazales de Tiro con Arco", "Price":"500 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Maravilloso", "Properties":"Poco común - Requiere vinculación"},
    {"Name":"Brazales de Defensa", "Price":"4.000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Maravilloso", "Properties":"Raro - Requiere vinculación"},
    {"Name":"Broche de Protección", "Price":"500 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Magico - Combate - Maravilloso", "Properties":"Poco común - Requiere vinculación"},
    {"Name":"Aro de Explosión", "Price":"500 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Poco Común"},
    {"Name":"Capa de Desplazamiento", "Price":"8000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Rara - Requiere Vinculación"},
    {"Name":"Capa de Protección", "Price":"1000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Poco Común - Requiere Vinculación"},
    {"Name":"Daga de Veneno", "Price":"800 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Arma", "Properties":"Rara"},
    {"Name":"Espada Danzarina", "Price":"5000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Arma", "Properties":"Muy Rara - Requiere Vinculación"},
    {"Name":"Defensora", "Price":"20000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Arma", "Properties":"Legendaria - Requiere Vinculación"},
    {"Name":"Armadura de Escamas de Dragón", "Price":"4000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Muy Rara - Requiere Vinculación"},
    {"Name":"Asesina de Dragones", "Price":"2000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Arma", "Properties":"Rara - Requiere Vinculación"},
    {"Name":"Armadura Enana", "Price":"6000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Muy Rara"},
    {"Name":"Arrojador Enano", "Price":"6000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Arma", "Properties":"Muy Rara - Requiere Vinculación"},
    {"Name":"Cadena de Efrit", "Price":"50000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Legendaria - Requiere Vinculación"},
    {"Name":"Cota Élfica", "Price":"2000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Rara"},
    {"Name":"Lengua de Llama", "Price":"3000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Arma", "Properties":"Rara - Requiere Vinculación"},
    {"Name":"Marca de Escarcha", "Price":"2000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Arma", "Properties":"Muy Rara - Requiere Vinculación"},
    {"Name":"Guanteletes de Poder de Ogro", "Price":"1000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Poco Común - Requiere Vinculación"},
    {"Name":"Asesina de Gigantes", "Price":"1200 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Arma", "Properties":"Rara - Requiere Vinculación"},
    {"Name":"Armadura Ilusionada", "Price":"2000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Rara"},
    {"Name":"Guantes Atrapa Proyectiles", "Price":"450 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Poco Común - Requiere Vinculación"},
    {"Name":"Martillo de los Rayos", "Price":"8000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Arma", "Properties":"Legendaria - Requiere Vinculación"},
    {"Name":"Cinta de Intelecto", "Price":"1000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Poco Común - Requiere Vinculación"},
    {"Name":"Yelmo del Brillo", "Price":"15000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Muy Rara - Requiere Vinculación"},
    {"Name":"Yelmo de Teletransportación", "Price":"40000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Rara - Requiere Vinculación"},
    {"Name":"Vengador Sagrado", "Price":"90000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Arma", "Properties":"Legendaria - Requiere Vinculación"},
    {"Name":"Instrumento de los Bardos - Arpa Anstruth", "Price":"5000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Muy Rara - Requiere Vinculación"},
    {"Name":"Instrumento de los Bardos - Mandolina Canaith", "Price":"2500 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Rara - Requiere Vinculación"},
    {"Name":"Instrumento de los Bardos - Lira Cli", "Price":"2500 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Rara - Requiere Vinculación"},
    {"Name":"Instrumento de los Bardos - Laúd Doss", "Price":"1500 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Poco Común - Requiere Vinculación"},
    {"Name":"Instrumento de los Bardos - Bandlore Fochulan", "Price":"1500 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Poco Común - Requiere Vinculación"},
    {"Name":"Instrumento de los Bardos - Cítara Mac-Fuirmidh", "Price":"2000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Poco Común - Requiere Vinculación"},
    {"Name":"Instrumento de los Bardos - Arpa Ollamh", "Price":"70000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Legendaria - Requiere Vinculación"},
    {"Name":"Piedra de Ioun - Agilidad", "Price":"3000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Muy Rara - Requiere Vinculación"},
    {"Name":"Piedra de Ioun - Conciencia", "Price":"500 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Rara - Requiere Vinculación"},
    {"Name":"Piedra de Ioun - Fortaleza", "Price":"3000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Muy Rara - Requiere Vinculación"},
    {"Name":"Piedra de Ioun - Perspicacia", "Price":"3000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Muy Rara - Requiere Vinculación"},
    {"Name":"Piedra de Ioun - Intelecto", "Price":"3000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Muy Rara - Requiere Vinculación"}

]
dnd_items_part_8 = [
    {"Name":"Piedra Ioun de Liderazgo", "Price":"3,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Muy Raro - Requiere Afinidad"},
  {"Name":"Piedra Ioun de Maestria", "Price":"8,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Legendario - Requiere Afinidad"},
  {"Name":"Piedra Ioun de Proteción", "Price":"1,200 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Piedra Ioun de Regeneración", "Price":"5,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Legendario - Requiere Afinidad"},
  {"Name":"Piedra Ioun de Reserva", "Price":"10,500 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Piedra Ioun de Fuerza", "Price":"3,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Muy Raro - Requiere Afinidad"},
  {"Name":"Bandas de Hierro de Bilarro", "Price":"2,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Raro"},
  {"Name":"Jabalina de Relámpago", "Price":"150 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Arma", "Properties":"Poco Común"},
  {"Name":"Espada de la Suerte (Por Carga)", "Price":"50,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Legendario - Requiere Afinidad"},
  {"Name":"Piedra de la Suerte", "Price":"500 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Poco Común - Requiere Afinidad"},
  {"Name":"Maza de Disrupción", "Price":"3,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Arma", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Maza de Castigo", "Price":"1,500 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Arma", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Maza de Terror", "Price":"2,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Arma", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Manto de Resistencia a Hechizos", "Price":"1,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Armadura", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Armadura del Marinero", "Price":"Armadura + 200 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Armadura", "Properties":"Poco Común"},
  {"Name":"Armadura Mithril", "Price":"Armadura + 800 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Armadura", "Properties":"Poco Común"},
  {"Name":"Robavidas (Completamente Cargado)", "Price":"7,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Arma", "Properties":"Muy Raro - Requiere Afinidad"},
  {"Name":"Arco del Juramento", "Price":"4,500 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Arma", "Properties":"Muy Raro - Requiere Afinidad"},
  {"Name":"Perla de Poder", "Price":"500 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Poco Común - Requiere Afinidad"},
  {"Name":"Amuleto de Cierre de Heridas", "Price":"900 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Poco Común - Requiere Afinidad"},
  {"Name":"Flautas de Aterrorización", "Price":"600 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Poco Común"},
  {"Name":"Flautas de las Alcantarillas", "Price":"200 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Poco Común - Requiere Afinidad"},
  {"Name":"Armadura de Placas de Eterealidad", "Price":"48,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Armadura", "Properties":"Legendario - Requiere Afinidad"},
  {"Name":"Cuenta de oración - Bendecir", "Price":"200 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Cuenta de oración - Curación", "Price":"1,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Cuenta de oración - Gran Restauración", "Price":"2,500 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Cuenta de oración - Castigo", "Price":"300 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Cuenta de oración - Invocaciones", "Price":"5,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Cuenta de oración - Caminata en el viento", "Price":"1,200 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Maravilloso", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Anillo de Evasión", "Price":"2,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Anillo", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Anillo de Caída de Pluma", "Price":"800 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Anillo", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Anillo de Comando Elemental de Fuego", "Price":"15,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Anillo", "Properties":"Legendario - Requiere Afinidad"},
  {"Name":"Anillo de Acción Libre", "Price":"2,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Anillo", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Anillo de Protección", "Price":"2,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Anillo", "Properties":"Raro - Requiere Afinidad"},
  {"Name":"Anillo de Regeneración", "Price":"10,000 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Objeto Mágico - Combate - Anillo", "Properties":"Muy Raro - Requiere Afinidad"},
  
  
  {"Name":"Anillo de Resistencia", "Price":"1,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Anillo", "Properties":"Rare - Requires Attunement"},
  {"Name":"Anillo de Estrellas Fugaces", "Price":"8,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Anillo", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Anillo de Almacenamiento de Hechizos", "Price":"3,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Anillo", "Properties":"Rare - Requires Attunement"},
  {"Name":"Anillo de Reversión de Hechizos", "Price":"20,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Anillo", "Properties":"Legendary - Requires Attunement"},
  {"Name":"Anillo del Carnero", "Price":"1,500 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Anillo", "Properties":"Rare - Requires Attunement"},
  {"Name":"Anillo de Dominio del Elemental de Agua", "Price":"20,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Anillo", "Properties":"Legendary - Requires Attunement"},
  {"Name":"Túnica de los Ojos", "Price":"2,500 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Rare - Requires Attunement"},
  {"Name":"Túnica de Colores Cintilantes", "Price":"4,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Túnica de las Estrellas", "Price":"6,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Túnica del Archimago", "Price":"50,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Legendary - Requires Attunement"},
  {"Name":"Vara de Alerta", "Price":"5,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Varita", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Vara del Poderoso Señor", "Price":"15,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Varita", "Properties":"Legendary - Requires Attunement"},
  {"Name":"Vara de Seguridad", "Price":"20,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Varita", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Vara del Guardián del Pacto +1", "Price":"900 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Varita", "Properties":"Uncommon - Requires Attunement"},
  {"Name":"Vara del Guardián del Pacto +2", "Price":"3,500 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Varita", "Properties":"Rare - Requires Attunement"},
  {"Name":"Vara del Guardián del Pacto +3", "Price":"11,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Varita", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Cuerda de Enredamiento", "Price":"600 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Rare"},
  {"Name":"Silla de Montar del Caballero", "Price":"150 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Uncommon"},
  {"Name":"Escarabajo de Protección", "Price":"30,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Legendary - Requires Attunement"},
  {"Name":"Cimitarra de Velocidad", "Price":"5,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Maravilloso", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Escudo del Centinela", "Price":"800 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Uncommon - Requires Attunement"},
  {"Name":"Escudo de Atracción de Proyectiles", "Price":"1,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Rare - Requires Attunement"},
  {"Name":"Escudo Guardador de Hechizos", "Price":"15,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Armadura", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Bastón de Encantamiento", "Price":"550 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate -Staff", "Properties":"Rare - Requires Attunement"},
  {"Name":"Bastón de Fuego", "Price":"15,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate -Staff", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Bastón de Escarcha", "Price":"20,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate -Staff", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Bastón de Curación", "Price":"3,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate -Staff", "Properties":"Rare - Requires Attunement"},
  {"Name":"Bastón de Poder", "Price":"60,500 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate -Staff", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Bastón de Golpe", "Price":"10,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate -Staff", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Bastón de Insectos Enjambre", "Price":"2,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate -Staff", "Properties":"Rare - Requires Attunement"},
  {"Name":"Bastón de la Víbora", "Price":"200 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate -Staff", "Properties":"Uncommon - Requires Attunement"},
  {"Name":"Bastón del Bosque", "Price":"2,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate -Staff", "Properties":"Rare - Requires Attunement"},
  {"Name":"Bastón de Truenos y Relámpagos", "Price":"4,500 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate -Staff", "Properties":"Very Rare - Requires Attunement"},
  {"Name":"Bastón de Marchitamiento", "Price":"800 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate -Staff", "Properties":"Rare - Requires Attunement"},
  {"Name":"Espada Solar", "Price":"5,000 gp", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Magico - Combate - Arma", "Properties":"Rare - Requires Attunement"}
]
dnd_items_part_9 = [
    {"Name":"Espada de la Respuesta", "Price":"30,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Arma", "Properties":"Legendaria - Requiere Afinidad"},
    {"Name":"Espada Robavidas", "Price":"1,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Arma", "Properties":"Rara - Requiere Afinidad"},
    {"Name":"Espada Afilada", "Price":"1,200 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Arma", "Properties":"Rara - Requiere Afinidad"},
    {"Name":"Espada de Heridas", "Price":"2,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Arma", "Properties":"Rara - Requiere Afinidad"},
    {"Name":"Vara de Tentáculos", "Price":"20,500 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Vara", "Properties":"Rara - Requiere Afinidad"},
    {"Name":"Arma Viciosa", "Price":"1,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Arma", "Properties":"Rara"},
    {"Name":"Espada Vorpal", "Price":"20,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Arma", "Properties":"Legendaria - Requiere Afinidad"},
    {"Name":"Varita de Vinculación", "Price":"4,500 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Varita", "Properties":"Rara - Requiere Afinidad"},
    {"Name":"Varita de Detección de Enemigos", "Price":"3,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Varita", "Properties":"Rara"},
    {"Name":"Varita del Miedo", "Price":"2,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Varita", "Properties":"Rara - Requiere Afinidad"},
    {"Name":"Varita de Bolas de Fuego", "Price":"5,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Varita", "Properties":"Rara - Requiere Afinidad"},
    {"Name":"Varita de Rayos", "Price":"3,500 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Varita", "Properties":"Rara - Requiere Afinidad"},
    {"Name":"Varita de Misiles Mágicos", "Price":"1,500 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Varita", "Properties":"Poco Común"},
    {"Name":"Varita de Parálisis", "Price":"5,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Varita", "Properties":"Rara - Requiere Afinidad"},
    {"Name":"Varita de Polimorfia", "Price":"20,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Varita", "Properties":"Muy Rara - Requiere Afinidad"},
    {"Name":"Varita del Mago de Guerra +1", "Price":"700 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Varita", "Properties":"Poco Común - Requiere Afinidad"},
    {"Name":"Varita del Mago de Guerra +2", "Price":"2,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Varita", "Properties":"Rara - Requiere Afinidad"},
    {"Name":"Varita del Mago de Guerra +3", "Price":"8,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Varita", "Properties":"Muy Rara - Requiere Afinidad"},
    {"Name":"Varita de Telaraña", "Price":"2,000 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Varita", "Properties":"Poco Común - Requiere Afinidad"},
    {"Name":"Arma de Advertencia", "Price":"400 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Arma", "Properties":"Poco Común - Requiere Afinidad"},
    {"Name":"Abanico de Viento", "Price":"300 po", "AC":"null", "Damage":"null", "Weight":"null", "Type":"Mágico - Combate - Maravilloso", "Properties":"Poco Común"},
    {"Name":"Suministros de Alquimista", "Price":"50 po", "AC":"null", "Damage":"null", "Weight":"8 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Suministros de Cervecero", "Price":"20 po", "AC":"null", "Damage":"null", "Weight":"9 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Suministros de Calígrafo", "Price":"10 po", "AC":"null", "Damage":"null", "Weight":"5 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Suministros de Pintor", "Price":"10 po", "AC":"null", "Damage":"null", "Weight":"5 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Herramientas de Cartógrafo", "Price":"15 po", "AC":"null", "Damage":"null", "Weight":"6 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Herramientas de Zapatero", "Price":"5 po", "AC":"null", "Damage":"null", "Weight":"5 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Utensilios de Cocinero", "Price":"1 po", "AC":"null", "Damage":"null", "Weight":"8 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Herramientas de Soplador de Vidrio", "Price":"30 po", "AC":"null", "Damage":"null", "Weight":"5 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Herramientas de Joyero", "Price":"25 po", "AC":"null", "Damage":"null", "Weight":"2 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Herramientas de Curtidor", "Price":"5 po", "AC":"null", "Damage":"null", "Weight":"5 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Herramientas de Albañil", "Price":"10 po", "AC":"null", "Damage":"null", "Weight":"8 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Herramientas de Carpintero", "Price":"8 po", "AC":"null", "Damage":"null", "Weight":"6 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Herramientas de Alfarero", "Price":"10 po", "AC":"null", "Damage":"null", "Weight":"3 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},
    {"Name":"Herramientas de Herrero", "Price":"20 po", "AC":"null", "Damage":"null", "Weight":"8 lb.", "Type":"Herramientas de Artesano", "Properties":"null"},

    {"Name":"Herramientas de hojalatero", "Price":"50 po", "AC":"null", "Damage":"null", "Weight":"10 lb.", "Type":"Herramientas de artesano", "Properties":"null"},
    {"Name":"Herramientas de tejedor", "Price":"1 po", "AC":"null", "Damage":"null", "Weight":"5 lb.", "Type":"Herramientas de artesano", "Properties":"null"},
    {"Name":"Herramientas de navegante", "Price":"25 po", "AC":"null", "Damage":"null", "Weight":"2 lb.", "Type":"Herramientas de artesano", "Properties":"null"},
    {"Name":"Herramientas de carpintero", "Price":"1 po", "AC":"null", "Damage":"null", "Weight":"5 lb.", "Type":"Herramientas de artesano", "Properties":"null"},
    {"Name":"Herramientas de ladrón", "Price":"25 po", "AC":"null", "Damage":"null", "Weight":"1 lb.", "Type":"Herramientas de artesano", "Properties":"null"},
    {"Name":"Kit de venenos", "Price":"50 po", "AC":"null", "Damage":"null", "Weight":"2 lb.", "Type":"Herramientas de artesano", "Properties":"null"},
    {"Name":"Kit de herboristería", "Price":"5 po", "AC":"null", "Damage":"null", "Weight":"3 lb.", "Type":"Herramientas de artesano", "Properties":"null"},
    {"Name":"Kit de Disfraz", "Price":"25 po", "AC":"null", "Damage":"null", "Weight":"3 lb.", "Type":"Herramientas de artesano", "Properties":"null"},
    {"Name":"Kit de falsificación", "Price":"15 po", "AC":"null", "Damage":"null", "Weight":"5 lb.", "Type":"Herramientas de artesano", "Properties":"null"},
    {"Name":"Juego de dados", "Price":"1 pl", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Juegos de azar", "Properties":"null"},
    {"Name":"Juego de Ajedrez Dracónico", "Price":"1 po", "AC":"null", "Damage":"null", "Weight":"0.5 lb.", "Type":"Juegos de azar", "Properties":"null"},
    {"Name":"Juego de cartas", "Price":"5 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Juegos de azar", "Properties":"null"},
    {"Name":"Juego de Three-Dragon Ante", "Price":"1 po", "AC":"null", "Damage":"null", "Weight":"-", "Type":"Juegos de azar", "Properties":"null"},
    {"Name":"Gaita", "Price":"30 po", "AC":"null", "Damage":"null", "Weight":"6 lb.", "Type":"Instrumento musical", "Properties":"null"},
    {"Name":"Tambor", "Price":"6 po", "AC":"null", "Damage":"null", "Weight":"3 lb.", "Type":"Instrumento musical", "Properties":"null"},
    {"Name":"Dulcimer", "Price":"25 po", "AC":"null", "Damage":"null", "Weight":"10 lb.", "Type":"Instrumento musical", "Properties":"null"},
    {"Name":"Flauta", "Price":"2 po", "AC":"null", "Damage":"null", "Weight":"1 lb.", "Type":"Instrumento musical", "Properties":"null"},
    {"Name":"Laúd", "Price":"35 po", "AC":"null", "Damage":"null", "Weight":"2 lb.", "Type":"Instrumento musical", "Properties":"null"},
    {"Name":"Lira", "Price":"30 po", "AC":"null", "Damage":"null", "Weight":"2 lb.", "Type":"Instrumento musical", "Properties":"null"},
    {"Name":"Cuerno", "Price":"3 po", "AC":"null", "Damage":"null", "Weight":"2 lb.", "Type":"Instrumento musical", "Properties":"null"},
    {"Name":"Flauta de Pan", "Price":"12 po", "AC":"null", "Damage":"null", "Weight":"2 lb.", "Type":"Instrumento musical", "Properties":"null"},
    {"Name":"Chirimía", "Price":"2 po", "AC":"null", "Damage":"null", "Weight":"1 lb.", "Type":"Instrumento musical", "Properties":"null"},
    {"Name":"Viola", "Price":"30 po", "AC":"null", "Damage":"null", "Weight":"1 lb.", "Type":"Instrumento musical", "Properties":"null"},
]
dnd_items_part_10 = [
  {"Name": "Katana", "Price": "50 po", "AC": "null", "Damage": "1d10", "Weight": 6, "Type": "Arma exótica (corte)", "Properties": "Crítico 18-20/x2, puede usarse a una mano con la dote apropiada"},
  {"Name": "Wakizashi", "Price": "35 po", "AC": "null", "Damage": "1d6", "Weight": 2, "Type": "Arma exótica (corte)", "Properties": "Crítico 19-20/x2, ligera"},
  {"Name": "Naginata", "Price": "60 po", "AC": "null", "Damage": "1d10", "Weight": 8, "Type": "Arma exótica (corte)", "Properties": "Alcance, Crítico x4"},
  {"Name": "Kama", "Price": "2 po", "AC": "null", "Damage": "1d6", "Weight": 2, "Type": "Arma exótica (corte)", "Properties": "Ligera, puede usarse con Flurry of Blows"},
  {"Name": "Kusarigama", "Price": "12 po", "AC": "null", "Damage": "1d6/1d4", "Weight": 3, "Type": "Arma exótica doble", "Properties": "Una parte cortante, otra con cadena; posibilidad de desarme"},
  {"Name": "Tetsubo", "Price": "15 po", "AC": "null", "Damage": "2d6", "Weight": 12, "Type": "Arma exótica (contundente)", "Properties": "Crítico x3"},
  {"Name": "Shuriken (5 unidades)", "Price": "1 po", "AC": "null", "Damage": "1d2", "Weight": 0.5, "Type": "Arma arrojadiza (perforante)", "Properties": "Ligera, alcance 10 pies, se considera munición"},
  {"Name": "Tessen (abanico de guerra)", "Price": "5 po", "AC": 1, "Damage": "1d4", "Weight": 1, "Type": "Escudo ligero/arma improvisada", "Properties": "Puede ocultarse fácilmente, bonificador de escudo"},
  {"Name": "Escudo de bambú", "Price": 3, "AC": "1 po", "Damage": "null", "Weight": 4, "Type": "Escudo ligero", "Properties": "Hecho de materiales naturales, no metálico"},
  {"Name": "Escudo de acero oriental", "Price": "20 po", "AC": 2, "Damage": "null", "Weight": 6, "Type": "Escudo pesado", "Properties": "Puede mejorarse mágicamente, más estilizado"},
  {"Name": "Escudo de Fuerza (+3)", "Price": "6000 po", "AC": 3, "Damage": "null", "Weight": 6, "Type": "Escudo mágico", "Properties": "Requiere Fuerza 15 o superior"},
  {"Name": "Escudo de Poder (+4)", "Price": "12000 po", "AC": 4, "Damage": "null", "Weight": 8, "Type": "Escudo mágico", "Properties": "Requiere Fuerza 18 o superior"},
  {"Name": "Broquel", "Price": "5 po", "AC": 1, "Damage": "null", "Weight": 8, "Type": "Escudo", "Properties": "Ligero, puede usarse con una mano, no penaliza a la Destreza"},

  {"Name": "Pistola (Pistol)", "Price": "250 po", "AC": "null", "Damage": "1d10", "Weight": 3, "Type": "Arma de Fuego (a distancia)", "Properties": "Alcance 30/90, recarga, una mano"},
  {"Name": "Mosquete (Musket)", "Price": "500 po", "AC": "null", "Damage": "1d12", "Weight": 10, "Type": "Arma de Fuego (a distancia)", "Properties": "Alcance 40/120, recarga, dos manos"},
  {"Name": "Arquebus (Arquebus)", "Price": "400 po", "AC": "null", "Damage": "2d6", "Weight": 10, "Type": "Arma de Fuego (a distancia)", "Properties": "Alcance 60/180, recarga, dos manos, humo"},
  {"Name": "Escopeta (Scattergun)", "Price": "600 po", "AC": "null", "Damage": "2d8", "Weight": 8, "Type": "Arma de Fuego (a distancia)", "Properties": "Cono de 15 pies, recarga, dos manos"},
  {"Name": "Pistola de repetición (Repeating Pistol)", "Price": "750 po", "AC": "null", "Damage": "1d10", "Weight": 4, "Type": "Arma de Fuego (a distancia)", "Properties": "Alcance 30/90, recarga (6 tiros), una mano"},
  {"Name": "Mosquete de repetición (Repeating Musket)", "Price": "1000 po", "AC": "null", "Damage": "1d12", "Weight": 11, "Type": "Arma de Fuego (a distancia)", "Properties": "Alcance 40/120, recarga (6 tiros), dos manos"},
  {"Name": "Trabuco", "Price": "500 po", "AC": "null", "Damage": "2d8", "Weight": 10, "Type": "Arma de Fuego (a distancia)", "Properties": "Cono de 15 pies, recarga, dos manos, dispersión"},
]
# Pociones
pociones_1 = [
    {"Name": "Poción de Curación", "Price": "50 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Restaura 2d4+2 HP"},
    {"Name": "Poción de Curación Mayor", "Price": "150 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Restaura 4d4+4 HP"},
    {"Name": "Poción de Curación Superior", "Price": "450 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Restaura 8d4+8 HP"},
    {"Name": "Poción de Curación Suprema", "Price": "1350 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Restaura 10d4+20 HP"},
    {"Name": "Poción de Escalada", "Price": "180 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Ventaja en pruebas de Atletismo, velocidad de escalada igual a caminata por 1h"},
    {"Name": "Poción de Invisibilidad", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Invisibilidad por 1 hora o hasta atacar o lanzar hechizo"},
    {"Name": "Poción de Velocidad", "Price": "400 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Efecto del conjuro Celeridad por 1 minuto"},
    {"Name": "Poción de Vuelo", "Price": "500 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Vuelo por 1h, velocidad 60 pies"},
    {"Name": "Poción de Resistencia al Fuego", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Resistencia al daño de fuego por 1 hora"},
    {"Name": "Poción de Resistencia al Frío", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Resistencia al daño de frío por 1 hora"},
    {"Name": "Poción de Resistencia al Rayo", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Resistencia al daño eléctrico por 1 hora"},
    {"Name": "Poción de Resistencia al Ácido", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Resistencia al daño de ácido por 1 hora"},
    {"Name": "Poción de Resistencia al Veneno", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Resistencia al daño por veneno por 1 hora"},
    {"Name": "Poción de Resistencia Psíquica", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Resistencia al daño psíquico por 1 hora"},
    {"Name": "Poción de Resistencia Necrótica", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Resistencia al daño necrótico por 1 hora"},
    {"Name": "Poción de Resistencia Radiante", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Resistencia al daño radiante por 1 hora"},
    {"Name": "Poción de Resistencia Tónica", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Resistencia al daño sónico por 1 hora"},
    {"Name": "Poción de Respirar Bajo el Agua", "Price": "180 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Respirar bajo el agua por 1 hora"},
    {"Name": "Poción de Heroísmo", "Price": "400 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "10 HP temporales y efecto de Bendecir por 1h"},
    {"Name": "Poción de Vitalidad", "Price": "800 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Cura enfermedades y venenos, restaura todos los dados de golpe"},
    {"Name": "Poción de Amistad con los Animales", "Price": "125 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Efecto del conjuro Amistad con los Animales por 1 hora"},
    {"Name": "Poción de Disminución", "Price": "270 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Reduce tamaño a la mitad por 1 minuto"},
    {"Name": "Poción de Agrandamiento", "Price": "270 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Duplica tamaño y fuerza, ventaja en pruebas de FU por 1 minuto"},
    {"Name": "Poción de Forma Gaseosa", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Transforma al usuario en forma gaseosa por 1 hora"},
    {"Name": "Poción de Lectura Mental", "Price": "400 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Detecta pensamientos (como el conjuro) por 1 minuto"},
    {"Name": "Poción de Invulnerabilidad", "Price": "500 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Resistencia a todo daño por 1 minuto"},
    {"Name": "Poción de Fuerza de Gigante de Tormenta", "Price": "5000 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "FU se convierte en 29 por 1 hora"},
    {"Name": "Poción de Fuerza de Gigante de la Colina", "Price": "250 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "FU se convierte en 21 por 1 hora"},
    {"Name": "Poción de Fuerza de Gigante de Escarcha", "Price": "500 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "FU se convierte en 23 por 1 hora"},
    {"Name": "Poción de Fuerza de Gigante de Fuego", "Price": "1000 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "FU se convierte en 25 por 1 hora"},
    {"Name": "Poción de Fuerza de Gigante de Nubes", "Price": "3000 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "FU se convierte en 27 por 1 hora"},
    {"Name": "Poción de Fuerza de Gigante de Piedra", "Price": "1500 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "FU se convierte en 23 por 1 hora"},
    {"Name": "Aceite de Resbaladicidad", "Price": "250 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Efecto de Libertad de Movimiento por 8 horas"},
    {"Name": "Elixir de Salud", "Price": "500 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Cura ceguera, sordera, enfermedades, venenos y restaura HP"},
    {"Name": "Elixir de Resiliencia", "Price": "350 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Ventaja en tiradas de salvación de Constitución por 1 hora"},
    {"Name": "Elixir de Visión en la Oscuridad", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Otorga visión en la oscuridad 60 pies por 1h"},
    {"Name": "Elixir de Rapidez", "Price": "350 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Velocidad +10 pies por 1h"},
    {"Name": "Elixir de Valentía", "Price": "300 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "+1d4 a tiradas de ataque y salvaciones por 1 minuto"},
    {"Name": "Elixir de Vida", "Price": "1200 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Cura 2d4+2 y elimina enfermedades y venenos"},
    {"Name": "Poción de Claridad", "Price": "150 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Ventaja en salvaciones de INT, SAB y CAR por 1h"},
    {"Name": "Poción de Perspicacia", "Price": "200 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Ventaja en pruebas de Sabiduría (Perspicacia) por 1 hora"},
    {"Name": "Poción de Suerte", "Price": "600 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Permite repetir una tirada de ataque, habilidad o salvación"},
    {"Name": "Poción de Visión Verdadera", "Price": "2500 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Efecto del conjuro Visión Verdadera por 1 hora"},
    {"Name": "Poción de Eterealidad", "Price": "3000 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Accede al Plano Etéreo por 1 hora"},
    {"Name": "Poción de Comprensión", "Price": "150 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Efecto de Comprender Idiomas por 1 hora"},
    {"Name": "Poción de Lenguas", "Price": "500 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Entiende y habla cualquier idioma por 1 hora"},
    {"Name": "Poción de Ceguera", "Price": "150 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Induce ceguera durante 1 minuto (uso ofensivo)"},
    {"Name": "Poción de Sueño", "Price": "100 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Actúa como el conjuro Sueño en un área cercana"},
    {"Name": "Poción de Aliento de Fuego", "Price": "150 po", "AC": "", "Damage": "4d6", "Weight": "0.5", "Type": "Poción", "Properties": "Permite exhalar fuego 3 veces por 1h (cono de 15 pies)"},
    {"Name": "Poción de Veneno", "Price": "100 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Parece curativa, pero causa 3d6 veneno, salvación CON la reduce a la mitad"},
    {"Name": "Filtro de Amor", "Price": "90 po", "AC": "", "Damage": "", "Weight": "0.5", "Type": "Poción", "Properties": "Provoca enamoramiento mágico bajo efecto de encantamiento"},

    {"Name": "Fuego Alquímico", "Price": "50 po", "AC": "", "Damage": "1d4 por turno", "Weight": "0.5", "Type": "Consumible, Arrojadizo", "Properties": "Sufre daño de fuego al inicio de cada turno hasta gastar una acción para apagarlo"},
]



# Insertar los datos en la base de datos
def insert_items(items_list):
    for item in items_list:
        # Unificar claves posibles
        name = item.get("Name", "")
        price = item.get("Price", "")
        ac = item.get("AC", item.get("CA", ""))
        damage = item.get("Damage", "")
        weight = item.get("Weight", item.get("Peso", item.get("weight", "")))
        type_ = item.get("Type", "")
        properties = item.get("Properties", "")
        img = item.get("img", "")

        new_item = Items(
            Name=name,
            Price=price,
            AC=ac,
            Damage=damage,
            Weight=weight,
            Type=type_,
            Properties=properties,
            img=img
        )
        session.add(new_item)
        print(f"✅ Insertado: {name}")

try:
    # Insertar todos los items de todas las listas
    for i in range(1, 11):
        insert_items(eval(f"dnd_items_part_{i}"))
        session.commit()
        print(f"\n\033[92m✅ Todos los items de la parte {i} han sido insertados correctamente.\033[0m\n")

    # session.commit()
    print("✅ Todos los items han sido insertados correctamente.")

    # Insertar todas las pociones de todas las listas
    for i in range(1, 1):
        insert_items(eval(f"pociones_{i}"))
        session.commit()
        print(f"\n\033[92m✅ Todas las pociones de la parte {i} han sido insertados correctamente.\033[0m\n")

    # session.commit()
    print("✅ Todas las pociones han sido insertados correctamente.")

except Exception as e:
    print("❌ Ocurrió un error durante el procesamiento:")
    print(e)

finally:
    session.close()
    connection.close()
    print("🔒 Conexión cerrada.")
