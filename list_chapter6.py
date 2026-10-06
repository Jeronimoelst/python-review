
resultados = [
    "PASS",
    "FAIL",
    "PASS",
    "ERROR",
    "PASS",
    "SKIPPED",
    "FAIL",
    "PASS"
]

# 1. Imprime cuántos tests hay en total
print(f"Total de tests: {len(resultados)}")


# 2. Imprime el primer resultado
print(f"Primer resultado: {resultados[0]}")

# 3. Imprime el último resultado
print(f"Último resultado: {resultados[-1]}")

# 4. Recorre la lista e imprime cada resultado
for resultado in resultados:
    print(f"Resultado: {resultado}")

# 5. Imprime únicamente los resultados que NO sean PASS
print('resultados que NO sean PASS:')
for resultado in resultados:
    if resultado != 'PASS':
        print(f'Resultados que no son PASS: {resultado}')

# 6. Cuenta cuántos FAIL hay
fail_count = resultados.count('FAIL')

# 7. Cuenta cuántos ERROR hay
error_count = resultados.count('ERROR')

# 8. Comprueba si existe algún SKIPPED
skipped_exists = 'SKIPPED' in resultados


# 9. Añade un nuevo resultado "PASS" al final
resultados.append('PASS')

# 10. Elimina el resultado "SKIPPED"
resultados.remove('SKIPPED')

# 11. Imprime la posición del primer "ERROR"
erro_index = resultados.index('ERROR')

# 12. Utiliza enumerate() para mostrar:
# Índice: 0 - Resultado: PASS
# Índice: 1 - Resultado: FAIL
# etc.
for i, resultado in enumerate(resultados):
    print(f'indice: {i} - resultado: {resultado}')

# 13. Calcula el porcentaje de tests PASS
pass_count = resultados.count('PASS')
total_tests = len(resultados)
pass_percentage = (pass_count / total_tests) * 100

# 14. Si el porcentaje de PASS es >= 80:
#     imprime "TEST SUITE APROBADA"
#     En caso contrario:
#     imprime "TEST SUITE NO APROBADA"
if pass_percentage >= 80:
    print("TEST SUITE APROBADA")
else:
    print("TEST SUITE NO APROBADA")