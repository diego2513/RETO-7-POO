
class Payment_Method:
    def __init__(self):
        pass
    def pay(self, amount):
        self.amount = amount

class Card(Payment_Method):
    def __init__(self):
        self.__card_type = input("Es una tarjeta de debito o de credito?: ").lower()

        while self.__card_type not in ["credito", "debito"]:
            self.__card_type = input("Tipo de tarjeta no valido ingresa nuevamente: ")

        self.__card_number = (input("Ingresa el numero de la tarjeta: ").replace(" ", ""))

        while len(self.__card_number) != 16:
            self.__card_number = (input("Numero de tarjeta no valido por favor ingresalo nuevamente: ").replace(" ", ""))

        self.expirationM = int(input("Ingresa el mes de la fecha de expiracion de la tarjeta: "))

        while self.expirationM > 12 or self.expirationM < 0:
            print("Mes de la fecha de expiracion no valido")
            self.expirationM = int(input("Vuelve a Ingresar el mes de la fecha de expiracion de tu tarjeta: "))

        self.expirationY = int(input("Ingresa el año de la fecha de expiracion de tu tarjeta: "))

        while self.expirationY > 99 or self.expirationY < 25:
            print("Año de la fecha de expiracion no valido")
            self.expirationY = int(input("Vuelve a ingresar el año de la fecha de expiracion de tu tarjeta: "))

        while self.expirationY == 25 and self.expirationM < 6:
            print("Esta tarjeta ha expirado tienes que ingresa otra ")
            self.expirationM = int(input("Vuelve a Ingresar el mes de la fecha de expiracion de tu tarjeta: "))
            self.expirationY = int(input("Vuelve a ingresar el año de la fecha de expiracion de tu tarjeta: "))

        self.cvv = (input("Ingresa el codigo deseguridad de tu tarjeta: "))

        while len(self.cvv) < 3 or len(self.cvv) > 4:
            print("Cvv no valido deber de entre 3-4 numeros:")
            self.cvv = (input("Vuelve a ingresar el codigo de seguridad de tu tarjeta: "))

    @property
    def card_type(self):
        return self.__card_type
    
    @property
    def card_number(self):
        return self.__card_number
    
    @card_type.setter
    def card_type(self, value):
        if value.lower() in ["credito", "debito"]:
            self.__card_type = value.lower()
        else:
            raise ValueError("El tipo de tarjeta debe ser 'credito' o 'debito'")
    
    @card_number.setter
    def card_number(self, value):
        clean_number = value.replace(" ", "")
        if len(clean_number) == 16 and clean_number.isdigit():
            self.__card_number = clean_number
        else:
            raise ValueError("El número de tarjeta debe tener 16 dígitos")
    
    def pay(self, amount):
        self.amount = amount
        print(f"\nProcediendo con el pago de ${self.amount} con la tarjeta terminada en {self.__card_number[-4:]}")
        print(f"\nEl pago de ${self.amount} ha sido completado exitosamente")


class Cash(Payment_Method):
    def __init__(self, amount):
        self.amount = amount
        self.__money = int(input("Con cuanto pagaras el total de la cuenta: "))
        self.__change = self.__money - self.amount

    @property
    def money(self):
        return self.__money
    
    @property
    def change(self):
        return self.__change
    
    @money.setter
    def money(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__money = value
            self.__change = self.__money - self.amount
        else:
            raise ValueError("El dinero debe ser un número positivo")

    def pay(self, amount):
        self.amount = amount
        print(f"\nProcediendo con el pago de ${self.amount} con el monto de ${self.__money} en efectivo")
        print(f"\nEl pago de {self.amount} ha sido exitoso tu cambio es de {self.__change}")