# haslo = "tajnehaslo"
# podane = ""
# attempts = 0
# while podane != haslo and attempts < 5:
#     podane = input("podaj haslo: ")
#     attempts += 1
#     if podane != haslo:
#         print("niepoprawne haslo, sprobuj ponownie.")
#
# if podane == haslo:
#     print("poprawne haslo!")
# else:
#     print("wykorzystales wszystkie proby. Dostep zablokowany.")
#
#
# # else w petli while
#
# x = int(input("podaj liczbe (0 lub 1): "))
#
# while x==1:
#     print("podales: '1'")
#     break
# else:
#     print("podales: inna liczbe niz '1'")


# # oblicz nwd dwoch liczb (algorytm Euklidesa)
#
# a = int(input("podaj pierwsza liczbe: "))
# b = int(input("podaj druga liczbe: "))
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# else:
#     print("nwd wynosi = ", a)
#
# #algorytm na obliczanie nww z dodawaniem
#
# a1 = int(input("podaj pierwsza liczbe: "))
# b1 = int(input("podaj druga liczbe: "))
# a = a1
# b = b1
#
#
# while a1 != b1:
#     if a1 < b1:
#         a1 += a
#     else:
#         b1 += b
#
# print("nww wynosi = ", a1)
#


# metoda wyciagania wag zamien liczbe dziesietna na binarna

# sprawdzenie najwiekszej potegi 2 mniejszej lub rownej liczbie
dec = int(input("podaj liczbe dziesietna: "))
potega = 0
while 2 ** potega <= dec:
    potega += 1
potega -= 1
bin = []
while potega >= 0:
    if dec >= 2 ** potega:
        bin.append(1)
        dec -= 2 ** potega
    else:
        bin.append(0)
    potega -= 1
print("liczba binarna to: ", bin)

# zagniezdzone petle for

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")

#tabliczka mnozenia

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:4}", end="")
    print()