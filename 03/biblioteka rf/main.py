from typing import Dict
import json
import os

class Ksiazka:  #Reprezentuje pojedynczą książkę w bibliotece.
    def __init__(self, tytul: str, autor: str, kategoria: str,
                 liczba_stron: int, rok_wydania: int):
        self.tytul = tytul
        self.autor = autor
        self.kategoria = kategoria
        self.liczba_stron = liczba_stron
        self.rok_wydania = rok_wydania

    def to_dict(self) -> Dict: #Zamienia obiekt na słownik (do zapisu w JSON).
        return {
            "tytul": self.tytul,
            "autor": self.autor,
            "kategoria": self.kategoria,
            "liczba_stron": self.liczba_stron,
            "rok_wydania": self.rok_wydania
        }

    def __str__(self) -> str:
        return f'"{self.tytul}" — {self.autor} ({self.rok_wydania})'

class Biblioteka:
    # Ścieżka do pliku względem katalogu projektu (data/biblioteka.json)
    #
    #PLIK = os.path.join(os.path.dirname(__file__), '..', 'data', 'biblioteka.json')

    ilosc = 0   # atrybut klasy – liczba książek

    def __init__(self, plik = "biblioteka.json"):
        self.plik = plik
        self._wczytaj_baze()

    def _wczytaj_baze(self) -> None:
        #Wczytuje stan biblioteki z pliku JSON. Metoda wewnętrzna.
        try:
            with open(self.plik, 'r', encoding='utf-8') as f:
                self.ksiazki = json.load(f)
        except FileNotFoundError:
            self.ksiazki = []
        Biblioteka.ilosc = len(self.ksiazki)

    def _zapisz_baze(self) -> None:
        #Zapisuje aktualny stan biblioteki do pliku JSON. Metoda wewnętrzna.
        #os.makedirs(os.path.dirname(self.PLIK), exist_ok=True)
        with open(self.plik, 'w', encoding='utf-8') as f:
            json.dump(self.ksiazki, f, indent=4)

    def czy_istnieje_tytul(self, tytul: str) -> bool:
        #Sprawdza, czy książka o podanym tytule już istnieje w bibliotece.
        return any(k['tytul'] == tytul for k in self.ksiazki)

    def dodaj_ksiazke(self, ksiazka: Ksiazka) -> bool:
        #Dodaje książkę do biblioteki.
        #Zwraca True jeśli dodano, False jeśli tytuł już istnieje.

        #ks_dict = ksiazka.__dict__
        ks_dict = ksiazka.to_dict()
        if self.czy_istnieje_tytul(ks_dict['tytul']):
            return False
        self.ksiazki.append(ks_dict)
        Biblioteka.ilosc += 1
        self._zapisz_baze()
        return True

    def usun_ksiazke(self, tytul: str) -> bool:
        #Usuwa książkę o podanym tytule.
        #Zwraca True jeśli usunięto, False jeśli nie znaleziono.

        nowa_lista = [k for k in self.ksiazki if k['tytul'] != tytul]
        if len(nowa_lista) == len(self.ksiazki):
            return False
        self.ksiazki = nowa_lista
        Biblioteka.ilosc -= 1
        self._zapisz_baze()
        return True

    def ile_ksiazek(self) -> int:
        #Zwraca aktualną liczbę książek w bibliotece.
        return Biblioteka.ilosc

def dodaj_i_informuj(biblioteka: Biblioteka, ksiazka: Ksiazka) -> None:
    #Pomocnicza funkcja — dodaje książkę i wypisuje wynik.
    if biblioteka.dodaj_ksiazke(ksiazka):
        print(f"Dodano: {ksiazka}")
    else:
        print(f"Tytuł już istnieje w bibliotece: '{ksiazka.tytul}'")


def usun_i_informuj(biblioteka: Biblioteka, tytul: str) -> None:
    #Pomocnicza funkcja — usuwa książkę i wypisuje wynik.
    if biblioteka.usun_ksiazke(tytul):
        print(f"Usunięto książkę: '{tytul}'")
    else:
        print(f"Nie znaleziono książki: '{tytul}'")

def nowa_ksiazka() -> Ksiazka:
    #Pobiera dane książki i tworzy obiekt Ksiazka.
    tytul = input('Podaj tytuł książki:')
    autor = input('Podaj autora książki:')
    kategoria = input('Podaj kategorię książki:')
    liczba_stron = int(input('Podaj liczbę stron:'))
    rok_wydania = int(input('Podaj rok wydania:'))
    return Ksiazka(tytul, autor,kategoria, liczba_stron, rok_wydania)

def wyswietl_liste(biblioteka: Biblioteka) -> None:
    #Wyświetla wszystkie książki w bibliotece.
    print(f"\n--- Lista książek ({biblioteka.ile_ksiazek()} pozycji) ---")
    if biblioteka.ile_ksiazek() == 0:
        print("Biblioteka jest pusta.")
        return
    for i, k in enumerate(biblioteka.ksiazki, start=1):
        print(f"  {i}. \"{k['tytul']}\" — {k['autor']} "
              f"({k['rok_wydania']}) | {k['kategoria']} | {k['liczba_stron']} str.")

if __name__ == "__main__":
    b = Biblioteka()

    k1 = Ksiazka("Hobbit", "J.R.R. Tolkien", "fantasy", 300, 1937)
    k2 = Ksiazka("Python 101", "M. Driscoll", "informatyka", 250, 2014)
    k3 = Ksiazka("Hobbit", "J.R.R. Tolkien", "fantasy", 300, 1937)  # duplikat

    dodaj_i_informuj(b, k1)    # Dodano: "Hobbit" — J.R.R. Tolkien (1937)
    dodaj_i_informuj(b, k2)    # Dodano: "Python 101" — M. Driscoll (2014)
    dodaj_i_informuj(b, k3)    # Tytuł już istnieje w bibliotece: 'Hobbit'

    print(f"\nLiczba książek: {b.ile_ksiazek()}")   # 2

    #usun_i_informuj(b, "Hobbit")        # Usunięto książkę: 'Hobbit'
    usun_i_informuj(b, "Nieistniejąca") # Nie znaleziono książki: 'Nieistniejąca'

    print(f"\nLiczba książek: {b.ile_ksiazek()}")   # 1

    while True:
        opcja = int(input("podaj opcję: \n 1 - lista książek; \n 2 - dodaj książkę; \n 3 - Usuń książkę; \n 0 - koniec \n"))
        if opcja == 1:
            wyswietl_liste(b)
        elif opcja == 2:
            dodaj_i_informuj(b, nowa_ksiazka())
        elif opcja == 3:
            tytul = input('Podaj tytuł książki:')
            usun_i_informuj(b, tytul)
        elif opcja == 0:
            print('Cześć, pa, pa')
            break
        else:
            print('Podałeś złą opcję!')