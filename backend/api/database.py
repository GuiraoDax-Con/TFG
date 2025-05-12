from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



# URL_DATABASE = 'mysql+pymysql://root:root@localhost:3306/laguarida'
URL_DATABASE = 'mysql+pymysql://dm:1235@localhost:3306/laguarida'

engine= create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()