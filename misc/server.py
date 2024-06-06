import socket
import sys


def start_service(id, name):
    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar el socket al puerto donde el bus está escuchando
    bus_address = ('localhost', 5000)
    print('connecting to {} port {}'.format(*bus_address))
    sock.connect(bus_address)
    #verificar conexion
    print("Servicio:", name, "Conectado al bus")

    try:
        # Enviar datos
        message = b'00010sinit' + (id).encode()
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
            print("Procesing ...")
            print('received {!r}'.format(data))
            if sinit == 1:
                sinit = 0
                print('Received sinit answer')
            else:
                print("Send answer")
                message = b'00013' + (id).encode() + b'Received'
                print('sending {!r}'.format(message))
                sock.sendall(message)

    finally:
        print('closing socket')
        sock.close()

id_serv = 1
# Base de datos simulada de usuarios
usuarios = [
    {"id": 1, "nombre": "Juan Pérez", "correo": "juan@example.com"},
    {"id": 2, "nombre": "María López", "correo": "maria@example.com"}
]



