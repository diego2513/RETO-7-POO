
import json
import os
from collections import deque, namedtuple
from datetime import datetime
from typing import Dict, List, Optional

from metodos_de_pago import Cash, Card
from menutotal import Appetizer, Beverage, MainCourse, Dessert

def show_menu():
    print("+--------------------- MENÚ ---------------------+")
    print("|                   🥤 BEBIDAS                   |")
    print("|------------------------------------------------|")
    print(f"| Fanta          | ${fanta.price} | {fanta.type_bebida}                  |")
    print(f"| Agua           | ${agua.price} | {agua.type_bebida}                  |")
    print(f"| Vino           | ${vino.price} | {vino.type_bebida}              |")
    
    print("+------------------------------------------------+")
    print("|                🍽️ APERITIVOS                    |")
    print("|------------------------------------------------|")
    print(f"| Arepa con queso | ${arepas_queso.price} | {arepas_queso.type_aperitivo} |")
    print(f"| Palitos de queso| ${palitos_queso.price} | {palitos_queso.type_aperitivo} |")
    print(f"| Ensalada        | ${ensalada.price} | {ensalada.type_aperitivo}  |")

    print("+------------------------------------------------+")
    print("|            🍛 PLATOS PRINCIPALES               |")
    print("|------------------------------------------------|")
    print(f"| Perro caliente | ${perro_caliente.price} | {perro_caliente.type_principio} |")
    print(f"| Bandeja paisa  | ${bandeja_paisa.price} | {bandeja_paisa.type_principio}  |")
    print(f"| Carne de Res   | ${carne_asada.price} | {carne_asada.type_principio} |")

    print("+------------------------------------------------+")
    print("|                🍰 POSTRES                      |")
    print("|------------------------------------------------|")
    print(f"| Helado de fresa | ${helado.price} | {helado.type_dessert} |")
    print(f"| Brownie         | ${brownie.price} | {brownie.type_dessert} |")
    print(f"| Galleta         | ${galleta.price} | {galleta.type_dessert} |")

    print("+------------------------------------------------+")

MenuItem = namedtuple('MenuItem', ['name', 'price', 'category', 'type_categoria'])

class Order:
    #Inicializar lista para usar despues en la orden
    def __init__(self):
        self.finalorder = []
    
    #el usuario hace la orden a traves de iteraciones
    def add(self):
        #primer item de la orden o slair del programa en caso de digitar "no"
        item_name = input("\nIngresa el item del menu que quieras agregar a tu cuenta o 'no' para salir del programa: ").lower()
        if item_name in Menu:
            quantity = int(input(f"\n¿Cuántos {item_name} deseas ordenar?: "))
            self.finalorder.append((item_name, quantity)) #tupla en "finalorder" para generar la orden
        elif item_name == "no":
            quit()
        else:
            print(f"\nDisculpa {item_name} no esta en el menu")
            quantity = input("Ingresalo de nuevo")
            
        if item_name == "no":
            quit() #si "no", sale del programa
        while True:
            item_name = input("\nHay algo mas que quieras agregar o digita 'no' para terminar la orden: ")
            if item_name == "no":
                break  #si "no" se rompe la iteracion
            
            if item_name in Menu:
                quantity = int(input(f"\n¿Cuántos {item_name} deseas ordenar?: "))
                self.finalorder.append((item_name, quantity)) #tupla en "finalorder" para generar la orden
            else:
                print(f"\nDisculpa {item_name} no esta en el menu")

    def show_final_order(self):
        print(f"su orden es: {self.finalorder}") #Imprime la orden 
    
    def final_price(self):
        total = 0
        for final_item, quantity in self.finalorder:
            final_item = Menu[final_item] #ya que final_item es solo una palabra no tiene atributos por lo que aqui se convierte en un item de "Menu"
            if final_item == arepas_queso:
                print("Se ha aplicado un 50% de descuento en arepas con queso")  
                discount = arepas_queso.price * 0.5     #50 % off en arepas con queso
                total += discount * quantity
                 
            elif final_item == carne_asada:
                print("Se ha aplicado un 30% de descuento en carne asada") 
                discount = carne_asada.price * 0.7    #30% off si en carne asada
                total += discount * quantity
                  
            elif final_item == brownie:  
                print("Se ha aplicado un 90% de descuento en brownies")
                discount = brownie.price * 0.1    #90 % off en brownies
                total += discount * quantity
            elif final_item == helado:
                print("Se ha aplicado 2x1 en helado")
                free = quantity//2
                discount = helado.price * free
                total += (helado.price * quantity) - discount    
            else:
                total += final_item.price * quantity  # si no incluye ninguno de los anteriores simplemente se pone el precio normal
        return total


class OQueue:
    def __init__(self):
        self.orders = []
        self.order_conteo = 1
    
    def add_order(self, order):
        order.order_id = f"ORDEN-{self.order_conteo:04d}"
        self.orders.append(order)
        self.order_conteo += 1
        print(f"Orden {order.order_id} agregada a la cola.")
    
    def show_orders(self):
        print(f"\n=== ÓRDENES TOTALES ({len(self.orders)}) ===")
        for i, order in enumerate(self.orders, 1):
            print(f"{i}. {order.order_id} - Items: {len(order.finalorder)}")


class Menu2:
    def save_menu(self, menu_name: str, menu_dict: Dict):
        try:
            with open(f"{menu_name}.json", 'w') as f:
                menu_data = {}
                for item_key, item_obj in menu_dict.items():
                    menu_data[item_key] = {
                        "name": item_obj.name,
                        "price": item_obj.price,
                        "category": item_obj.__class__.__name__
                    }
                json.dump(menu_data, f, indent=2)
            print(f"Menú '{menu_name}' guardado exitosamente.")
            return True
        except Exception as e:
            print(f"Error al guardar menú: {e}")
            return False


Oqueue = OQueue()
MMenu = Menu2()

def goodbye():
    print("+------------------------------------------------+")
    print("|    🙌 GRACIAS POR VISITAR EL RESTAURANTE 🙌    |")
    print("+------------------------------------------------+")

def payment_mom(fprice):
    print("+------------------------------------------------+")
    print("|               MOMENTO DEL PAGO                 |")
    print("+------------------------------------------------+")
    print("\n\nMetodos de pago disponibles:")
    print("\nTarjeta de debito o credito")
    print("Efectivo")
    pago = input("\nQue metodo de pago prefieres: ")

    while pago not in ["efectivo" , "tarjeta"]:
        pago = input("Opcion de pago no valida, vuelve a ingresarla: ")

    if pago == "tarjeta":
        C = Card()

        print(f"\nTu tarjeta de {C.card_type} es:")
        print(f"\nNumero: {C.card_number}")
        print(f"Fecha de expiracion: {C.expirationM}/{C.expirationY}")
        print(f"Cvv: {C.cvv}")

        CCard = input("\nEs correcto, digita 'si' o 'no': ").lower()

        if CCard == "si":
            C.pay(fprice)
        else:
            again = input("\nPara cambiar el metodo de pago opcion 1 y para otra tarjeta opcion 2: ")

            while again not in ["1", "2"]:
                again = input("\nOpcion no valida ingresa de nuevo ")

            if again == "1":
                D = Cash(fprice)
            elif again == "2":
                C = Card()
    elif pago == "efectivo":
        D = Cash(fprice)

        print(f"Quieres pagar {fprice} con {D.money}")

        DCash = input("\nEs correcto, digita 'si' o 'no': ").lower()

        if DCash == "si":
            D.pay(fprice)
        else:
            again = input("\nPara cambiar el metodo de pago opcion 1 y para otro monto en efectivo opcion 2: ")

            while again not in ["1", "2"]:
                again = input("\nOpcion no valida ingresa de nuevo ")

            if again == "1":
                C = Card()
            elif again == "2":
                D = Cash(fprice)

fanta = Beverage("Fanta", 4000, "soda")
agua = Beverage("Agua", 2500, "agua")
vino = Beverage("Vino", 15000, "alcohol")
arepas_queso = Appetizer("Arepa con queso", 10000, "COLOMBIANO")
palitos_queso = Appetizer("Palitos de queso", 10000, "panaderia")
ensalada = Appetizer("Ensalada", 10000, "Fresco")
perro_caliente = MainCourse("Perro caliente", 12000, "Comida rapida")
bandeja_paisa = MainCourse("Bandeja paisa", 25000, "COLOMBIANO")
carne_asada = MainCourse("Carne de Res", 25000, "Proteina")
helado = Dessert("Helado de fresa", 6000, "Frio")
brownie = Dessert("Brownie", 7000, "Dulce")
galleta = Dessert("galleta", 4000, "Dulce")

Menu = {
    "fanta": fanta,
    "agua": agua,
    "vino": vino,
    "arepa con queso": arepas_queso,
    "palitos de queso": palitos_queso,
    "ensalada": ensalada,
    "perro caliente": perro_caliente,
    "bandeja paisa": bandeja_paisa,
    "carne asada": carne_asada,
    "helado": helado,
    "brownie": brownie,
    "galleta": galleta,
}

special_item = MenuItem("Plato Especial", 30000, "Especiales", "Plato del día")

def Extra_order():
    continue_orders = True
    while continue_orders:
        show_menu()
        O = Order()
        O.add()
        O.show_final_order()
        O.final_price()

        print (f"El precio final de tu cuenta aplicando las promociones seria de: ${O.final_price()} cop")

        tip_cop = int(input("Cuanto de propina deseas agregar: "))

        fprice = int(O.final_price()) + tip_cop
        print (f"El precio final de tu cuenta con propia incluida seria de: ${fprice} cop")

        Oqueue.add_order(O)
        
        payment_mom(fprice)
        
        another_order = input("\n¿Deseas procesar otra orden? (si/no): ").lower()
        if another_order == "no":
            continue_orders = False

if __name__ == "__main__":
    Extra_order()
    
    MMenu.save_menu("menu_principal", Menu)
    
    Oqueue.show_orders()
    
    goodbye()