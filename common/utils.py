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
        print("4. Crear usuario")
        print("5. Volver al menú principal")
        
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
            print((data.decode()))

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
            # Solicitar datos del nuevo usuario
            id_usuario = input("Ingrese el id del nuevo usuario: ")
            rut = input("Ingrese el rut del nuevo usuario: ")
            tipo_usuario = input("Ingrese el tipo del nuevo usuario: ")
            correo = input("Ingrese el email del nuevo usuario: ")
            fono = input("Ingrese el fono del nuevo usuario: ")
            nombre = input("Ingrese el nombre del nuevo usuario: ")
            apellido_paterno = input("Ingrese el ap_p del nuevo usuario: ")
            apellido_materno = input("Ingrese elap_m del nuevo usuario: ")
            estado_cuenta = input("Ingrese el estado del nuevo usuario: ")
            contrasena = input("Ingrese la contraseña del nuevo usuario: ")
            user_data = json.dumps({'id_usuario': id_usuario,
            'rut': rut,
            'tipo_usuario': tipo_usuario,
            'correo': correo,
            'fono': fono,
            'nombre': nombre,
            'apellido_paterno': apellido_paterno,
            'apellido_materno': apellido_materno,
            'estado_cuenta': estado_cuenta,
            'contrasena': contrasena}).encode()
            data_length = str(len(user_data) + 15).zfill(5).encode()
            message = data_length + serv_id.encode() + b'NEWUSR' + user_data
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

        elif opcion == '5':
            # Volver al menú principal
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")