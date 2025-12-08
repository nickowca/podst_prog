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
# open() - otwiera plik
# read() - odczytuje cala zawartosc pliku
# close() - zamyka plik (wazne! zawsze nalezy zamknac plik po uzyciu)

print("1a. odczyt pliku tekstowego\n")
f = open("text/test.txt")  # otwarcie pliku do odczytu
print(f.read())  # odczytanie i wyswietlenie calej zawartosci
f.close()  # zamkniecie pliku

print("------------------")

# odczyt pliku tekstowego przy uzyciu with - automatyczne zamykanie pliku
# with - menedzer kontekstu, automatycznie zamyka plik po zakonczeniu bloku
# nie trzeba uzywac close() - plik zamyka sie automatycznie

print("1b. odczyt pliku tekstowego przy uzyciu with\n")
with open("text/test.txt") as f:  # automatyczne zamkniecie pliku po zakonczeniu bloku
  print(f.read())  # odczytanie calej zawartosci

print("------------------")

# sprawdzanie wlasciwosci pliku - nazwa, tryb, czy zamkniety
# name - zwraca nazwe pliku
# mode - zwraca tryb otwarcia pliku (r, w, a, rb, wb, etc.)
# closed - zwraca True jesli plik jest zamkniety, False jesli otwarty

print("1c. sprawdzanie właściwości pliku\n")
f = open("text/test.txt", "r")  # "r" - tryb odczytu (read)
print("Filename:", f.name)  # nazwa pliku
print("Mode:", f.mode)  # tryb pracy
print("Is Closed?", f.closed)  # sprawdza czy plik jest zamkniety (False)

f.close()  # zamykamy plik
print("Is Closed?", f.closed)  # teraz plik jest zamkniety (True)

print("------------------")


# odczyt liniami - petla for
# iteracja po liniach pliku za pomoca petli for
# strip() - usuwa biale znaki (spacje, entery) z poczatku i konca linii

print("1d. odczyt liniami\n")
with open("text/test.txt") as file:
    for l in file:  # iteracja po kazdej linii pliku
        print(l.strip())  # wyswietlenie linii bez bialych znakow na koncach

print("------------------")


# odczyt czesciowy pliku - read(n) odczytuje n znakow
# read(n) - odczytuje n znakow z pliku
# przydatne przy pracy z duzymi plikami

print("1e. odczyt czesciowy pliku\n")
with open("text/test.txt") as f:
  print(f.read(5))  # zwroci pierwsze 5 znakow z pliku

print("------------------")


# odczyt pierwszej linii - readline()
# readline() - odczytuje jedna linie z pliku
# kazde kolejne wywolanie readline() czyta kolejna linie

print("1f. odczyt pierwszej linii\n")
with open("text/test.txt") as f:
  print(f.readline())  # odczytuje i wyswietla pierwsza linie

print("------------------")


# odczyt dwoch pierwszych linii - dwa razy readline()
# kolejne wywolania readline() odczytuja kolejne linie
print("1g. odczyt dwoch pierwszych linii\n")
with open("text/test.txt") as f:
  print(f.readline())  # pierwsza linia
  print(f.readline())  # druga linia

print("------------------")

# odczyt wszystkich linii do listy - readlines()
# readlines() - zwraca liste wszystkich linii z pliku
# kazda linia jest osobnym elementem listy
print("1h. odczyt wszystkich linii do listy\n")
with open("text/test.txt") as f:
    lines = f.readlines()  # odczytuje wszystkie linie do listy
    print(lines)  # wyswietla liste linii

print("\n\n")

print("------------------")

print("2. Zapis do pliku tekstowego")

print("------------------")

print("\n\n")



# zapis do pliku tekstowego - write()
# "w" - tryb zapisu (write), nadpisuje cala zawartosc pliku lub tworzy nowy plik
# write() - zapisuje tekst do pliku (trzeba recznie dodac \n dla nowej linii)

print("2a. zapis do pliku tekstowego\n")
with open("text/output.txt", "w") as f:  # "w" nadpisuje lub tworzy nowy plik
    f.write("pierwsza linia do zapisania\n")  # zapisujemy pierwsza linie
    f.write("druga linia do zapisania\n")  # zapisujemy druga linie
print("zapisano do pliku output.txt")
# odczyt pliku output.txt
print("\nzawartosc pliku output.txt:\n")
with open("text/output.txt") as f:  # odczytujemy zapisany plik
    print(f.read())

print("------------------")

# dopisywanie do pliku tekstowego - append()
# "a" - tryb dopisywania (append), dodaje tekst na koniec pliku
# nie usuwa istniejacych danych, tylko dopisuje na koniec
print("2b. dopisywanie do pliku tekstowego\n")
with open("text/output.txt", "a") as f:  # "a" - tryb dopisywania
  f.write("dopisana linia\n")  # dopisujemy nowa linie na koniec

# odczyt pliku output.txt
with open("text/output.txt") as f:
  print(f.read())  # wyswietlamy cala zawartosc
print("------------------")
# nadpisywanie pliku tekstowego - write()
# "w" - tryb zapisu (write) usuwa cala poprzednia zawartosc!
# UWAGA: uzycie "w" na istniejacym pliku usuwa jego cala zawartosc
print("2c. nadpisywanie pliku tekstowego\n")
with open("text/output.txt", "w") as f:  # "w" usuwa poprzednia zawartosc
  f.write("ups! usunalem wszystko i zapisuje na nowo\n")

# odczyt pliku text/output.txt
print("\nzawartosc pliku text/output.txt:\n")
with open("text/output.txt") as f:
  print(f.read())  # poprzednia zawartosc zostala usunieta

print("------------------")

print("3. Operacje na plikach binarnych")

print("------------------")
print("\n\n")
# zapis do pliku binarnego - write binary
# "wb" - tryb zapisu binarnego (write binary) - do obrazow, filmow, etc.
# "rb" - tryb odczytu binarnego (read binary)
# pliki binarne to np. obrazy, filmy, pliki wykonywalne
print("3a. zapis do pliku binarnego\n")
with open("images/image_copy.png", "wb") as f:  # "wb" - zapis binarny
    with open("images/image.png", "rb") as original:  # "rb" - odczyt binarny
        f.write(original.read())  # kopiujemy dane binarne z jednego pliku do drugiego
print("skopiowano plik image.png do image_copy.png")
print("------------------")

# odczyt pliku binarnego - read binary
# read(n) w trybie binarnym odczytuje n bajtow
# dane binarne wyswietlane sa jako bytes (np. b'\x89PNG...')
print("3b. odczyt pliku binarnego\n")
with open("images/image.png", "rb") as f:  # "rb" - odczyt binarny
    data = f.read(10)  # odczyt pierwszych 10 bajtow
    print("pierwsze 10 bajtow pliku image.png:", data)  # wyswietla dane binarne
print("------------------")

