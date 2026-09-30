'''Validador de datos de usuarios

Tenemos esta lista:

usuarios = [
    {"nombre": "Ana", "edad": 25, "activo": True},
    {"nombre": "Pedro", "edad": 17, "activo": True},
    {"nombre": "Laura", "edad": 31, "activo": False},
    {"nombre": "Carlos", "edad": 22, "activo": True},
]

Crea:

def validar_usuarios(usuarios):

Debes recorrer la lista con for.

Un usuario será válido si:

tiene 18 años o más
está activo

Para cada usuario debes mostrar:

Ana → VÁLIDO
Pedro → NO VÁLIDO
Laura → NO VÁLIDO
Carlos → VÁLIDO

Después muestra:

Usuarios válidos: 2
Usuarios no válidos: 2
🚫 Esta vez hay una restricción

No puedes utilizar:

count()

Tienes que utilizar contadores + for + if.

Este ejercicio ya se parece bastante más a la lógica que vas a utilizar posteriormente para validar datos en tests automatizados.'''
usuarios = [
    {"nombre": "Ana", "edad": 25, "activo": True},
    {"nombre": "Pedro", "edad": 17, "activo": True},
    {"nombre": "Laura", "edad": 31, "activo": False},
    {"nombre": "Carlos", "edad": 22, "activo": True},
]

def validar_usuarios(usuarios):
    validos = 0
    no_validos = 0

    for usuario in usuarios:
        if usuario["edad"] >= 18 and usuario["activo"] is True:
            print(f"{usuario['nombre']} → VÁLIDO")
            validos += 1
        else:
            print(f"{usuario['nombre']} → NO VÁLIDO")
            no_validos += 1

    print(f"Usuarios válidos: {validos}")
    print(f"Usuarios no válidos: {no_validos}")

validar_usuarios(usuarios)


    