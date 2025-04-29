from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .routes import items_router, monsters_router

app = FastAPI()


app.title = "La guarida del Dungeon Master"
app.version = "0.1.0"

# Incluir subrouters
app.include_router(items_router)
app.include_router(monsters_router)


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

@app.get("/hello_world")
def home():
    return "Hola Mundo"
