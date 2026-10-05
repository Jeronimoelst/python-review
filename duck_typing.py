class TestLogin:
    def ejecutar(self):
        print("Test de login ejecutado")


class TestCompra:
    def ejecutar(self):
        print("Test de compra ejecutado")

def ejecutar_test(test):
    try:
        test.ejecutar()

    except AttributeError:
        print("El objeto no tiene el método 'ejecutar'")
   

ejecutar_test(TestLogin())
ejecutar_test(TestCompra())
ejecutar_test("hola")
