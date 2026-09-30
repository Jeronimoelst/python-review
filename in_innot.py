'''in / not in

Tienes una lista de roles permitidos:

["admin", "tester", "developer", "manager"]

Crea una variable:

rol_usuario

El programa debe comprobar si ese rol está permitido.

Después prueba:

tester
cliente
admin

La comprobación debe realizarse utilizando un operador de pertenencia.'''




roles_permitidos = ["admin", "tester", "developer", "manager"]

for rol_usuario in ["tester", "cliente", "admin"]:
    if rol_usuario in roles_permitidos:
        print(f"El rol '{rol_usuario}' está permitido.")
    else:
        print(f"El rol '{rol_usuario}' NO está permitido.")