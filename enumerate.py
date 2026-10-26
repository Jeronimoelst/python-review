tests = ["Login", "Registro", "Compra", "Logout", "Busqueda"]

resultados = ["PASS", "FAIL", "PASS", "ERROR", "PASS"]
contador_pass = 0

for i, (test,resultado) in enumerate(zip(tests, resultados), start=1):
    if resultado == "PASS":
        contador_pass += 1


    print(f"Test{i}: {test} - Resultado: {resultados}")
    print(f"Cantidad de tests que pasaron: {contador_pass}")