'''Tuplas

Una aplicación recibe las coordenadas de un usuario:

(1920, 1080)

La primera posición representa el ancho de pantalla y la segunda la altura.

Crea un programa que:

Guarde las coordenadas en una tupla.
Extraiga el ancho y la altura.
Calcule el número total de píxeles.
Determine si la resolución es Full HD o superior.

Pregunta para razonar:
¿Por qué tendría sentido utilizar una tupla en lugar de una lista en este caso?'''

mi_tupla = (1920,1080)

def analizar_tupla(mi_tupla):
    ancho, altura = mi_tupla
    total_pixeles = ancho * altura
    if total_pixeles >= 2073600:
        resolucion = 'Full HD o superior'
    else:
        resolucion = 'Menor a Full HD'
    return ancho, altura, total_pixeles, resolucion

ancho, altura, total_pixeles, resolucion = analizar_tupla(mi_tupla)
print(f'Ancho: {ancho}')
print(f'Altura: {altura}')
print(f'Total de píxeles: {total_pixeles}')
print(f'Resolución: {resolucion}')