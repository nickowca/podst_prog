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


# odczyt pliku tekstowego - standardowy sposób
# open() - otwiera plik
# read() - odczytuje całą zawartość pliku
# close() - zamyka plik (ważne! zawsze należy zamknąć plik po użyciu)

print("1a. odczyt pliku tekstowego\n")
f = open("text/test.txt")  # otwarcie pliku do odczytu
print(f.read())  # odczytanie i wyświetlenie całej zawartości
f.close()  # zamknięcie pliku

print("------------------")

# odczyt pliku tekstowego przy użyciu with - automatyczne zamykanie pliku
# with - menedżer kontekstu, automatycznie zamyka plik po zakończeniu bloku
# nie trzeba używać close() - plik zamyka się automatycznie

print("1b. odczyt pliku tekstowego przy uzyciu with\n")
with open("text/test.txt") as f:  # automatyczne zamknięcie pliku po zakończeniu bloku
  print(f.read())  # odczytanie całej zawartości

print("------------------")

# sprawdzanie właściwości pliku - nazwa, tryb, czy zamknięty
# name - zwraca nazwę pliku
# mode - zwraca tryb otwarcia pliku (r, w, a, rb, wb, etc.)
# closed - zwraca True jeśli plik jest zamknięty, False jeśli otwarty

print("1c. sprawdzanie właściwości pliku\n")
f = open("text/test.txt", "r")  # "r" - tryb odczytu (read)
print("Filename:", f.name)  # nazwa pliku
print("Mode:", f.mode)  # tryb pracy
print("Is Closed?", f.closed)  # sprawdza czy plik jest zamknięty (False)

f.close()  # zamykamy plik
print("Is Closed?", f.closed)  # teraz plik jest zamknięty (True)

print("------------------")


# odczyt liniami - pętla for
# iteracja po liniach pliku za pomocą pętli for
# strip() - usuwa białe znaki (spacje, entery) z początku i końca linii

print("1d. odczyt liniami\n")
with open("text/test.txt") as file:
    for l in file:  # iteracja po każdej linii pliku
        print(l.strip())  # wyświetlenie linii bez białych znaków na końcach

print("------------------")


# odczyt częściowy pliku - read(n) odczytuje n znaków
# read(n) - odczytuje n znaków z pliku
# przydatne przy pracy z dużymi plikami

print("1e. odczyt czesciowy pliku\n")
with open("text/test.txt") as f:
  print(f.read(5))  # zwróci pierwsze 5 znaków z pliku

print("------------------")


# odczyt pierwszej linii - readline()
# readline() - odczytuje jedną linię z pliku
# każde kolejne wywołanie readline() czyta kolejną linię

print("1f. odczyt pierwszej linii\n")
with open("text/test.txt") as f:
  print(f.readline())  # odczytuje i wyświetla pierwszą linię

print("------------------")


# odczyt dwóch pierwszych linii - dwa razy readline()
# kolejne wywołania readline() odczytują kolejne linie
print("1g. odczyt dwoch pierwszych linii\n")
with open("text/test.txt") as f:
  print(f.readline())  # pierwsza linia
  print(f.readline())  # druga linia

print("------------------")

# odczyt wszystkich linii do listy - readlines()
# readlines() - zwraca listę wszystkich linii z pliku
# każda linia jest osobnym elementem listy
print("1h. odczyt wszystkich linii do listy\n")
with open("text/test.txt") as f:
    lines = f.readlines()  # odczytuje wszystkie linie do listy
    print(lines)  # wyświetla listę linii

print("\n\n")

print("------------------")

print("2. Zapis do pliku tekstowego")

print("------------------")

print("\n\n")



# zapis do pliku tekstowego - write()
# "w" - tryb zapisu (write), nadpisuje całą zawartość pliku lub tworzy nowy plik
# write() - zapisuje tekst do pliku (trzeba ręcznie dodać \n dla nowej linii)

print("2a. zapis do pliku tekstowego\n")
with open("text/output.txt", "w") as f:  # "w" nadpisuje lub tworzy nowy plik
    f.write("pierwsza linia do zapisania\n")  # zapisujemy pierwszą linię
    f.write("druga linia do zapisania\n")  # zapisujemy drugą linię
print("zapisano do pliku output.txt")
# odczyt pliku output.txt
print("\nzawartosc pliku output.txt:\n")
with open("text/output.txt") as f:  # odczytujemy zapisany plik
    print(f.read())

print("------------------")

# dopisywanie do pliku tekstowego - append()
# "a" - tryb dopisywania (append), dodaje tekst na koniec pliku
# nie usuwa istniejących danych, tylko dopisuje na koniec
print("2b. dopisywanie do pliku tekstowego\n")
with open("text/output.txt", "a") as f:  # "a" - tryb dopisywania
  f.write("dopisana linia\n")  # dopisujemy nową linię na koniec

# odczyt pliku output.txt
with open("text/output.txt") as f:
  print(f.read())  # wyświetlamy całą zawartość
print("------------------")
# nadpisywanie pliku tekstowego - write()
# "w" - tryb zapisu (write) usuwa całą poprzednią zawartość!
# UWAGA: użycie "w" na istniejącym pliku usuwa jego całą zawartość
print("2c. nadpisywanie pliku tekstowego\n")
with open("text/output.txt", "w") as f:  # "w" usuwa poprzednią zawartość
  f.write("ups! usunalem wszystko i zapisuje na nowo\n")

# odczyt pliku text/output.txt
print("\nzawartosc pliku text/output.txt:\n")
with open("text/output.txt") as f:
  print(f.read())  # poprzednia zawartość została usunięta

print("------------------")

print("3. Operacje na plikach binarnych")

print("------------------")
print("\n\n")
# zapis do pliku binarnego - write binary
# "wb" - tryb zapisu binarnego (write binary) - do obrazów, filmów, etc.
# "rb" - tryb odczytu binarnego (read binary)
# pliki binarne to np. obrazy, filmy, pliki wykonywalne
print("3a. zapis do pliku binarnego\n")
with open("images/image_copy.png", "wb") as f:  # "wb" - zapis binarny
    with open("images/image.png", "rb") as original:  # "rb" - odczyt binarny
        f.write(original.read())  # kopiujemy dane binarne z jednego pliku do drugiego
print("skopiowano plik image.png do image_copy.png")
print("------------------")

# odczyt pliku binarnego - read binary
# read(n) w trybie binarnym odczytuje n bajtów
# dane binarne wyświetlane są jako bytes (np. b'\x89PNG...')
print("3b. odczyt pliku binarnego\n")
with open("images/image.png", "rb") as f:  # "rb" - odczyt binarny
    data = f.read(10)  # odczyt pierwszych 10 bajtów
    print("pierwsze 10 bajtow pliku image.png:", data)  # wyświetla dane binarne
print("------------------")

