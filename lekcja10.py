# funkcja map() i lambda

# map(funkcja, kolekcja)

# liczby = list(map(int, input("podaj liczby oddzielone spacjami: ").split()))
# kwadraty = list(map(lambda x: x**2, liczby))
# print("Kwadraty podanych liczb:", kwadraty)
#
#
# literki = list(map(str, input("podaj literki oddzielone spacjami: ").split()))
# duze_litery = list(map(lambda x: x.upper(), literki))
# print("duże litery:", duze_litery)
#
# ceny = [10.5, 5.0, 3.2]
# ilosci = [3, 5, 2]
#
# wartosci = list(map(lambda c, i: c*i, ceny, ilosci))
# print("wartosci zakupow: ", wartosci)
#
def hello3(imie):
    print("Cześć " + imie + "!")

hello3('ania')

from math import pi

def circle_surface(r):
    return pi * r**2
print(circle_surface(5))

def circle(r, pi = pi):
    perimeter = 2 * pi * r
    area = pi * r**2
    return perimeter, area

a, b = circle(int(input("podaj promień: ")))
print(f"obwod {a:.2f} pole {b:.2f}")

def switchBMI(sex = "M", height = 170, weight = 70):
    if sex == "M":
        return lambda weight, height: (weight+2) / height **2
    else:
        return lambda weight, height: weight / height**2

BMI = switchBMI("M")
print(BMI(53, 1.75))

# lista liczb zwraca sume liczb parzystych

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def suma_parzystych(lista):
    return sum(x for x in lista if x % 2 == 0)

def policz_wystapienia(lista, element):
    return lista.count(element)

def cena_brutto(cena_netto, vat = 23):
    return(cena_netto * (1 + vat / 100))

