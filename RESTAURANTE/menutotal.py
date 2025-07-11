

#clase padre Menu_item
class MenuItem:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self.__name = value
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")
    
    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__price = value
        else:
            raise ValueError("El precio debe ser un número positivo")

#clase bebida
class Beverage(MenuItem):
    def __init__(self, name, price, type_bebida):
        super().__init__(name, price)
        self.type_bebida = type_bebida

#clase aperitivo
class Appetizer(MenuItem):
    def __init__(self, name, price, type_aperitivo):
        super().__init__(name, price)
        self.type_aperitivo = type_aperitivo

#clase plato principal
class MainCourse(MenuItem):
    def __init__(self, name, price, type_principio):
        super().__init__(name, price)
        self.type_principio = type_principio

#clase postre
class Dessert(MenuItem):
    def __init__(self, name, price, type_dessert):
        super().__init__(name, price)
        self.type_dessert = type_dessert
