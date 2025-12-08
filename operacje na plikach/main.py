### OPERACJE NA PLIKACH ###

"""
r - odczytywanie
w - zapisywanie
a - dopisywanie
b - tryb binarny
t - tryb tekstowy
+ - otwarcie do odczytu i zapisu
"wb" / "rb" - zapis/odczyt w trybie binarnym
"""
print("\n\n")
print("------------------")


print("1. Odczyt pliku tekstowego")

print("------------------")
print("\n\n")


# odczyt pliku tekstowego - standardowy sposob

print("1a. odczyt pliku tekstowego\n")
f = open("text/test.txt")
print(f.read())
f.close()

print("------------------")

# od czyt pliku tekstowego przy uzyciu with - automatyczne zamykanie pliku

print("1b. odczyt pliku tekstowego przy uzyciu with\n")
with open("text/test.txt") as f:
  print(f.read())

print("------------------")

# sprawdzanie wlasciwosci pliku - nazwa, tryb, czy zamkniety

print("1c. sprawdzanie właściwości pliku\n")
f = open("text/test.txt", "r")
print("Filename:", f.name) # nazwa pliku
print("Mode:", f.mode) # tryb pracy
print("Is Closed?", f.closed) # sprawdza czy plik jest zamkniety

f.close()
print("Is Closed?", f.closed)

print("------------------")


# odczyt liniami - petla for

print("1d. odczyt liniami\n")
with open("text/test.txt") as file:
    for l in file:
        print(l.strip())

print("------------------")


# odczyt czesciowy pliku - read(n) odczytuje n znakow

print("1e. odczyt czesciowy pliku\n")
with open("text/test.txt") as f:
  print(f.read(5)) # zwroci pierwsze 5 znakow

print("------------------")


# odczyt pierwszej linii - readline()

print("1f. odczyt pierwszej linii\n")
with open("text/test.txt") as f:
  print(f.readline())

print("------------------")


# odczyt dwoch pierwszych linii - dwa razy readline()
print("1g. odczyt dwoch pierwszych linii\n")
with open("text/test.txt") as f:
  print(f.readline())
  print(f.readline())

print("------------------")

# odczyt wszystkich linii do listy - readlines()
print("1h. odczyt wszystkich linii do listy\n")
with open("text/test.txt") as f:
    lines = f.readlines()
    print(lines)

print("\n\n")

print("------------------")

print("2. Zapis do pliku tekstowego")

print("------------------")

print("\n\n")



# zapis do pliku tekstowego - write()

print("2a. zapis do pliku tekstowego\n")
with open("text/output.txt", "w") as f: # "w" nadpisuje lub tworzy nowy plik
    f.write("pierwsza linia do zapisania\n")
    f.write("druga linia do zapisania\n")
print("zapisano do pliku output.txt")
# odczyt pliku output.txt
print("\nzawartosc pliku output.txt:\n")
with open("text/output.txt") as f:
    print(f.read())

print("------------------")

# dopisywanie do pliku tekstowego - append()
print("2b. dopisywanie do pliku tekstowego\n")
with open("text/output.txt", "a") as f:
  f.write("dopisana linia\n")

# odczyt pliku output.txt
with open("text/output.txt") as f:
  print(f.read())
print("------------------")
# nadpisywanie pliku tekstowego - write()
print("2c. nadpisywanie pliku tekstowego\n")
with open("text/output.txt", "w") as f:
  f.write("ups! usunalem wszystko i zapisuje na nowo\n")

# odczyt pliku text/output.txt
print("\nzawartosc pliku text/output.txt:\n")
with open("text/output.txt") as f:
  print(f.read())
print("\n\n")
print("------------------")

print("3. Operacje na plikach binarnych")

print("------------------")
print("\n\n")
# zapis do pliku binarnego - write binary
print("3a. zapis do pliku binarnego\n")
with open("images/image_copy.png", "wb") as f: # "wb" - zapis binarny
    with open("images/image.png", "rb") as original: # "rb" - odczyt binarny
        f.write(original.read())
print("skopiowano plik image.png do image_copy.png")
print("------------------")

# odczyt pliku binarnego - read binary
print("3b. odczyt pliku binarnego\n")
with open("images/image.png", "rb") as f:
    data = f.read(10) # odczyt pierwszych 10 bajtow
    print("pierwsze 10 bajtow pliku image.png:", data)
print("------------------")

# 4. usuwanie plikow
print("\n\n")
print("------------------")

print("3. Usuwanie plików")

print("------------------")
print("\n\n")

# usuwanie pliku
import os
os.remove("text/output.txt")
print("usunieto plik text/output.txt")
# sprawdzenie czy plik istnieje
if not os.path.exists("text/output.txt"):
    print("plik text/output.txt nie istnieje")
print("------------------")
