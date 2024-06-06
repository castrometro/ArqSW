import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.modelos import Comunidad, get_session


def create_comunidad(nombre_comunidad):
    session = get_session()
    try:
        comunidad = Comunidad(nombre_comunidad=nombre_comunidad)
        session.add(comunidad)
        session.commit()
        return comunidad
    finally:
        session.close()
def get_comunidad(id_comunidad):
    session = get_session()
    try:
        comunidad = session.query(Comunidad).filter(Comunidad.id_comunidad == id_comunidad).one()
        return comunidad
    finally:
        session.close()
def get_comunidades():
    session = get_session()
    try:
        comunidades = session.query(Comunidad).all()
        return comunidades
    finally:
        session.close()
def get_comunidad_by_nombre(nombre_comunidad):
    session = get_session()
    try:
        comunidad = session.query(Comunidad).filter(Comunidad.nombre_comunidad == nombre_comunidad).one()
        return comunidad
    finally:
        session.close()
def delete_comunidad(id_comunidad):
    session = get_session()
    try:
        comunidad = session.query(Comunidad).filter(Comunidad.id_comunidad == id_comunidad).one()
        session.delete(comunidad)
        session.commit()
        return comunidad
    finally:
        session.close()
def update_comunidad(id_comunidad, nombre_comunidad):
    session = get_session()
    try:
        comunidad = session.query(Comunidad).filter(Comunidad.id_comunidad == id_comunidad).one()
        comunidad.nombre_comunidad = nombre_comunidad
        session.commit()
        return comunidad
    finally:
        session.close()