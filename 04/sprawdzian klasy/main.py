class PojazdWodny:
    def __init__(self, nazwa: str, predkosc: int):
        self.nazwa = nazwa
        self.predkosc = predkosc

    def przedstaw_sie(self):
        return f"{self.nazwa} | Prędkość: {self.predkosc} km/h"

    def maksymalny_zasieg(self):
        raise NotImplementedError("Klasa pochodna musi zdefiniować metodę maksymalny_zasieg()")

class Lodz(PojazdWodny):
    def __init__(self, nazwa: str, predkosc: int, liczba_wiosel: int):
        super().__init__(nazwa, predkosc)
        self.liczba_wiosel = liczba_wiosel

    def przedstaw_sie(self):
        base = super().przedstaw_sie()
        return f"{base} | wiosła : {self.liczba_wiosel}"

    def maksymalny_zasieg(self):
        return f"Zasięg łodzi: {self.predkosc * 20 * self.liczba_wiosel} km"

class Okret(PojazdWodny):
    def __init__(self, nazwa: str, predkosc: int, liczba_dzial: int, stan_zalogi: int):
        super().__init__(nazwa, predkosc)
        self.liczba_dzial = liczba_dzial
        self.stan_zalogi = stan_zalogi


    def przedstaw_sie(self):
        base = super().przedstaw_sie()
        return f"{base} | działa: {self.liczba_dzial} | załoga: {self.stan_zalogi}"

    def maksymalny_zasieg(self):
        return f"Zasięg okrętu: {self.predkosc * 50 * self.stan_zalogi} km"



lodz = Lodz("Flis", 8, 4)
okret = Okret("Burza", 35, 12, 200)


print(lodz.przedstaw_sie())
print(lodz.maksymalny_zasieg())
print(okret.przedstaw_sie())
print(okret.maksymalny_zasieg())