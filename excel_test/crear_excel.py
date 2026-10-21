
import openpyxl

# Crear un libro Excel nuevo
libro = openpyxl.Workbook()

# Cambiar el nombre de la hoja
hoja = libro.active
hoja.title = "Resultados"

# Crear los encabezados
hoja["A1"] = "Test"
hoja["B1"] = "Resultado"

# Introducir los resultados de prueba
datos = [
    ["TEST-101", "PASS"],
    ["TEST-102", "FAIL"],
    ["TEST-103", "PASS"],
    ["TEST-104", ""],
    ["TEST-105", "FAIL"],
    ["TEST-106", "PASS"]
]

for fila in datos:
    hoja.append(fila)

# Guardar el archivo Excel
libro.save("resultados.xlsx")

print("Archivo resultados.xlsx creado correctamente.")