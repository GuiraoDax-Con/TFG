from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine,Base
from .routers import items, monsters

app = FastAPI()

Base.metadata.create_all(bind=engine)  # Crear las tablas en la base de datos

# Configurar CORS para permitir peticiones desde el frontend (Vue)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # frontend Vue por defecto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.title = "La guarida del Dungeon Master"
app.version = "0.1.0"

# Incluir subrouters
app.include_router(items.router)
app.include_router(monsters.router)




@app.get("/")
def health_check():
    return 'Todo correcto!'

