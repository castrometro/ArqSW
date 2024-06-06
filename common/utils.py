import json



def autenticacion_usuarios(sock):
    serv_id = 'serv2'
    message = 'Funcionalidad en desarrollo'
    return message



def gestion_usuarios(sock):
    serv_id = 'serv1'
    while True:
        # Menú de opciones para Gestión de Usuarios
        print("\nSeleccione una operación de Gestión de Usuarios:")
        print("1. Listar usuarios")
        print("2. Actualizar usuario")
        print("3. Eliminar usuario")
        print("4. Volver al menú principal")
        
        opcion = input("Ingrese el número de la operación: ")
        
        if opcion == '1':
            # Enviar solicitud para listar usuarios
            message = b'00015' + serv_id.encode() + b'LSTUSR'
            print('sending {!r}'.format(message))
            sock.sendall(message)

            # Esperar la respuesta
            amount_received = 0
            amount_expected = int(sock.recv(5))

            data = b''
            while amount_received < amount_expected:
                chunk = sock.recv(amount_expected - amount_received)
                data += chunk
                amount_received += len(chunk)
            
            # Procesar la respuesta
            print("Lista de usuarios:")
            print(json.loads(data[7:].decode()))

        elif opcion == '2':
            # Solicitar datos del usuario a actualizar
            user_id = input("Ingrese el ID del usuario a actualizar: ")
            user_name = input("Ingrese el nuevo nombre del usuario: ")
            user_email = input("Ingrese el nuevo email del usuario: ")
            
            user_data = json.dumps({"id": int(user_id), "nombre": user_name, "email": user_email}).encode()
            data_length = str(len(user_data) + 15).zfill(5).encode()
            message = data_length + serv_id.encode() + b'UPDUSR' + user_data
            print('sending {!r}'.format(message))
            sock.sendall(message)

            # Esperar la respuesta
            amount_received = 0
            amount_expected = int(sock.recv(5))

            data = b''
            while amount_received < amount_expected:
                chunk = sock.recv(amount_expected - amount_received)
                data += chunk
                amount_received += len(chunk)
            
            # Procesar la respuesta
            print("Respuesta del servicio:")
            print(data[7:].decode())

        elif opcion == '3':
            # Solicitar ID del usuario a eliminar
            user_id = input("Ingrese el ID del usuario a eliminar: ")
            data_length = str(len(user_id) + 15).zfill(5).encode()
            message = data_length + serv_id.encode() + b'DELUSR' + user_id.encode()
            print('sending {!r}'.format(message))
            sock.sendall(message)

            # Esperar la respuesta
            amount_received = 0
            amount_expected = int(sock.recv(5))

            data = b''
            while amount_received < amount_expected:
                chunk = sock.recv(amount_expected - amount_received)
                data += chunk
                amount_received += len(chunk)
            
            # Procesar la respuesta
            print("Respuesta del servicio:")
            print(data[7:].decode())

        elif opcion == '4':
            # Volver al menú principal
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")