from pathlib import Path
import shutil

carpeta = Path("analizador2/archivos_resultados")
carpeta.mkdir(parents=True, exist_ok=True)

contador_pass = 0
contador_fail = 0
total_tests = 0
resultados = []

while True:
    resultado = input("Ingrese el resultado del test (pass/fail) o 'fin' para terminar: ").strip().lower()
    if resultado == 'pass':
        contador_pass += 1
        total_tests += 1
        resultados.append('pass')
    elif resultado == 'fail':
        contador_fail += 1
        total_tests += 1
        resultados.append('fail')
    elif resultado == 'fin':
        break
    else:
        print("Resultado no válido. Introduce PASS, FAIL o FIN.")
print(f"Tests passed: {contador_pass}")
print(f"Tests failed: {contador_fail}")
print(f"Total tests: {total_tests}")    

archivo = carpeta / "resultados.txt"
if archivo.exists():
    numero = 1
    while True:
        nuevo_nombre = carpeta / f"resultados_{numero}.txt"
        
        if not nuevo_nombre.exists():
            shutil.copy(archivo, nuevo_nombre)
            print(f"Copia de seguridad: {nuevo_nombre}")
            break

        numero += 1
contenido = (
    f"Tests passed: {contador_pass}\n"
    f"Tests failed: {contador_fail}\n"
    f"Total tests: {total_tests}\n"
    f"Resultados: {', '.join(resultados)}\n"
)

archivo.write_text(contenido, encoding="utf-8")

print(f"Archivo guardado: {archivo}")