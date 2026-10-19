import sys 


if len(sys.argv) < 2:
    print("...")
else:
    resultados = sys.argv[1].upper()
    match resultados:
        
        case "PASS":
            print("El resultado es positivo.")
        case "FAIL":
            print("El resultado es negativo.")
        case "ERROR":
            print("El resultado es un error.")
        case "SKIPPED":
            print("El resultado a saltado.")
        case _:
            print("IndexError: El resultado no es válido.")