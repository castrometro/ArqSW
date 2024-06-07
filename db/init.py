from modelos import get_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import *
# from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/arquitectura_servicios')

Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

#instalar todos los modelos reqlos