import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.modelos import Usuario, Comunidad, get_session


def create_usuario(nombre, apellido_paterno, apellido_materno, correo, fono, tipo_usuario, estado_cuenta, contrasena, id_usuario, rut):
    session = get_session()
    try:
        usuario = Usuario(
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            correo=correo,
            fono=fono,
            tipo_usuario=tipo_usuario,
            estado_cuenta=estado_cuenta,
            contrasena=contrasena,
            rut=rut
        )
        session.add(usuario)
        session.commit()
        return usuario
    finally:
        session.close()

def get_usuario(id_usuario):
    session = get_session()
    try:
        usuario = session.query(Usuario).filter(Usuario.id_usuario == id_usuario).one()
        return usuario
    finally:
        session.close()


def get_usuarios():
    session = get_session()
    try:
        usuarios = session.query(Usuario).all()
        return [usuario.to_dict() for usuario in usuarios]
    finally:
        session.close()


# def get_comunidades():
#     session = get_session()
#     try:
#         comunidades = session.query(Comunidad).all()
#         return comunidades
#     finally:
#         session.close()

# def get_comunidad_by_nombre(nombre_comunidad):
#     session = get_session()
#     try:
#         comunidad = session.query(Comunidad).filter(Comunidad.nombre_comunidad == nombre_comunidad).one()
#         return comunidad
#     finally:
#         session.close()

# def delete_comunidad(id_comunidad):
#     session = get_session()
#     try:
#         comunidad = session.query(Comunidad).filter(Comunidad.id_comunidad == id_comunidad).one()
#         session.delete(comunidad)
#         session.commit()
#         return comunidad
#     finally:
#         session.close()
        
# def update_comunidad(id_comunidad, nombre_comunidad):
#     session = get_session()
#     try:
#         comunidad = session.query(Comunidad).filter(Comunidad.id_comunidad == id_comunidad).one()
#         comunidad.nombre_comunidad = nombre_comunidad
#         session.commit()
#         return comunidad
#     finally:
#         session.close()