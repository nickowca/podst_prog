# wyrazenia skladane w pythonie

# kwadraty = []
# for x in range(5):
#     kwadraty.append(x ** 2)
# print(kwadraty)

# to jest to sam co wyzej, ale krocej

# kwadraty = [x ** 2 for x in range(5)]
# print(kwadraty)
#
# # 1. list comprehension z petla for
#
# kwadraty = [x ** 2 for x in range(1, 11)]
#
# # dodanie filtra if
# parzyste = [x for x in range(1,11) if x % 2 == 0]
# print(parzyste)
#
# # dla kazdej liczby x od 1 do 10 oblicz x**2 i  zbuduj liste wynikowa
# kwadraty = [x ** 2 for x in range(1, 11)]
# print(kwadraty)
#
# #lista zawierajacy kwadraty liczb od 1 do 20 ale tylko tych, ktore sa podzielne przez 3
# kwadraty = [x ** 2 for x in range(1, 21) if x % 3 == 0]
# print(kwadraty)
#
# # utworzenie listy zawierajacej tylko samogloski z podanego napisu
# napis = input("podaj napis: ")
# samogloski = [litera for litera in napis if litera.lower() in 'aąeęioóuy']
# print(samogloski)
#
#
# slowa = ["Python", "jest", "Super", "językiem", "dla", "Programistów", "ale"]
# wynik = [s for s in slowa if s[0].isupper() and len(s) > 4]
# print(wynik)
#
# #if else w list comprehension
# parzyste_nieparzyste = [ "parzysta" if x % 2 == 0 else "nieparzysta" for x in range(1, 11)]
# print(parzyste_nieparzyste)
#
#
# #wypisywanie imion zawierajace litere l
# imiona = ["Anna", "marek", "Kasia", "piotr", "Zofia", "ala"]
# imiona_litera_l = [imie for imie in imiona if 'l' in imie.lower()]
# print(imiona_litera_l)


lista_liczb = ["mała" if l < 5 else ("średnia" if l == 5 else "duża") for l in range(1,11)]

print(lista_liczb)