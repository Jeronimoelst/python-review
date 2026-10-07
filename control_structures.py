'''usuarios = [
    {"nombre": "Ana", "edad": 25, "activo": True},
    {"nombre": "Carlos", "edad": 17, "activo": True},
    {"nombre": "Laura", "edad": 30, "activo": False},
    {"nombre": "Pedro", "edad": 22, "activo": True},
]

for usuario in usuarios:
    if usuario['edad'] >= 18 and usuario['activo']:
        print(f"{usuario['nombre']} es mayor de edad y está activo.")
    elif usuario['edad'] < 18: 
        print(f"{usuario['nombre']} es menor de edad.")
    elif not usuario['activo']:
        print(f"{usuario['nombre']} no está activo.")
        '''
resultados = [
    "PASS",
    "FAIL",
    "PASS",
    "ERROR",
    "PASS",
    "SKIPPED",
    "FAIL",
    "PASS"
]
contador_pass = 0
contador_fail = 0
contador_error = 0
contador_skipped = 0
for resultado in resultados:
    if resultado == "PASS":
        print("pass")
        contador_pass += 1
    elif resultado == "FAIL":
        print("fail")
        contador_fail += 1
    elif resultado == "ERROR":
        print("error")
        contador_error += 1
    elif resultado == "SKIPPED":
        print("skipped")
        contador_skipped += 1
    else:
        print("Resultado desconocido.")

print(f"Total de tests pasados: {contador_pass}")
print(f"Total de tests fallidos: {contador_fail}")
print(f"Total de tests con error: {contador_error}")
print(f"Total de tests omitidos: {contador_skipped}")