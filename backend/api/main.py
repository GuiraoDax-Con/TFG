from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.title = "La guarida del Dungeon Master"
app.version = "0.1.0"

Base.metadata.create_all(bind=engine)

# Configurar CORS para permitir peticiones desde el frontend (Vue)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # frontend Vue por defecto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta de prueba
@app.get("/api/mensaje")
def leer_mensaje():
    return {"mensaje": "¡Hola desde FastAPI en La Guarida del DM!"}

@app.get("/")
def home():
    return "Hola Mundo"
