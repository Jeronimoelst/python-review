'''Booleanos

Imagina que estás realizando una validación de acceso a una aplicación.

Tienes:
usuario_correcto
password_correcta
cuenta_activa

El acceso solamente debe permitirse cuando:

el usuario sea correcto;
la contraseña sea correcta;
la cuenta esté activa.

Haz que el programa muestre:

Acceso permitido

o:

Acceso denegado

Objetivo: razonar utilizando valores booleanos.'''

usuario_correcto = "usuario123"
password_correcta = "contraseña123"
cuenta_activa = False or True
def validar_acceso():
    usuario = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    if usuario == usuario_correcto and password == password_correcta and cuenta_activa:
        return "Acceso permitido"
    else:
        return "Acceso denegado"

print(validar_acceso())
