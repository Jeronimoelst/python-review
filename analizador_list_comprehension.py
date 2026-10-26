tests = ["T001", "T002", "T003", "T004", "T005", "T006", "T007", "T008"]

resultados = [
    "PASS", "FAIL", "PASS", "ERROR",
    "PASS", "SKIPPED", "FAIL", "PASS"
]

nombres = [
    "Login",
    "Registro",
    "Compra",
    "Logout",
    "Busqueda",
    "Perfil",
    "Carrito",
    "Pago"
]

tests_pass = [
    test
    for test, resultado in zip(tests, resultados)
    if resultado == "PASS"
]

print(f"Tests passed: {tests_pass}")

tests_fail=[
    test
    for test, resultado in zip(tests,resultados)
    if resultado == "FAIL"
]

print(f"Tests failed: {tests_fail}")

nombres_pass = [
    nombre
    for nombre, resultado in zip(nombres, resultados)
    if resultado == "PASS"
]

print(f"Names of tests passed: {nombres_pass}")

resultados_unicos = {
    resultado for resultado in resultados
}
print(f'Unique results: {resultados_unicos}')

informe = {
    test : resultado
    for test, resultado in zip(tests, resultados)

}
print(f"inform: {informe}")

total_tests = len(tests)
total_pass = len(tests_pass)
total_fail = len(tests_fail)
porcentaje_pass = (total_pass * total_tests)/ 100

print(total_tests)
print(total_pass)
print(total_fail)
print(f'porcentaje de pruebas aprobadas: {porcentaje_pass:.2f}%')


