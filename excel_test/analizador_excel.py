from pathlib import Path
import openpyxl

# Buscar el Excel en la misma carpeta que este archivo Python
ruta_excel = Path(__file__).parent / "resultados.xlsx"

libro = openpyxl.load_workbook(ruta_excel)


def analizar_excel(libro):
    # Seleccionar la hoja activa
    hoja = libro.active

    # Inicializar contadores
    total_tests = 0
    tests_passed = 0
    tests_failed = 0
    tests_omitidos = 0

    # Recorrer las filas desde la segunda
    for fila in hoja.iter_rows(min_row=2, values_only=True):
        resultado = fila[1]

        # Comprobar si la celda está vacía
        if resultado is None or resultado == "":
            tests_omitidos += 1
            continue

        resultado = str(resultado).strip().upper()
        total_tests += 1

        if resultado == "PASS":
            tests_passed += 1
        elif resultado == "FAIL":
            tests_failed += 1

    # Mostrar resultados
    print(f"Total de pruebas procesadas: {total_tests}")
    print(f"Pruebas aprobadas: {tests_passed}")
    print(f"Pruebas fallidas: {tests_failed}")
    print(f"Pruebas omitidas: {tests_omitidos}")


analizar_excel(libro)
