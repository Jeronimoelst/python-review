'''Operadores de comparación

Tienes:

edad = ...
salario = ...

El programa debe determinar si una persona cumple los requisitos para solicitar una determinada ayuda.

Requisitos:

Tener al menos 18 años.
Tener un salario inferior a 1.500 €.

El programa debe producir un booleano indicando si cumple los requisitos.

Después prueba diferentes valores para comprobar que funciona correctamente.'''

edad = int(input ('edad: '))
salario = int(input('salario: '))

def condiciones_de_consecion(edad, salario):
    if edad >= 18 and salario < 1500:
        return True
    else:
        return False

resultado = condiciones_de_consecion(edad, salario)

print(resultado)

'''
ejemplo mas avanzado:

edad = int(input ('edad: '))
salario = int(input('salario: '))

def condiciones_de_consecion(edad, salario):
    return edad >= 18 and salario < 1500


resultado = condiciones_de_consecion(edad, salario)

print(resultado)

'''
