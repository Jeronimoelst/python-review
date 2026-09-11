'''Crea un pequeño programa para generar automáticamente un identificador de usuario.

Datos:

nombre
apellido
año de nacimiento

El programa debe generar un identificador combinando esos datos.

Por ejemplo, si los datos fueran:

Carlos
García
1998

debería producir algo parecido a:

carlos.garcia1998

Condiciones:

No escribas el identificador manualmente.
Utiliza las variables.
El resultado debe estar en minúsculas.
Debes eliminar los espacios innecesarios.'''

def datos():
    nombre = input('introduce tu nombre: ') .strip() .lower()
    apellido = input('introduce tu apellido: ') .strip() .lower() 
    fecha_nacimiento = input ('introduce tu fecha de nacimiento: ') .strip()

    identificador = f'{nombre}.{apellido}{fecha_nacimiento}'
    '''print(f'El identificador del usuario es: {identificador}')'''
    return identificador
print(f'El identificador del usuario es: {datos()}')