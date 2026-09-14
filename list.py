'''Listas + lógica aplicada a QA

Crea una lista con estos resultados de pruebas:

"PASS"
"FAIL"
"PASS"
"PASS"
"FAIL"

Crea una función llamada:

analizar_resultados()

La función debe:

Recorrer la lista.
Contar cuántos "PASS" hay.
Contar cuántos "FAIL" hay.
Calcular el porcentaje de pruebas aprobadas.
Devolver esos tres valores.
Mostrar el resultado de forma clara.
Condición adicional

Si el porcentaje de pruebas aprobadas es 80% o superior, debe aparecer:

Estado del test: APROBADO

Si es inferior:

Estado del test: REVISAR'''

lista_test = ['PASS', 'FAIL', 'PASS', 'PASS', 'FAIL']
lista_test.extend(['PASS', 'PASS', 'PASS', 'FAIL', 'PASS', 'FAIL', 'PASS', 'PASS', 'FAIL', 'PASS'])

def analizar_resultados():
    test_pass = lista_test.count('PASS')
    test_fail = lista_test.count('FAIL')
    total_tests = len(lista_test)
    porcentaje_aprobados = (test_pass / total_tests) * 100
    if porcentaje_aprobados >= 80:
        resultado_test = 'aprobado'
    else:
        resultado_test = 'revisar'

    print(f'cantidad de pruebas aprobadas: {test_pass}')
    print(f'cantidad de pruebas falladas: {test_fail}')
    print(f'porcentaje de pruebas aprobadas: {porcentaje_aprobados:.2f}%')
    print(f'estado del test: {resultado_test.upper()}')
    return test_pass, test_fail, porcentaje_aprobados
print(analizar_resultados())
