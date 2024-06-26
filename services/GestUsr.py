import socket
import json
from db.comunidad import get_comunidades
from db.usuarios import create_usuario, get_usuarios

# Datos del Servicio
serv_id = "serv1"
serv_name = "Gestion de Usuarios"


def crear_usuario(user_data):
    print(user_data)
    user_data = json.loads(user_data)
    create_usuario(**user_data)
    return "Ok".encode()

def listar_usuarios():
    #return json.dumps(usuarios).encode()
    #return get_usuarios()
    #print(get_comunidades())
    json_comunidades = json.dumps(get_usuarios())
    return json_comunidades.encode()

def actualizar_usuario(user_data):
    user_data = json.loads(user_data)
    for usuario in usuarios:
        if usuario["id"] == user_data["id"]:
            usuario.update(user_data)
            return b'Usuario actualizado'
    return b'Usuario no encontrado'

def eliminar_usuario(user_id):
    global usuarios
    user_id = int(user_id)
    usuarios = [usuario for usuario in usuarios if usuario["id"] != user_id]
    return b'Usuario eliminado'

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto donde el bus está escuchando
bus_address = ('localhost', 5000)
print('connecting to {} port {}'.format(*bus_address))
sock.connect(bus_address)

try:
    # Enviar datos
    message = b'00010sinit' + serv_id.encode()
    print('sending {!r}'.format(message))
    sock.sendall(message)
    sinit = 1

    while True:
        # Esperar la transacción
        print("Waiting for transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))

        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
        
        print("Processing ...")
        print('received {!r}'.format(data))

        if sinit == 1:
            sinit = 0
            print('Received sinit answer')
        else:
            # Procesar la transacción recibida
            operacion = data[5:11].decode()
            contenido = data[11:].decode()
            print('Operation:', operacion)
            print('Content:', contenido)

            if operacion == "LSTUSR":
                respuesta = listar_usuarios()
            elif operacion == "UPDUSR":
                respuesta = actualizar_usuario(contenido)
            elif operacion == "DELUSR":
                respuesta = eliminar_usuario(contenido)
            elif operacion == "NEWUSR":
                respuesta = crear_usuario(contenido)
            else:
                respuesta = b'Operacion no soportada'
            
            response_length = str(len(respuesta) + 10).zfill(5).encode()
            message = response_length + serv_id.encode() + respuesta
            print('sending {!r}'.format(message))
            message = b'00013serv1Received'
            sock.sendall(message)

finally:
    print('closing socket')
    sock.close()
