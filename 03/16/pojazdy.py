class Pojazd:
    def __init__(self, marka, predkosc_max):
        self.marka = marka
        self.predkosc_max = predkosc_max
        print(f" [Pojazd.__init__] Utworzono pojazd: {self.marka}")

        def info(self):
            return f"Pojazd: {self.marka}, prędkość max: {self.predkosc_max} km/h"

class Samochod(Pojazd):
    def __init__(self, marka, predkosc_max, liczba_drzwi, ilosc_kol = 4):
        super().__init__(marka, predkosc_max)
        self.liczba_drzwi = liczba_drzwi
        self.ilosc_kol = ilosc_kol
        print(f" [Samochod.__init__] Utworzono samochód: {self.marka} z {self.liczba_drzwi} drzwiami i {self.ilosc_kol} kołami")

    def info(self):
        return f"Samochód: {self.marka}, prędkość max: {self.predkosc_max} km/h, drzwi: {self.liczba_drzwi}, koła: {self.ilosc_kol} szt."


class Motocykl(Pojazd):
    def __init__(self, marka, predkosc_max, ilosc_kol, pojemnosc, typ):
        super().__init__(marka, predkosc_max)
        self.typ = typ
        self.ilosc_kol = ilosc_kol
        self.pojemnosc = pojemnosc
        print(f" [Motocykl.__init__] Utworzono motocykl: {self.marka} typu {self.typ}")

    def info(self):
        return f"Motocykl: {self.marka}, prędkość max: {self.predkosc_max} km/h, typ: {self.typ}"


s = Samochod("Toyota", 180, 4)
print(s.info())

