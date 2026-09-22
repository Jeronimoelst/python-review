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
