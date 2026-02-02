import os
import json


if os.path.exists("dane_wyjsciowe.txt"):
    os.remove("dane_wyjsciowe.txt")

try:
    with open("oszczep.txt", "r") as plik:
        dane = plik.read().splitlines()
        for linia in dane:
            zawodnik, wyniki = linia.split(":")
            tabWyniki = wyniki.split()
            for i in range(len(tabWyniki)):
                tabWyniki[i] = float(tabWyniki[i])
            tabWyniki.sort()
            najlepszy = tabWyniki[-1]
            zawodnik_w = f"{zawodnik}: {najlepszy}\n"
            with open(f"dane_wyjsciowe.txt", "a") as plik_txt:
                plik_txt.write(zawodnik_w)
    print("stworzono plik 'dane_wyjsciowe.txt'")
except FileNotFoundError:
    print('nie znaleziono pliku "oszczep.txt"')

try:
    with open("oszczep.json", "r") as plik_json:
        dane_json = json.load(plik_json)
        lista_wynikow = []
        for zawodnik in dane_json:
            nazwisko = zawodnik["zawodnik"]
            wyniki = zawodnik["rzuty"]
            wyniki.sort()
            najlepszy = wyniki[-1]

            zawodnik_j = {"zawodnik": nazwisko, "najdluzszy_rzut": najlepszy}
            lista_wynikow.append(zawodnik_j)

    with open("dane_wyjsciowe.json", "w") as plik_jsonw:
        json.dump(lista_wynikow, plik_jsonw, indent=4)
        print("stworzono plik 'dane_wyjsciowe.json'")

except FileNotFoundError:
    print('nie znaleziono pliku "oszczep.json"')



























