class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"



new_car = Car("BMW", "X5", 2020)
print(new_car.display_info())

print(new_car)