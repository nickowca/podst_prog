import math

class Figura:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def opis(self):
        return f"Figura: {self.nazwa}"

    def pole(self):
        raise NotImplementedError("Klasa pochoda musi zdefiniowac motode pole()")

    def obwod(self):
        pass

class Prostokat(Figura):
    def __init__(self, a, b):
        super().__init__("Prostokat")
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return 2 * (self.a + self.b)


class Kolo(Figura):
    def __init__(self, r):
        super().__init__("Kolo")
        self.r = r

    def pole(self):
        return math.pi * self.r ** 2

    def obwod(self):
        return 2 * math.pi * self.r



class Trojkat(Figura):
    def __init__(self, a, b, c):
        super().__init__("Trojkat")
        self.a = a
        self.b = b
        self.c = c

    def pole(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def obwod(self):
        return self.a + self.b + self.c

p = Prostokat(5, 3)
print(p.opis())
print(f"Pole: {p.pole()}")
print(f"Obwod: {p.obwod()}")
t = Trojkat(3, 4, 5)
print(t.opis())
print(f"Pole: {t.pole()}")
print(f"Obwod: {t.obwod()}")



print()