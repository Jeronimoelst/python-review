'''Reto final — mezcla de todo

Este es el que quiero que hagas sin mirar nada de lo anterior si puedes.

Estás creando una pequeña validación para una aplicación de QA.

Tienes un usuario:

nombre
edad
email
rol
activo

Y una lista de roles permitidos:

["admin", "tester", "developer"]

El usuario será considerado válido solamente si:

tiene al menos 18 años;
tiene email;
está activo;
su rol está dentro de los roles permitidos.

El programa debe generar un resultado indicando:

Usuario válido

o:

Usuario no válido
Pero añade una dificultad:

En lugar de limitarte a decir si es válido o no, haz que el programa pueda identificar por qué no es válido.

Por ejemplo:

Usuario no válido
Motivo: cuenta inactiva

o:

Usuario no válido
Motivo: rol no permitido

Si tiene varios problemas, debería poder indicarlos.

🎯 Orden que te recomiendo

No hagas los 15 de golpe.

Haz hoy:

1 → 2 → 3 → 4 → 5 → 8 → 9 → 11 → 15

Los demás puedes utilizarlos como refuerzo.

Y una regla importante: primero intenta resolverlos sin buscar la solución en Internet. Si te atascas, mándame tu código aunque esté incompleto. Te diré qué está bien, dónde está el error y qué concepto necesitas revisar, pero sin darte directamente la solución, para que realmente desarrolles el razonamiento.'''

def usuario():
    nombre = str(input('Escribe el nombre '))
    edad = int(input('escribe la edad '))
    email = input('Escribe tu email ')
    rol = str(input('escribe tu rol '))
    activo = input("Escribe tu estado (True/False): ").strip().lower() == "true"

    roles_permitidos = ["admin", "tester", "developer"]


    if edad >= 18 and activo and rol in roles_permitidos and email != "":
        print("Usuario válido")
    else:
        print("Usuario no válido")

    usuario_no_valido = 0

    if edad < 18:
        print("Menor de edad")
        usuario_no_valido += 1

    if email == "":
        print("Falta el email")
        usuario_no_valido += 1

    if rol not in roles_permitidos:
        print("Rol no permitido")
        usuario_no_valido += 1

    if not activo:
        print("Usuario inactivo")
        usuario_no_valido += 1
    if usuario_no_valido == 0:
        print("Usuario válido")
    else:
        print("Usuario no válido")
    

usuario()




    

