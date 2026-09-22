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

Intenta mantener cada cálculo en una variable diferente para poder comprobar tu razonamiento.

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
        self.__items['precio original'].append(precio_original),
        self.__items['descuento'].append(descuento),
        self.__items['precio con descuento'].append(precio_con_descuento),
        descuento = precio_original * descuento / 100
        precio_con_descuento = precio_original - descuento
        return precio_con_descuento
        

    def iva_incluido(self, precio_con_descuento, precio_con_iva):
        self.__items['precio con descuento'].append(precio_con_descuento),
        self.__items['precio con iva'].append(precio_con_iva),
        precio_con_iva = precio_con_descuento + precio_con_descuento * 21/100
        return precio_con_iva

    def precio_final(self, precio_final, precio_con_iva):
        precio_final = precio_con_iva
    
        


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
        print(f"datos del ticket: {self.__items}")
        


    def obtner_ticket(self):
        return self.__items

creacion_ticket = tickect()


while True:
    try:
        precio_original = float(input('precio original')),
        descuento = int(input('descuento ')), 
        precio_con_descuento = float(input('precio con descuento')),
        precio_con_iva = float(input('precio con iva')),
        precio_final = float(input('precio final'))
        creacion_ticket.crear_tickets(
            precio_original = precio_original,
            descuento = descuento,
            precio_con_descuento =precio_con_descuento,
            precio_con_iva = precio_con_iva,
            precio_final = precio_final
        )

        break
    except ValueError as e:
            print(f"\n[Error de Datos] {e}. Inténtalo de nuevo.\n")


'''


class Ticket:

    def __init__(self):
        self.__items = {
            "precio_original": [],
            "descuento": [],
            "precio_con_descuento": [],
            "iva": [],
            "precio_final": []
        }

    def crear_ticket(self, precio_original, descuento):

        importe_descuento = precio_original * descuento / 100

        precio_con_descuento = precio_original - importe_descuento

        iva = precio_con_descuento * 21 / 100

        precio_final = precio_con_descuento + iva

        self.__items["precio_original"].append(precio_original)
        self.__items["descuento"].append(descuento)
        self.__items["precio_con_descuento"].append(precio_con_descuento)
        self.__items["iva"].append(iva)
        self.__items["precio_final"].append(precio_final)

        print("\n--- TICKET ---")
        print(f"Precio original: {precio_original:.2f} €")
        print(f"Descuento: {descuento:.2f}%")
        print(f"Precio con descuento: {precio_con_descuento:.2f} €")
        print(f"IVA: {iva:.2f} €")
        print(f"Precio final: {precio_final:.2f} €")

    def obtener_tickets(self):
        return self.__items
        
creacion_ticket = Ticket()

precio_original = float(input("Precio original: "))
descuento = int(input("Descuento (%): "))

creacion_ticket.crear_ticket(
    precio_original,
    descuento
)

print(creacion_ticket.obtener_tickets())
