resultados = [
    " pass ",
    "FAIL",
    " error ",
    "PASS",
    " skipped ",
    "fail",
    "PASS",
    "ERROR",
    " pass",
    " skipped",
    "FAIL ",
    "pass",
    " error",
    "SKIPPED",
    " fail "
]
resultado_normalizados = [resultados.strip().upper() for resultados in resultados]
contador_resultados = {
    "PASS": 0,
    "FAIL": 0,
    "ERROR": 0,
    "SKIPPED": 0
}
for resultado in resultado_normalizados:
    if resultado == "PASS":
        print("Resultado: PASS")
        contador_resultados["PASS"] += 1
    elif resultado == "FAIL":
        print("Resultado: FAIL")
        contador_resultados["FAIL"] += 1
    elif resultado == "ERROR":
        print("Resultado: ERROR")
        contador_resultados["ERROR"] += 1
    elif resultado == "SKIPPED":
        print("Resultado: SKIPPED")
        contador_resultados["SKIPPED"] += 1
    else:
        print("Resultado desconocido:", resultado)

print("\nContador de resultados:")
for resultado, contador in contador_resultados.items():
    print(f"{resultado}: {contador}")
    
