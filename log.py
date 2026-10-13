import re

logs = """
ERROR: TEST-245 no ha superado la prueba
INFO: TEST-381 ha superado la prueba
ERROR: TEST-72 tiene un identificador incorrecto
ERROR: TEST-9042 contiene demasiados dígitos
INFO: TEST-518 revisado
"""

# 1. Crear un patrón para identificar códigos TEST con exactamente 3 dígitos
cod_test = re.compile(r"TEST-(\d{3})(?!\d)")

# 2. Encontrar todos los identificadores válidos
valid_log = cod_test.findall(logs)
print(f"Identificadores válidos: {valid_log}")

# 3. Comprobar si existe TEST-381
test_381_ver = re.search(r"\bTEST-381\b", logs)

if test_381_ver:
    print("TEST-381 encontrado")
else:
    print("TEST-381 no encontrado")

# 4. Extraer únicamente los números de los identificadores válidos
tres_digitos = valid_log
print(f"Números extraídos: {tres_digitos}")
