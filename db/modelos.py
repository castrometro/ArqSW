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

class Comunidad(Base):
    __tablename__ = 'comunidad'
    id_comunidad = Column(Integer, primary_key=True)
    nombre_comunidad = Column(String(50))

class Foro(Base):
    __tablename__ = 'foro'
    id_foro = Column(Integer, primary_key=True)
    id_comunidad = Column(Integer, ForeignKey('comunidad.id_comunidad'))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    tipo_foro = Column(String(50))
    estado_foro = Column(String(50))
    tema_foro = Column(String(50))

class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True)
    rut = Column(String(50))
    id_departamento = Column(Integer, ForeignKey('departamento.id_departamento'))
    tipo_usuario = Column(String(50))
    id_comunidad = Column(Integer, ForeignKey('comunidad.id_comunidad'))
    correo = Column(String(100))
    fono = Column(String(20))
    nombre = Column(String(50))
    apellido_paterno = Column(String(50))
    apellido_materno = Column(String(50))
    estado_cuenta = Column(String(50))

class Chat(Base):
    __tablename__ = 'chat'
    id_chat = Column(Integer, primary_key=True)
    id_usuario_remitente = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_usuario_receptor = Column(Integer, ForeignKey('usuario.id_usuario'))
    fecha_chat = Column(DateTime)

class ChatMensaje(Base):
    __tablename__ = 'chat_mensaje'
    id_chat_mensaje = Column(Integer, primary_key=True)
    contenido = Column(Text)
    archivo = Column(String(100))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_chat = Column(Integer, ForeignKey('chat.id_chat'))
    fecha_mensaje = Column(DateTime)

class Notificacion(Base):
    __tablename__ = 'notificacion'
    id_notificacion = Column(Integer, primary_key=True)
    fecha = Column(DateTime)
    hora = Column(DateTime)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_foro = Column(Integer, ForeignKey('foro.id_foro'))

class UsuarioSuspendido(Base):
    __tablename__ = 'usuario_suspendido'
    id_usuario_suspendido = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_foro = Column(Integer, ForeignKey('foro.id_foro'))
    duracion = Column(Integer)
    fecha_moderacion = Column(DateTime)
    estado = Column(String(50))
    razon = Column(String(250))

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

def get_session():
    # Configuración de la base de datos
    DATABASE_URL = 'postgresql://finflow:finflow@localhost:5432/arquitectura_servicios'
    engine = create_engine(DATABASE_URL)

    # Crear todas las tablas
    Base.metadata.create_all(engine)

    # Crear una sesión
    Session = sessionmaker(bind=engine)
    """Crea y retorna una nueva sesión."""
    return Session()

# Conexión a la base de datos
# engine = create_engine('postgresql://finflow:finflow@localhost:5432/arquitectura_servicios')

# # Crear todas las tablas
# Base.metadata.create_all(engine)

# # Crear una sesión
# Session = sessionmaker(bind=engine)
# session = Session()
