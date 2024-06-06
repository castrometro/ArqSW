from modelos import Foro, get_session

def create_foro(id_comunidad, id_usuario, tipo_foro, estado_foro, tema_foro):
    session = get_session()
    try:
        nuevo_foro = Foro(
            id_comunidad=id_comunidad,
            id_usuario=id_usuario,
            tipo_foro=tipo_foro,
            estado_foro=estado_foro,
            tema_foro=tema_foro
        )
        session.add(nuevo_foro)
        session.commit()
        return nuevo_foro
    finally:
        session.close()