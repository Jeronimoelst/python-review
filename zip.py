tests = ["T001", "T002", "T003", "T004", "T005"]
nombre = ["Login", "Registro", "Compra", "Logout", "Busqueda"]
resultados = ["PASS", "FAIL", "PASS", "ERROR", "PASS"]

contador_pass = 0
contador_fail = 0
contador_error = 0
contador_total = 0
for test,nombre, resultados in zip(tests,nombre,resultados):
    print(f"Test: {test}, Nombre: {nombre}, Resultado: {resultados}")
    
    if resultados == "PASS":
        contador_pass += 1
    elif resultados == "FAIL":
        contador_fail += 1
    else:
        contador_error += 1
    contador_total += 1
porcentaje_pass = (contador_pass / contador_total) * 100    
print(f"Total PASS: {contador_pass}")
print(f"Total FAIL: {contador_fail}")
print(f"Total ERROR: {contador_error}")
print(f"Total Tests: {contador_total}")
print(f"Porcentaje de PASS: {porcentaje_pass:.2f}%")