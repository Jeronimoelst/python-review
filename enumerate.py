tests = ["Login", "Registro", "Compra", "Logout", "Busqueda"]

resultados = ["PASS", "FAIL", "PASS", "ERROR", "PASS"]

for i, (test,resultados) in enumerate(zip(tests, resultados), start=1):
    print(f"Test{i}: {test} - Resultado: {resultados}")