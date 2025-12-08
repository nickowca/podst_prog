### OPERACJE NA PLIKACH ###

"""
teoria - tryby otwierania plików:
r - odczytywanie (read): domyślny tryb. zgłasza błąd, jeśli plik nie istnieje.
w - zapisywanie (write): otwiera plik do zapisu. jeśli plik istnieje, jego zawartość jest kasowana!
a - dopisywanie (append): otwiera plik, ale nie kasuje zawartości. dopisuje dane na końcu.
b - tryb binarny (binary): do plików nietekstowych (np. obrazki, dźwięk).
t - tryb tekstowy (text): domyślny dla plików z tekstem.
+ - aktualizacja: pozwala na jednoczesny odczyt i zapis.
"wb" / "rb" - konkretne połączenia: zapis binarny / odczyt binarny.
"""
print("\n\n")
print("------------------")


print("1. Odczyt pliku tekstowego")

print("------------------")
print("\n\n")


# odczyt pliku tekstowego - standardowy sposob

print("1a. odczyt pliku tekstowego\n")
# funkcja open() zwraca uchwyt do pliku (file handle)
# jeśli nie podamy drugiego argumentu, domyślnie jest to "r" (odczyt)
f = open("text/test.txt")
# metoda read() czyta całą zawartość pliku do jednego stringa
print(f.read())
# w tej metodzie musimy pamiętać o ręcznym zamknięciu pliku metodą close()
# jest to ważne aby zwolnić zasoby systemowe
f.close()

print("------------------")

# od czyt pliku tekstowego przy uzyciu with - automatyczne zamykanie pliku

print("1b. odczyt pliku tekstowego przy uzyciu with\n")
# konstrukcja 'with' to tzw. manager kontekstu
# jest bezpieczniejsza, bo gwarantuje zamknięcie pliku nawet jeśli wystąpi błąd
with open("text/test.txt") as f:
  print(f.read())
# tutaj plik jest już automatycznie zamknięty (po wyjściu z wcięcia)

print("------------------")

# sprawdzanie wlasciwosci pliku - nazwa, tryb, czy zamkniety

print("1c. sprawdzanie właściwości pliku\n")
f = open("text/test.txt", "r")
# obiekt pliku przechowuje informacje o sobie w zmiennych
print("Filename:", f.name) # nazwa pliku (ścieżka)
print("Mode:", f.mode) # tryb pracy (np. 'r', 'w')
print("Is Closed?", f.closed) # zwraca false, bo plik jest otwarty

f.close()
# po zamknięciu atrybut closed zmieni się na true
print("Is Closed?", f.closed)

print("------------------")


# odczyt liniami - petla for

print("1d. odczyt liniami\n")
# to najlepszy sposób na czytanie dużych plików
# pętla for pobiera z pliku po jednej linii na raz
with open("text/test.txt") as file:
    for l in file:
        # strip() usuwa białe znaki z początku i końca (w tym enter '\n')
        # bez strip() mielibyśmy podwójne odstępy między liniami
        print(l.strip())

print("------------------")


# odczyt czesciowy pliku - read(n) odczytuje n znakow

print("1e. odczyt czesciowy pliku\n")
with open("text/test.txt") as f:
  # podanie liczby w read() ogranicza odczyt do tylu znaków
  print(f.read(5)) # zwroci pierwsze 5 znakow

print("------------------")


# odczyt pierwszej linii - readline()

print("1f. odczyt pierwszej linii\n")
with open("text/test.txt") as f:
  # readline() czyta tylko jedną linię tekstu i zatrzymuje się
  print(f.readline())

print("------------------")


# odczyt dwoch pierwszych linii - dwa razy readline()
print("1g. odczyt dwoch pierwszych linii\n")
with open("text/test.txt") as f:
  print(f.readline()) # linia 1
  print(f.readline()) # linia 2

print("------------------")

# odczyt wszystkich linii do listy - readlines()
print("1h. odczyt wszystkich linii do listy\n")
with open("text/test.txt") as f:
    # readlines() wczytuje caly plik i tworzy listę stringów
    # każda linia z pliku jest osobnym elementem listy
    lines = f.readlines()
    print(lines)

print("\n\n")

print("------------------")

print("2. Zapis do pliku tekstowego")

print("------------------")

print("\n\n")



# zapis do pliku tekstowego - write()

print("2a. zapis do pliku tekstowego\n")
# tryb "w" jest destrukcyjny - jeśli plik istnieje, zostanie wyczyszczony!
with open("text/output.txt", "w") as f: # "w" nadpisuje lub tworzy nowy plik
    # metoda write() nie dodaje automatycznie entera, musimy dodać '\n' sami
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
# ponowne użycie trybu "w" skasuje wszystko co zostalo zrobione w punktach wyżej
with open("text/output.txt", "w") as f:
  f.write("ups! usunalem wszystko i zapisuje na nowo\n")

# odczyt pliku text/output.
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
# pliki jak obrazki (.png, .jpg) muszą być otwierane z literką 'b'
# kopiowanie pliku binarnego polega na odczytaniu bajtów z jednego i zapisaniu w drugim
with open("images/image_copy.png", "wb") as f: # "wb" - zapis binarny
    with open("images/image.png", "rb") as original: # "rb" - odczyt binarny
        f.write(original.read()) # read() tutaj czyta bajty, nie tekst
print("skopiowano plik image.png do image_copy.png")
print("------------------")

# odczyt pliku binarnego - read binary
print("3b. odczyt pliku binarnego\n")
with open("images/image.png", "rb") as f:
    data = f.read(10) # odczyt pierwszych 10 bajtow (nagłówek pliku)
    print("pierwsze 10 bajtow pliku image.png:", data)
print("------------------")

# 4. usuwanie plikow
print("\n\n")
print("------------------")

print("4. Usuwanie plików")

print("------------------")
print("\n\n")

# usuwanie pliku
# do operacji na plikach (usuwanie, zmiana nazwy) potrzebujemy biblioteki os
import os
# funkcja remove() trwale usuwa plik z dysku
os.remove("text/output.txt")
print("usunieto plik text/output.txt")
# sprawdzenie czy plik istnieje
# warto sprawdzać czy plik istnieje przed próbą odczytu/usunięcia, aby uniknąć błędów
if not os.path.exists("text/output.txt"):
    print("plik text/output.txt nie istnieje")
print("------------------")
