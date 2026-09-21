'''Operadores aritméticos

Una tienda tiene este producto:

Precio: 85 €
Descuento: 15 %
IVA: 21 %

Calcula el precio final que pagará el cliente.

Pero cuidado: debes razonar correctamente el orden.

Primero se aplica el descuento y después el IVA.

El programa debe mostrar:

Precio original:
Descuento:
Precio después del descuento:
IVA:
Precio final:

Intenta mantener cada cálculo en una variable diferente para poder comprobar tu razonamiento.'''

class tickect:
    def __init__(self):
        self.__items={
            'precio original' : [],
            'descuento' : [],
            'precio con descuento' : [],
            'precio con iva' : [],
            'precio final' : [],
        }

    def descuento(self, precio_original, descuento, precio_con_descuento):
        self.__items('precio original').append[precio_original],
        self.__items('descuento').append[descuento],
        self.__items('precio con descuento').append[precio_con_descuento],
        precio_con_descuento = precio_original - descuento

    def iva_incluido(self, precio_con_descuento, precio_con_iva):
        self.__items('precio con descuento').append[precio_con_descuento],
        self.__items('precio con iva').append[precio_con_iva],
        precio_con_iva = precio_con_descuento + 21% precio_con_descuento
    
        


    def crear_tickets(self, precio_original:float, descuento:int, precio_con_descuento:float,precio_con_iva:float,precio_final:float):
        if precio_original != float:
            raise ValueError('El precio debe ser un numero valido')
        if descuento != int:
            raise ValueError('debe ser un porcentaje verdadero')
        if precio_con_descuento != precio_original - descuento:
            raise ValueError('el precio no aplico bien el descuento')
        if precio_con_iva !=  21% precio_con_descuento:
            raise ValueError('el iva no esta aplicado')
        if precio_final != precio_con_iva:
            raise ValueError('algo anda mal')
'''vincular los datos que entran con el back
     ej:
     self._usuario["nombre"].append(nombre)    
             self._usuario["edad"].append(edad)
             self._usuario["email"].append(email)
             self._usuario["activo"].append(activo)
             self._usuario["numero_de_compras"].append(numero_de_compras)
     
             print(f"datos del usuario: {self._usuario}")
     
             luego
             obtener el return
             y crear el while true
     
     '''