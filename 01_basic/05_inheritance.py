"""
Herencia
"""

#Superclass
class Vehicle:
    def __init__(self, brand, color, max_speed):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed

    def speed_up(self):
        print(f'we are accelerating a vehicle {self.brand} to {self.max_speed} Km/h')


#Subclass
class Car(Vehicle):     #Auto hereda de vehiculo
    def __init__(self, brand, color, max_speed, door):
        #llama de init de clase padre
        super().__init__(brand, color, max_speed)

        #nuevo atributo de auto
        self.door = door


class Motorcycle(Vehicle):
    def __init__(self, brand, color, max_speed):
        super().__init__(brand, color, max_speed)
        self.wheel = 2 # rueda

    def speed_up(self):
        print(f'We are speed up a motorcycle {self.brand}')
#End of class


myCar = Car("Mazda", "red", 200, 4)
myMoto = Motorcycle("Yahama", "black", 120)


#Car no tiene metodo speed_up, por lo que llama a speed_up de la clase padre
myCar.speed_up()
myMoto.speed_up()