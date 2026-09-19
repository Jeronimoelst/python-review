'''Diccionarios

Imagina que estás almacenando los datos de un usuario de una aplicación:

nombre
edad
email
activo
numero_de_compras

Crea un diccionario con esos datos.

Después el programa debe:

Mostrar el nombre.
Comprobar si está activo.
Mostrar cuántas compras ha realizado.
Aumentar el número de compras en una unidad.
Añadir una nueva propiedad llamada premium.
Mostrar todos los datos finales.

Piensa: ¿por qué aquí es más adecuado un diccionario que una lista?
'''
class usuarios:
    def  __init__(self):
        self._usuario = {
             "nombre":  [],
             "edad": [],
             "email": [],
             "activo": [],
             "numero_de_compras": [],
        }
        

    def crear_usuario(self, nombre:str, edad:int, email:str, activo:bool, numero_de_compras:int):
        if not isinstance(nombre, str):
                raise ValueError("El nombre debe ser una cadena de texto.")
        if not isinstance(edad, int):
                raise ValueError("La edad debe ser un número entero.")
        if edad >= 18:
                raise ValueError("La edad debe ser mayor a 18.")
        if not isinstance(email, str):
                raise ValueError("El email debe ser una cadena de texto.")
        if not isinstance(activo, bool):
                raise ValueError("El estado de actividad debe ser un valor booleano.")
        if not isinstance(numero_de_compras, int):
                raise ValueError("El número de compras debe ser un número entero.")
        if numero_de_compras >= 10:
                raise ValueError("El número de compras debe ser mayor a 10.")

        self._usuario["nombre"].append(nombre)    
        self._usuario["edad"].append(edad)
        self._usuario["email"].append(email)
        self._usuario["activo"].append(activo)
        self._usuario["numero_de_compras"].append(numero_de_compras)

        print(f"datos del usuario: {self._usuario}")

    def obtener_dict(self):
        return self._usuario

registro = usuarios()

while True:
    try:
        nombre = input('introduce el nombre:').lower().strip()
        edad = int(input('introduce edad: '))
        email = input('introduce el email: ')
        activo = input("¿El usuario está activo? (si/no): ").lower().strip() == "si"
        numero_de_compras = int(input('introduce numero de compras: '))
        registro.crear_usuario(
            nombre= nombre,
            edad= edad,
            email= email,
            activo=activo,
            numero_de_compras= numero_de_compras
        )

        break

    
    except ValueError as e:
            print(f"\n[Error de Datos] {e}. Inténtalo de nuevo.\n")