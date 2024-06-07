from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Departamento(Base):
    __tablename__ = 'departamento'
    id_departamento = Column(Integer, primary_key=True)
    id_comunidad = Column(Integer, ForeignKey('comunidad.id_comunidad'))
    numero = Column(String(50))
    id_usuario_propietario = Column(Integer, ForeignKey('usuario.id_usuario'))
    
    def to_dict(self):
        return {
            'id_departamento': self.id_departamento,
            'id_comunidad': self.id_comunidad,
            'numero': self.numero,
            'id_usuario_propietario': self.id_usuario_propietario
        }
    
class Comunidad(Base):
    __tablename__ = 'comunidad'
    id_comunidad = Column(Integer, primary_key=True)
    nombre_comunidad = Column(String(50))

    def to_dict(self):
        return {
            'id_comunidad': self.id_comunidad,
            'nombre_comunidad': self.nombre_comunidad
        }

class Usuario_Departamento(Base):
    __tablename__ = 'usuario_departamento'
    id_usuario_departamento = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_departamento = Column(Integer, ForeignKey('departamento.id_departamento'))
    
    def to_dict(self):
        return {
            'id_usuario_departamento': self.id_usuario_departamento,
            'id_usuario': self.id_usuario,
            'id_departamento': self.id_departamento
        }

class Foro(Base):
    __tablename__ = 'foro'
    id_foro = Column(Integer, primary_key=True)
    id_comunidad = Column(Integer, ForeignKey('comunidad.id_comunidad'))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    tipo_foro = Column(String(50))
    estado_foro = Column(String(50))
    tema_foro = Column(String(50))
    
    def to_dict(self):
        return {
            'id_foro': self.id_foro,
            'id_comunidad': self.id_comunidad,
            'id_usuario': self.id_usuario,
            'tipo_foro': self.tipo_foro,
            'estado_foro': self.estado_foro,
            'tema_foro': self.tema_foro
        }

class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    rut = Column(String(50))
    tipo_usuario = Column(String(50))
    correo = Column(String(100))
    fono = Column(String(20))
    nombre = Column(String(50))
    apellido_paterno = Column(String(50))
    apellido_materno = Column(String(50))
    estado_cuenta = Column(String(50))
    contrasena = Column(String(50))
    def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'rut': self.rut,
            'tipo_usuario': self.tipo_usuario,
            'correo': self.correo,
            'fono': self.fono,
            'nombre': self.nombre,
            'apellido_paterno': self.apellido_paterno,
            'apellido_materno': self.apellido_materno,
            'estado_cuenta': self.estado_cuenta
        }
    def to_dict_private(self):
        return {
            'id_usuario': self.id_usuario,
            'rut': self.rut,
            'tipo_usuario': self.tipo_usuario,
            'correo': self.correo,
            'fono': self.fono,
            'nombre': self.nombre,
            'apellido_paterno': self.apellido_paterno,
            'apellido_materno': self.apellido_materno,
            'estado_cuenta': self.estado_cuenta,
            'contrasena': self.contrasena
        }

class Chat(Base):
    __tablename__ = 'chat'
    id_chat = Column(Integer, primary_key=True)
    id_usuario_remitente = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_usuario_receptor = Column(Integer, ForeignKey('usuario.id_usuario'))
    fecha_chat = Column(DateTime)
    
    def to_dict(self):
        return {
            'id_chat': self.id_chat,
            'id_usuario_remitente': self.id_usuario_remitente,
            'id_usuario_receptor': self.id_usuario_receptor,
            'fecha_chat': self.fecha_chat
        }

class ChatMensaje(Base):
    __tablename__ = 'chat_mensaje'
    id_chat_mensaje = Column(Integer, primary_key=True)
    contenido = Column(Text)
    archivo = Column(String(100))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_chat = Column(Integer, ForeignKey('chat.id_chat'))
    fecha_mensaje = Column(DateTime)
    
    def to_dict(self):
        return {
            'id_chat_mensaje': self.id_chat_mensaje,
            'contenido': self.contenido,
            'archivo': self.archivo,
            'id_usuario': self.id_usuario,
            'id_chat': self.id_chat,
            'fecha_mensaje': self.fecha_mensaje
        }

class Notificacion(Base):
    __tablename__ = 'notificacion'
    id_notificacion = Column(Integer, primary_key=True)
    fecha = Column(DateTime)
    hora = Column(DateTime)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_foro = Column(Integer, ForeignKey('foro.id_foro'))
    
    def to_dict(self):
        return {
            'id_notificacion': self.id_notificacion,
            'fecha': self.fecha,
            'hora': self.hora,
            'id_usuario': self.id_usuario,
            'id_foro': self.id_foro
        }

class UsuarioSuspendido(Base):
    __tablename__ = 'usuario_suspendido'
    id_usuario_suspendido = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_foro = Column(Integer, ForeignKey('foro.id_foro'))
    duracion = Column(Integer)
    fecha_moderacion = Column(DateTime)
    estado = Column(String(50))
    razon = Column(String(250))
    
    def to_dict(self):
        return {
            'id_usuario_suspendido': self.id_usuario_suspendido,
            'id_usuario': self.id_usuario,
            'id_foro': self.id_foro,
            'duracion': self.duracion,
            'fecha_moderacion': self.fecha_moderacion,
            'estado': self.estado,
            'razon': self.razon
        }

class ForoMensaje(Base):
    __tablename__ = 'foro_mensaje'
    id_foro_mensaje = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_foro = Column(Integer, ForeignKey('foro.id_foro'))
    fecha = Column(DateTime)
    hora = Column(DateTime)
    contenido = Column(Text)
    archivo = Column(String(100))
    estado = Column(String(50))
    
    def to_dict(self):
        return {
            'id_foro_mensaje': self.id_foro_mensaje,
            'id_usuario': self.id_usuario,
            'id_foro': self.id_foro,
            'fecha': self.fecha,
            'hora': self.hora,
            'contenido': self.contenido,
            'archivo': self.archivo,
            'estado': self.estado
        }


def get_session():
    # Configuración de la base de datos
    DATABASE_URL = 'postgresql://postgres:mysecretpassword@localhost:5432/arquitectura_servicios'
    engine = create_engine(DATABASE_URL)

    # Crear todas las tablas
    Base.metadata.create_all(engine)

    # Crear una sesión
    Session = sessionmaker(bind=engine)
    """Crea y retorna una nueva sesión."""
    return Session()

# Conexión a la base de datos
engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/arquitectura_servicios')

# Base.metadata.drop_all(engine)
# Crear todas las tablas
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()
