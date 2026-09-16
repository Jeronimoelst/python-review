'''Diccionarios

Imagina que estás almacenando los datos de un usuario de una aplicación:

nombre
edad
email
activo
numero_de_compras

Crea un diccionario con esos datos.

Después el programa debe:

Mostrar el nombre.
Comprobar si está activo.
Mostrar cuántas compras ha realizado.
Aumentar el número de compras en una unidad.
Añadir una nueva propiedad llamada premium.
Mostrar todos los datos finales.

Piensa: ¿por qué aquí es más adecuado un diccionario que una lista?
'''
min_caracteres = 10
maximo_caracteres = 50

def validar_caracteres():
    while True:
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        if min_caracteres <= len(nombre_usuario) <= maximo_caracteres:
            return nombre_usuario
        else:
            print(f"El nombre debe tener entre {min_caracteres} y {maximo_caracteres} caracteres. Inténtalo de nuevo.")

def validar_edad():
    while True:
            edad_usuario = int(input('ingrese la edad del Usuario:'))
            if edad_usuario >= 18 and edad_usuario <= 100:
                return edad_usuario
            else:
               print("debe ser mayor de edad (18). Inténtalo de nuevo.")


def datos_usuario(nombre_usuario, edad_usuario, email_usuario, actividad_usuario, compras_usauario):
    usuario = {
        'nombre': nombre_usuario,
        'edad': edad_usuario,
        'email': email_usuario,
        'activo': actividad_usuario,
        'numero_de_compras': compras_usauario
    }
    return usuario
input_nombre = validar_caracteres()
input_edad = validar_edad()
input_email = input("Ingrese el email del usuario: ")
input_activo = input("¿El usuario está activo? (True/False): ").lower() == 'true'
input_compras = int(input("Ingrese el número de compras del usuario: "))
usuario = datos_usuario(input_nombre, input_edad, input_email, input_activo, input_compras)