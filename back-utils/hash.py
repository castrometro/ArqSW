import bcrypt
from sqlalchemy.orm import Session

def validar_usuario(rut, contrasena, session: Session):
    # Buscar el usuario por rut
    usuario = session.query(Usuario).filter(Usuario.rut == rut).first()
    
    if usuario:
        # Verificar la contraseña hasheada
        if bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena.encode('utf-8')):
            return usuario.to_dict_private()
    
    return None
