import socket
import sys

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto donde el bus está escuchando
bus_address = ('localhost', 5000)
print('connecting to {} port {}'.format(*bus_address))
sock.connect(bus_address)

try:
    while True:
        # Enviar "Hello world" al servicio
        if input('Send Hello world to servi? y/n: ') != 'y':
            break
        message = b'00016serv1Hello world'
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # Esperar la respuesta
        print("Waiting for transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))

        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
        print("Checking servi answer ...")
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()