'''is / is not

Tienes:

resultado = None

Crea un programa que determine si todavía existe un resultado.

Después cambia el valor de resultado por un texto cualquiera y vuelve a comprobarlo.

Objetivo: entender cuándo utilizar is en lugar de ==.'''

resultado = None

if resultado is None:
    print ('el programa sigue vacio')
else:
    print('el resultado tiene un valor')