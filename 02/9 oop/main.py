class Prostokat:
    def __init__(self, a, b, colour="red"):
        self.a = a
        self.b = b
        self.colour = colour

    def area(self):
        return self.a * self.b

    def perimetr(self):
        return 2 * (self.a + self.b)


class KontoBankowe:
    def __init__(self, numer_konta, saldo=0):
        self.numer_konta = numer_konta
        self.saldo = saldo

    def wplata(self, kwota):
        self.saldo += kwota
        return f"Wpłacono {kwota} zł. Nowe saldo: {self.saldo} zł."

    def wyplata(self, kwota):
        if kwota > self.saldo:
            return "Niewystarczające środki na koncie."
        self.saldo -= kwota
        return f"Wypłacono {kwota} zł. Nowe saldo: {self.saldo} zł."

class StacjaBenzynowa:
    def __init__(self, nazwa, paliwa):
        self.nazwa = nazwa
        self.paliwa = paliwa

    def zatankuj(self, rodzaj_paliwa, ilosc):
        if rodzaj_paliwa in self.paliwa:
            return f"Zatankowano {ilosc} litrów {rodzaj_paliwa}."
        return f"Nie posiadamy {rodzaj_paliwa}."

if __name__ == "__main__":
    prostokat1 = Prostokat(5, 3)
    print(f"Pole prostokata: {prostokat1.area()}")
    print(f"Obwod prostokata: {prostokat1.perimetr()}")
    print(f"Kolor prostokata: {prostokat1.colour}")

    konto1 = KontoBankowe("123456789", 1000)
    print(konto1.wplata(500))
    print(konto1.wyplata(200))
    print(konto1.wyplata(1500))



