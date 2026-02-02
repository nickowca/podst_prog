class Car:
    def __init__(self, make, model, year, colour="White", fuel_type="Petrol", max_speed=160):
        self.fuel_type = fuel_type
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.max_speed = max_speed
        self.mileage = 0

    def display_info(self):
        return f"{self.year} {self.colour} {self.make} {self.model}, Max Speed: {self.max_speed} km/h, Fuel Type: {self.fuel_type}"

    def drive(self, distance):
        self.mileage += distance
        return f"you have driven {distance} km. total mileage is now {self.mileage} km."



new_car = Car("BMW", "X5", 2020, "Black", fuel_type="Diesel", max_speed=250)
print(new_car.display_info())
print(new_car.drive(100))
print(type(new_car))
print(f"{new_car.make}")
print(new_car)

sports_car = Car("Porsche", "911", 2022, "Red", max_speed=320)
family_car = Car("Toyota", "Camry", 2019, fuel_type="Hybrid", max_speed=210)
print(sports_car.display_info())
print(family_car.display_info())

print(sports_car.drive(254))
print(family_car.drive(150))
print(sports_car.mileage)



# funkcja speclajna __mul__
class Produkt:
    def __init__(self, nazwa, cena: float):
        self.nazwa = nazwa
        self.cena = cena
        self.liczba_sztuk = 1

    def __str__(self) -> str:
        return f"{self.nazwa} (Cena {self.cena}zł)"

    def __mul__(self, ilosc: int) -> int:
        return self.cena * ilosc

    def wypisz(self) -> str:
        print(f"{self.nazwa} (cena: {self.cena}zł Ilosc sztuk: {self.liczba_sztuk})")

oranges = Produkt("pomaranacze", 3.99)
pen = Produkt("pendrive", 50)

oranges.wypisz()
print(pen*10)

class Dog: