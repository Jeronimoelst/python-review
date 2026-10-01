




usuarios = [
    {
        "nombre": "Ana",
        "edad": 25,
        "activo": True,
        "rol": "admin"
    },
    {
        "nombre": "Carlos",
        "edad": 17,
        "activo": True,
        "rol": "usuario"
    },
    {
        "nombre": "Laura",
        "edad": 20,
        "activo": False,
        "rol": "usuario"
    },
    {
        "nombre": "Pedro",
        "edad": 22,
        "activo": True,
        "rol": "usuario"
    }
]

'''
def validar_usuario(usuario):
    usuarios_validos = 0
    usuarios_invalidos = 0

    for usuario in usuarios:
        if usuario["activo"] == True and usuario["edad"] >= 18:
            print(f"El usuario {usuario['nombre']} es válido.")
            usuarios_validos += 1
        else:
            print(f"El usuario {usuario['nombre']} es inválido.")
            usuarios_invalidos += 1
        if usuario["rol"] == "admin":
            print(f"El usuario {usuario['nombre']} es un administrador.")

    return usuarios_validos, usuarios_invalidos

print (validar_usuario(usuarios))
'''
def validar_usuario(usuario):
    try:
        if usuario["activo"] and usuario["edad"] >= 18:
            return True
        else:
            return False

    except (TypeError, ValueError):
        return False


usuarios_validos = 0
usuarios_invalidos = 0

for usuario in usuarios:

    if validar_usuario(usuario):
        print(f"El usuario {usuario['nombre']} es válido.")
        usuarios_validos += 1
    else:
        print(f"El usuario {usuario['nombre']} es inválido.")
        usuarios_invalidos += 1

    if usuario["rol"] == "admin":
        print(f"[ADMIN] {usuario['nombre']} - Acceso especial")


print(f"\nUsuarios válidos: {usuarios_validos}")
print(f"Usuarios inválidos: {usuarios_invalidos}")