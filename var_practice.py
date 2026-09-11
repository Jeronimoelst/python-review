'''Variables y asignación
Crea un programa que represente los datos de una persona:
nombre
edad
ciudad
salario mensual
si está trabajando actualmente
Después, calcula:
Cuánto ganaría al año.
Qué salario tendría después de recibir un aumento del 7%.
Muestra todos los datos de forma ordenada.
Condición: no escribas directamente los resultados calculados; deben salir de operaciones con las variables'''
def datos_persona():
    nombre_persona ='jeronimo'
    edad_persona =25
    ciudad ='mendoza'
    salario_mensual =1250.34
    trabaja_actualmente = True
    return nombre_persona, edad_persona, ciudad, salario_mensual, trabaja_actualmente

def calculos(salario_mensual):

    total_anual = salario_mensual * 12
    rebicion_de_salario = salario_mensual + salario_mensual * 0.07
    nuevo_salario_anual = rebicion_de_salario * 12
    return total_anual, rebicion_de_salario, nuevo_salario_anual



nombre, edad, ciudad, salario_mensual, trabaja_actualmente = datos_persona()
total_anual, rebicion_de_salario, nuevo_salario_anual = calculos(salario_mensual)

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Ciudad: {ciudad}")
print(f"Salario mensual: {salario_mensual}")
print(f"Trabaja actualmente: {trabaja_actualmente}")
print(f"Salario anual: {total_anual}")
print(f"Salario mensual después del aumento del 7%: {rebicion_de_salario}")
print(f"Salario anual después del aumento del 7%: {nuevo_salario_anual}") 
