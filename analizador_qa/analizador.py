from pathlib import Path

ruta_resultados = Path(__file__).parent / "resultados.txt"

with open(ruta_resultados, 'r', encoding='utf-8') as archivo:
    resultados = archivo.readlines()

for i in range(len(resultados)):
    print(f"Resultado {i + 1}: {resultados[i].strip()}")

contador_pass = 0
contador_fail = 0
contador_error = 0
contador_skipped = 0

for i in range(len(resultados)):
    if resultados[i].strip() == "PASS":
        contador_pass += 1
    elif resultados[i].strip() == "FAIL":
        contador_fail += 1
    elif resultados[i].strip() == "ERROR":
        contador_error += 1
    elif resultados[i].strip() == "SKIPPED":
        contador_skipped += 1

print(f"Pass: {contador_pass}")
print(f"Fail: {contador_fail}")
print(f"Error: {contador_error}")
print(f"Skipped: {contador_skipped}")

total_resultados = len(resultados)
porcentaje_pass = 0.0
if total_resultados > 0:
    porcentaje_pass = (contador_pass / total_resultados) * 100

ruta_informe = Path(__file__).parent / "informe.txt"

with open(ruta_informe, 'w', encoding='utf-8') as archivo:
    archivo.write(f"Total de resultados: {total_resultados}\n")
    archivo.write(f"Porcentaje de pass: {porcentaje_pass:.2f}%\n")
    archivo.write(f"Pass: {contador_pass}\n")
    archivo.write(f"Fail: {contador_fail}\n")
    archivo.write(f"Error: {contador_error}\n")
    archivo.write(f"Skipped: {contador_skipped}\n")
