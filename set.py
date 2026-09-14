'''Sets

Tienes los siguientes usuarios que han realizado una determinada prueba:

usuarios_dia_1 = ["Ana", "Carlos", "Pedro", "Laura", "Ana"]
usuarios_dia_2 = ["Pedro", "Laura", "Juan", "Carlos", "Pedro"]

Utilizando conjuntos, determina:

Todos los usuarios únicos.
Los usuarios que realizaron la prueba ambos días.
Los usuarios que solamente aparecen el primer día.
Cuántos usuarios diferentes realizaron la prueba en total.

Objetivo: entender realmente para qué sirve un set.'''
usuarios_dia_1 = ["Ana", "Carlos", "Pedro", "Laura", "Ana"]
usuarios_dia_2 = ["Pedro", "Laura", "Juan", "Carlos", "Pedro"]
set_dia_1 = set(usuarios_dia_1)
set_dia_2 = set(usuarios_dia_2)


usuarios_unicos = set_dia_1.union(set_dia_2)
usuarios_ambos_dias = set_dia_1.intersection(set_dia_2)
usuarios_solo_primer_dia = set_dia_1 - set_dia_2
usuarios_total = len(usuarios_unicos)

print(f'Usuarios únicos: {usuarios_unicos}')
print(f'Usuarios que realizaron la prueba ambos días: {usuarios_ambos_dias}')
print(f'Usuarios que solamente aparecen el primer día: {usuarios_solo_primer_dia}')
print(f'Usuarios que realizaron la prueba en total: {usuarios_total}')




'''

'''
