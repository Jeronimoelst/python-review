resultados = [
    "PASS",
    "FAIL",
    "PASS",
    "ERROR",
    "SKIPPED",
    "PASS",
    "FAIL",
    "PASS",
    "ERROR"
]
contador_pass = 0
contador_fail = 0
contador_error = 0
contador_skipped = 0

for resultado in resultados:
    if resultado == 'PASS':
        contador_pass += 1
    elif resultado == 'FAIL':  
        contador_fail += 1
    elif resultado == 'ERROR':
        contador_error += 1
    elif resultado == 'SKIPPED':
        pass  # No se incrementa ningún contador para SKIPPED
    
if contador_pass > contador_fail:
        print("Hay más tests pasados que fallidos.")
else:
        print("Hay más tests fallidos que pasados.")
