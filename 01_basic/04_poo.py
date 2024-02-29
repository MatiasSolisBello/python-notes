class Car:
    # Constructor
    def __init__(self, color, max_speed, brand):
        self.color = color
        self.max_speed = max_speed
        self.brand = brand

    def speed_up(self): # metodo
        print(f'we are accelerating with a max. of {self.max_speed}')
# End of class


myCar = Car('blue', 200, "Toyota") # objeto o instancia de la clase auto
print(f'{myCar.color}, {myCar.brand}, {myCar.max_speed}')
myCar.speed_up()    # retorna lo indicado en el metodo