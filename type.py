'''Crea variables utilizando exactamente esos valores.

Tu programa debe determinar:

qué tipo tiene inicialmente cada variable;
convertir "25" a entero;
convertir "18.75" a decimal;
convertir "True" a booleano;
comprobar al final que las conversiones tienen el tipo esperado.

Objetivo: practicar type() y conversión de tipos.'''

numero_entero_str = '25'
numero_decimal_str = '18.75'
valor_bool_str = 'True'

print(f'Ahora 25 es:{type(numero_entero_str)}' )
print(f'Ahora 18.75 es:{type(numero_decimal_str)}' )
print(f'Ahora True es:{type(valor_bool_str)}' ) 

def determinar_tipos(numero_entero_str, numero_decimal_str, valor_bool_str):
    numero_entero = int(numero_entero_str)
    numero_decimal = float(numero_decimal_str)
    valor_bool= valor_bool_str == 'True'
    return numero_entero, numero_decimal, valor_bool


numero_entero, numero_decimal, valor_bool = determinar_tipos(numero_entero_str, numero_decimal_str, valor_bool_str)
print(f'tipo de 25: {type(numero_entero)}')
print(f'tipo de 18.75: {type(numero_decimal)}')
print(f'tipo de True: {type(valor_bool)}')
