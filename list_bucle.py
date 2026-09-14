'''Recorrer resultados de tests

Utiliza esta lista:

resultados = [
    "PASS",
    "FAIL",
    "PASS",
    "ERROR",
    "PASS",
    "FAIL",
    "SKIPPED",
    "PASS"
]

Crea una función:

analizar_resultados()

Pero esta vez no puedes utilizar count().

La función debe recorrer la lista y contar manualmente:

PASS
FAIL
ERROR
SKIPPED

Después debe calcular:

total de tests
porcentaje de PASS

Y mostrar:

PASS: X
FAIL: X
ERROR: X
SKIPPED: X
Total: X
Porcentaje PASS: X%
🎯 Condición

Esta vez quiero que utilices un bucle for.

Todavía no necesitas aprender while.

Este ejercicio es un salto importante porque pasamos de:

"Sé utilizar métodos de listas"

a:

"Sé procesar datos elemento por elemento."

Y eso es fundamental para QA Automation.'''
lista_de_resultados=["PASS",
    "FAIL",
    "PASS",
    "ERROR",
    "PASS",
    "FAIL",
    "SKIPPED",
    "PASS"]

def analizar_resultados(lista_de_resultados):
    pass_count = 0
    fail_count = 0
    error_count = 0
    skipped_count = 0
    for resultado in lista_de_resultados:
        if resultado == 'PASS':
            pass_count += 1
        elif resultado == 'FAIL':
            fail_count += 1
        elif resultado == 'ERROR':
            error_count += 1
        elif resultado == 'SKIPPED':
            skipped_count += 1
    total_test = len(lista_de_resultados)
    porcentaje_pass = (pass_count / total_test)* 100
    print(F'pass:{pass_count}')
    print(F'fail:{fail_count}')
    print(F'error:{error_count}')
    print(F'skipped:{skipped_count}')
    print(F'total:{total_test}')
    print(F'porcentaje pass:{porcentaje_pass:.2f}%')
print(analizar_resultados(lista_de_resultados))