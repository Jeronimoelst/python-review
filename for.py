resultados = [
    "PASS",
    "FAIL",
    "PASS",
    "ERROR",
    "SKIPPED",
    "PASS",
    "FAIL",
    "PASS",
    "ERROR",
    "PASS"
]

print(f"Resultados de los tests: {len(resultados)}")
def contar_resultados(resultados):
    
    contador_pass = 0
    contador_fail = 0
    contador_error = 0
    contador_skipped = 0
    
    
    for resultado in resultados:
        if resultado =='PASS':
            print("El resultado es PASS")
            contador_pass += 1
        elif resultado == 'FAIL':
            print("El resultado es FAIL")
            contador_fail += 1
        elif resultado == 'ERROR':
            print("El resultado es ERROR")
            contador_error += 1
        elif resultado == 'SKIPPED':
            print("El resultado es SKIPPED")
            contador_skipped += 1

    
    porcentaje_pass = (contador_pass / len(resultados)) * 100
    print(f"Porcentaje de PASS: {porcentaje_pass:.2f}%")

    
    print(f"PASS: {contador_pass}")
    print(f"FAIL: {contador_fail}")
    print(f"ERROR: {contador_error}")
    print(f"SKIPPED: {contador_skipped}")

    if porcentaje_pass >= 80:
        print("siute case passed")
    else:
        print("siute case failed")
contar_resultados(resultados)

