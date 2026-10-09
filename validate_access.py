
nombre = input('Nombre de usuario: ').strip().lower()
edad = int(input('Edad: '))
activo = input('Cuenta activa (true o false): ').strip().lower() == 'true'
rol = input('Rol (admin, tester o developer): ').strip().lower()
identificado = input('Usuario identificado (true o false): ').strip().lower() == 'true'


def datos_usuario(nombre, edad, activo, rol, identificado):

    if nombre == '':
        print('Acceso denegado: nombre vacío')

    elif edad < 18:
        print('Acceso denegado: edad insuficiente')

    elif not activo:
        print('Acceso denegado: cuenta inactiva')

    elif not identificado:
        print('Acceso denegado: usuario no identificado')

    elif rol in ['admin', 'tester']:
        print('Acceso permitido')

    elif rol == 'developer':
        print('Acceso denegado: rol sin permisos para pruebas')

    else:
        print('Acceso denegado: rol inválido')


datos_usuario(nombre, edad, activo, rol, identificado)