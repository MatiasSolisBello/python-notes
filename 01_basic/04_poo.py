from datetime import date

class Car:
    # Constructor
    def __init__(self, color, max_speed, brand, date_fabrication):
        self.color = color
        self.max_speed = max_speed
        self.brand = brand
        self.date_fabrication = date_fabrication

    def get_data(self):
        print(f'{self.color}, {self.brand}, {self.max_speed}, {self.date_fabrication}')

    # calcular la edad en base a su fecha de fabricación
    def get_age(self):
        year_fabrication = self.date_fabrication.year
        today = date.today().year
        return print(today - year_fabrication)
# End of class

# objeto o instancia de la clase auto
myCar = Car('blue', 200, "Toyota", date(2000, 2, 2))
myCar.get_data()
myCar.get_age()