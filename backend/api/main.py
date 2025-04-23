from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .routes import router

app = FastAPI()


app.title = "La guarida del Dungeon Master"
app.version = "0.1.0"



# Configurar CORS para permitir peticiones desde el frontend (Vue)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # frontend Vue por defecto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas de la API
app.include_router(router)

# Ruta de prueba
@app.get("/api/mensaje")
def leer_mensaje():
    return {"mensaje": "¡Hola desde FastAPI en La Guarida del DM!"}

@app.get("/")
def home():
    return "Hola Mundo"
