import bcrypt
import socket
import json
from sqlalchemy.orm import Session
from db.modelos import Usuario

def validar_usuario(rut, contrasena, session: Session):
    # Buscar el usuario por rut
    usuario = session.query(Usuario).filter(Usuario.rut == rut).first()
    
    if usuario:
        # Verificar la contraseña hasheada
        if bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena.encode('utf-8')):
            return usuario.to_dict_private()
        
    return None

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
            contenido = data[11:]
            print('Operation:', operacion)
            print('Content:', contenido)

            if operacion == "LSTUSR":
                respuesta = listar_usuarios()
               
            elif operacion == "UPDUSR":
                respuesta = actualizar_usuario(contenido)
            elif operacion == "DELUSR":
                respuesta = eliminar_usuario(contenido)
            else:
                respuesta = b'Operacion no soportada'
            
            response_length = str(len(respuesta) + 10).zfill(5).encode()
            message = response_length + serv_id.encode() + respuesta
            print('sending {!r}'.format(message))
            sock.sendall(message)

finally:
    print('closing socket')
    sock.close()
