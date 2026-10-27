tests = ["T001", "T002", "T003", "T004", "T005"]

nombres = ["Login", "Registro", "Compra", "Logout", "Busqueda"]

resultados = ["PASS", "FAIL", "PASS", "ERROR", "PASS"]

iterador_test = iter(tests)
iterador_nombre = iter(nombres)
iterador_resultado = iter(resultados)

contador_pass = 0 
contador_fail = 0
contador_error = 0 
total_tests = 0 

while True:
    try:
        test = next(iterador_test)
        nombre = next(iterador_nombre)
        resultado = next(iterador_resultado)

        print(f"Test: {test}- Nombre: {nombre}- Resultado: {resultado}")

        total_tests += 1 
        if resultado == 'PASS':
            contador_pass += 1
        elif resultado == 'FAIL':
            contador_fail +=1
        elif resultado == 'ERROR':
            contador_error += 1

    except StopIteration:
        break

if total_tests > 0:
    porcentaje_pass = (contador_pass / total_tests) * 100
else:
    porcentaje_pass = 0    

print("\n===== INFORME QA =====")
print(f"Total de pruebas: {total_tests}")
print(f"PASS: {contador_pass}")
print(f"FAIL: {contador_fail}")
print(f"ERROR: {contador_error}")
print(f"Porcentaje PASS: {porcentaje_pass:.2f}%")
