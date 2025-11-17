#INSTRUKCJA
#Wykonuj kolejne zadania (w dowolnej kolejności i gdy nie będą się pojawiać błędy
#usuń z początku i końca kodu znaczniki komentarza: ' """ '

#Zadanie 1 – Popraw błędy składniowe // 1 pkt
#W tym programie są błędy składniowe i logiczne. Popraw go, by działał poprawnie.

print("Zadanie 1 – Popraw błędy składniowe")

liczby = [3, 5, 7, 9]
for i in liczby:
    if i % 2 == 0:
        print(f"Liczba {i} jest parzysta")
    else:
        print("Nieparzysta:", i)

print("--------------------------------------------")

# Zadanie 2 - silnia z błędami  // 1 pkt
# Program powinien obliczać silnię liczby n.
# Silnia n to iloczyn liczb od 1 do n (np. silnia 4 to 1*2*3*4, a wynikiem jest 24)
# Znajdź i popraw błędy.

print("Zadanie 2 – silnia z błędami")

n = int(input("Podaj liczbę: "))
silnia = 1
for i in range(1, n + 1):
    silnia *= i
print("Silnia wynosi:", silnia)

print("--------------------------------------------")

# Zadanie 3 - zliczanie słów  // 1 pkt
# Program powinien zliczać wystąpienia słów w tekście, z wykorzystaniem słownika
# Popraw błędy i przetestuj działanie.

print("Zadanie 3 - zliczanie słów")

text = input("Podaj tekst: ")
slowa = text.split()
zlicz = {}    #deklaracja pustego słownika
for s in slowa:
    if s not in zlicz:
        zlicz[s] = 1   #dodanie nowego elementu do słownika
    else:
        zlicz[s] += 1
print(zlicz)

print("--------------------------------------------")

#Zadanie 4 – Duplikaty  // 1 pkt
# Uzupełnij program tak, aby usuwał duplikaty z listy bez użycia set() (czyli zbiorów).
# W miejsce _________ wpisz odpowiednie części programu

print("Zadanie 4 – Duplikaty")

lista = [3, 5, 3, 8, 5, 2, 8, 1]
unique = []

for x in lista:
    if x not in unique:
        unique.append(x)

print(unique)

print("--------------------------------------------")

#Zadanie 5 – Długości stringów  // 1 pkt
# Uzupełnij program tak, aby zamieniał listę stringów na listę długości tych stringów.
# W miejsce _________ wpisz odpowiednie części programu

print("Zadanie 5 – Długości stringów")

words = ["Python", "AI", "Programowanie", "Kot"]
lengths = [ len(w) for w in words ]
print(lengths)

print("--------------------------------------------")

# Zadanie 6 – Lista liczb dodatnich  // 1 pkt
# Uzupełnij program, aby do listy `dodatnie` trafiły tylko liczby większe od 0.

print("Zadanie 6 – Lista liczb dodatnich")

liczby = [3, -1, 0, 8, -5, 10]
pozytywne = []

for x in liczby:
    #twój kod
    if x > 0:
        pozytywne.append(x)

print(f"Liczby dodatnie:{pozytywne}")


print("--------------------------------------------")

#Zadanie 7 – Sortowanie  // 2 pkt
# Napisz program, który pobiera 3 liczby od użytkownika i wypisuje je w kolejności rosnącej.
# Nie używaj funkcji sort(), tylko własnej logiki (if / elif / else).

print("Zadanie 7 – Sortowanie")

x, y, z = map(int, input("podaj trzy liczby odzdzielone spacjami: ").split())

if x > y:
    h = x
    x = y
    y = h
if  x > z:
    h = x
    x = z
    z = h
if y > z:
    h = y
    y = z
    z = h


print(x,y,z)

print("--------------------------------------------")

# Zadanie 8 - Lista liczb  // 2 pkt
# Napisz program, który wczyta ciąg liczb (np. "3 7 -1 0 5"),
# a następnie:
#   a) utworzy listę z tych liczb
#   b) obliczy sumę liczb dodatnich
#   c) obliczy liczbę wartości ujemnych
#   d) wypisze wynik w postaci: "Suma dodatnich = X, liczba ujemnych = Y"

print("Zadanie 8 - Lista liczb")
#Miejsce na twój kod


liczby = [ int(x) for x in input("podaj liczby oddzielone spacjami: ").split() ]

suma_d = 0
liczba_u = 0


for x in liczby:
    if x > 0:
        suma_d += x

liczba_u = sum(1 for x in liczby if x < 0)

print(liczby)
print(f"Suma dodatnich: {suma_d}, liczba ujemnych = {liczba_u}")

print("--------------KONIEC------------------")