# Generated from: lekcja_11-sortowanie.ipynb
# Converted at: 2026-04-13T06:03:09.584Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # LEKCJA 11 — Algorytmy na listach
# ## Sortowanie
# 
# ---
# 
# ### Co to jest sortowanie?
# 
# Sortowanie to ułożenie elementów listy w określonej kolejności - najczęściej od najmniejszego do największego (rosnąco) albo odwrotnie (malejąco).
# 
# Brzmi prosto. Ale jak komputer to robi? Nie może spojrzeć na całą listę naraz i od razu ją ułożyć - musi porównywać elementy **parami**, jeden po drugim.
# 
# W tej lekcji poznasz **trzy klasyczne algorytmy sortowania**, zrozumiesz jak działają krok po kroku, a na koniec porównasz je z wbudowaną funkcją Pythona.
# 
# 
# ### Zanim zaczniesz - pomocnicza funkcja
# 
# Uruchom poniższą komórkę. Definiuje ona funkcję `pokaz_liste`, której można używać w całym notatniku do czytelnego wyświetlania list.


def pokaz_liste(lista, etykieta="Lista", podswietl=None):
    """
    Wyświetla listę w czytelny sposób.
    podswietl: indeks elementu do wyróżnienia (opcjonalnie)
    """
    print(f"{etykieta}:")
    wynik = ""
    for i, el in enumerate(lista):
        if podswietl is not None and i in (podswietl if isinstance(podswietl, (list, tuple)) else [podswietl]):
            wynik += f" [{el}]"
        else:
            wynik += f"  {el} "
    print(wynik)
    print()


# Test
przyklad = [64, 34, 25, 12, 22, 11, 90]
pokaz_liste(przyklad, "Przykładowa lista")
pokaz_liste(przyklad, "Z wyróżnionym elementem", podswietl=[0, 1])
print(" Funkcja pomocnicza gotowa!")

# ---
# ---
# 
# # 1. Sortowanie bąbelkowe
# ## *(ang. Bubble Sort)*
# 
# ---
# 
# ### Jak to działa?
# 
# Wyobraź sobie, że stoisz przed tablicą z numerami i możesz porównywać tylko **dwa sąsiednie** elementy na raz.
# 
# Zasada jest prosta:
# > **Jeśli lewy element jest większy od prawego - zamień je miejscami.**
# 
# Przechodzisz tak przez całą listę od początku do końca. Po jednym takim przejściu **największy element trafia na koniec** - jak bąbel wypływający na powierzchnię wody.
# 
# Powtarzasz to tyle razy, ile jest elementów.
# 
# ---
# 
# ### Przykład krok po kroku
# 
# Lista: `[5, 3, 8, 1, 4]`
# 
# **Przejście 1:**
# ```
# [5, 3, 8, 1, 4]  ->  porównaj 5 i 3  ->  zamień  ->  [3, 5, 8, 1, 4]
# [3, 5, 8, 1, 4]  ->  porównaj 5 i 8  ->  OK       ->  [3, 5, 8, 1, 4]
# [3, 5, 8, 1, 4]  ->  porównaj 8 i 1  ->  zamień  ->  [3, 5, 1, 8, 4]
# [3, 5, 1, 8, 4]  ->  porównaj 8 i 4  ->  zamień  ->  [3, 5, 1, 4, 8] <- 8 na miejscu!
# ```
# 
# **Przejście 2:**
# ```
# [3, 5, 1, 4, 8]  ->  ...  ->  [3, 1, 4, 5, 8] <- 5 na miejscu!
# ```
# 
# I tak dalej, aż lista jest posortowana.


# ============================================================
# SORTOWANIE BĄBELKOWE - wersja z dokładnym wyświetlaniem kroków
# ============================================================

def sortowanie_babelkowe_z_krokami(lista):
    """
    Sortowanie bąbelkowe z wyświetlaniem każdego kroku.
    Dzięki temu zobaczysz dokładnie co się dzieje w każdej chwili.
    """
    n = len(lista)
    lista = lista[:]      # kopia, żeby nie niszczyć oryginału
    liczba_zamian = 0
    liczba_porownań = 0

    print(f"Startowa lista: {lista}")
    print("=" * 50)

    for i in range(n):                      # i = numer przejścia
        print(f"\n--- Przejście {i + 1} ---")
        zamieniono_cos = False

        for j in range(0, n - i - 1):       # j = pozycja porównania
            liczba_porownań += 1

            # Porównujemy elementy na pozycjach j i j+1
            if lista[j] > lista[j + 1]:
                # Zamiana!
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                liczba_zamian += 1
                zamieniono_cos = True
                print(f"  Porównanie {lista[j+1]} > {lista[j]}: ZAMIANA -> {lista}")
            else:
                print(f"  Porównanie {lista[j]} ≤ {lista[j+1]}: bez zmian  -> {lista}")

        # Jeśli w całym przejściu nie było żadnej zamiany — lista już posortowana!
        if not zamieniono_cos:
            print("   Brak zamian - lista posortowana. Przerywam wcześniej.")
            break

    print("\n" + "=" * 50)
    print(f"Wynik:            {lista}")
    print(f"Liczba porównań:  {liczba_porownań}")
    print(f"Liczba zamian:    {liczba_zamian}")
    return lista


wynik = sortowanie_babelkowe_z_krokami([5, 3, 8, 1, 4])

# ============================================================
# SORTOWANIE BĄBELKOWE - czysta implementacja do zapamiętania
# ============================================================

def sortowanie_babelkowe(lista):
    """
    Sortowanie bąbelkowe - czysta wersja bez wypisywania kroków.
    To jest kod, który powinieneś umieć napisać samodzielnie.
    """
    n = len(lista)
    lista = lista[:]      # kopia oryginału

    for i in range(n):                    # powtarzaj n razy
        for j in range(0, n - i - 1):     # przesuń bąbel do przodu
            if lista[j] > lista[j + 1]:   # jeśli zły porządek
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # zamień

    return lista


# Test na różnych listach
print("Test 1 - liczby:",        sortowanie_babelkowe([64, 34, 25, 12, 22, 11, 90]))
print("Test 2 - już posortowana:", sortowanie_babelkowe([1, 2, 3, 4, 5]))
print("Test 3 - odwrócona:",      sortowanie_babelkowe([5, 4, 3, 2, 1]))
print("Test 4 - jeden element:",   sortowanie_babelkowe([42]))
print("Test 5 - duplikaty:",       sortowanie_babelkowe([3, 1, 3, 2, 1]))

# ### Optymalizacja bąbelkowego
# 
# Zauważ jeden problem w podstawowej wersji: nawet jeśli lista jest już posortowana po 2 przejściach, algorytm dalej sprawdza kolejne przejścia niepotrzebnie.
# 
# Rozwiązanie: **flaga `zamieniono_cos`**. Jeśli podczas całego przejścia nie było ani jednej zamiany, lista jest już posortowana i możemy przerwać.


# WERSJA ULEPSZONA - z wczesnym wyjściem

def sortowanie_babelkowe_v2(lista):
    """
    Ulepszone sortowanie bąbelkowe.
    Zatrzymuje się gdy lista jest już posortowana.
    """
    n = len(lista)
    lista = lista[:]

    for i in range(n):
        zamieniono_cos = False                # flaga - czy coś zamieniliśmy?

        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                zamieniono_cos = True         # tak, zamieniliśmy

        if not zamieniono_cos:                # jeśli żadnej zamiany
            break                             # przerywamy - gotowe!

    return lista


# Porównaj ile przejść robi każda wersja na już posortowanej liście
print("Wynik ulepszonej wersji:", sortowanie_babelkowe_v2([1, 2, 3, 4, 5, 6, 7]))
print("Wynik ulepszonej wersji:", sortowanie_babelkowe_v2([5, 3, 8, 1, 4]))

# ---
# 
# ### Ćwiczenie 1.1 - Zrozumienie działania
# 
# Prześledź ręcznie (na papierze lub w komentarzu) jak bąbelkowe posortuje listę `[9, 2, 7, 1]`.
# 
# Zapisz co się dzieje w każdym przejściu, a potem sprawdź swój wynik uruchamiając `sortowanie_babelkowe_z_krokami([9, 2, 7, 1])`.


#  ĆWICZENIE 1.1
# Sprawdź swoje ręczne śledzenie algorytmu

sortowanie_babelkowe_z_krokami([9, 2, 7, 1])

# ---
# 
# ### Ćwiczenie 1.2 — Modyfikacja algorytmu


# ĆWICZENIE 1.2
# Zmodyfikuj funkcję sortowanie_babelkowe, żeby sortowała malejąco
# (od największego do najmniejszego).
# Wskazówka: zmień tylko JEDEN znak w warunku porównania.

def sortowanie_babelkowe_malejaco(lista):
    n = len(lista)
    lista = lista[:]

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:   # <- zmieniony warunek
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


# Uzupełnij funkcję powyżej i odkomentuj testy:
# print(sortowanie_babelkowe_malejaco([5, 3, 8, 1, 4]))
# Oczekiwany wynik: [8, 5, 4, 3, 1]

# ---
# 
# ### Ćwiczenie 1.3 — Sortowanie słów


# ĆWICZENIE 1.3
# Użyj sortowania bąbelkowego do posortowania listy słów alfabetycznie.
# Python potrafi porównywać napisy tak samo jak liczby (a < b < c ...).

slowa = ["banan", "jabłko", "czereśnia", "agrest", "data", "figa"]

# Wywołaj sortowanie_babelkowe na liście słów i wyświetl wynik.
# Twój kod tutaj:


# ---
# ---
# 
# # 2. Sortowanie przez wybór
# ## *(ang. Selection Sort)*
# 
# ---
# 
# ### Jak to działa?
# 
# Algorytm działa jak porządkowanie kart w ręce:
# 
# 1. Przeglądasz całą listę i **szukasz najmniejszego elementu**.
# 2. Zamieniasz go z pierwszym elementem listy.
# 3. Teraz pierwszy element jest na swoim miejscu - ignorujesz go.
# 4. Powtarzasz od kroku 1 dla reszty listy.
# 
# ---
# 
# ### Różnica względem bąbelkowego
# 
# | | Bąbelkowe | Przez wybór |
# |-|-----------|-------------|
# | Porównuje | Sąsiednie pary | Szuka minimum w całej reszcie |
# | Zamienia | Często (wiele małych zamian) | Rzadko (jedna zamiana na przejście) |
# | Co „odkłada" | Największy na koniec | Najmniejszy na początek |
# 
# ---
# 
# ### Przykład krok po kroku
# 
# Lista: `[64, 25, 12, 22, 11]`
# 
# ```
# Przejście 1: szukamy minimum w [64, 25, 12, 22, 11] -> min = 11 (indeks 4)
#              zamieniamy 64 ↔ 11  ->  [11, 25, 12, 22, 64]
# 
# Przejście 2: szukamy minimum w [25, 12, 22, 64] -> min = 12 (indeks 2)
#              zamieniamy 25 <-> 12  ->  [11, 12, 25, 22, 64]
# 
# Przejście 3: szukamy minimum w [25, 22, 64] -> min = 22 (indeks 3)
#              zamieniamy 25 <-> 22  ->  [11, 12, 22, 25, 64]
# 
# Przejście 4: szukamy minimum w [25, 64] -> min = 25 (indeks 3)
#              bez zamiany  ->  [11, 12, 22, 25, 64]
# ```


# ============================================================
# SORTOWANIE PRZEZ WYBÓR - wersja z krokami
# ============================================================

def sortowanie_wybor_z_krokami(lista):
    n = len(lista)
    lista = lista[:]
    liczba_porownań = 0
    liczba_zamian = 0

    print(f"Startowa lista: {lista}")
    print("=" * 50)

    for i in range(n - 1):
        # Zakładamy, że minimum jest na pozycji i
        indeks_minimum = i
        print(f"\n--- Przejście {i + 1} ---")
        print(f"  Szukam minimum w: {lista[i:]}")

        # Szukamy faktycznego minimum w reszcie listy
        for j in range(i + 1, n):
            liczba_porownań += 1
            if lista[j] < lista[indeks_minimum]:
                indeks_minimum = j

        print(f"  Znalezione minimum: {lista[indeks_minimum]} (indeks {indeks_minimum})")

        # Zamieniamy minimum z pierwszym elementem nieposortowanej części
        if indeks_minimum != i:
            lista[i], lista[indeks_minimum] = lista[indeks_minimum], lista[i]
            liczba_zamian += 1
            print(f"  Zamiana: {lista[indeks_minimum]} <-> {lista[i]}  ->  {lista}")
        else:
            print(f"  Minimum już na miejscu - bez zamiany  ->  {lista}")

        posortowane = lista[:i + 1]
        print(f"  Posortowane: {posortowane} | Do zrobienia: {lista[i + 1:]}")

    print("\n" + "=" * 50)
    print(f"Wynik:            {lista}")
    print(f"Liczba porównań:  {liczba_porownań}")
    print(f"Liczba zamian:    {liczba_zamian}")
    return lista


sortowanie_wybor_z_krokami([64, 25, 12, 22, 11])

# ============================================================
# SORTOWANIE PRZEZ WYBÓR — czysta implementacja
# ============================================================

def sortowanie_wybor(lista):
    """
    Sortowanie przez wybór.
    W każdym przejściu: znajdź minimum w reszcie i wstaw na właściwe miejsce.
    """
    n = len(lista)
    lista = lista[:]

    for i in range(n - 1):              # dla każdej pozycji od lewej
        indeks_minimum = i              # zakładamy: minimum jest tutaj

        for j in range(i + 1, n):       # szukamy mniejszego w reszcie
            if lista[j] < lista[indeks_minimum]:
                indeks_minimum = j      # znaleźliśmy mniejszy

        # Zamień minimum z pozycją i
        lista[i], lista[indeks_minimum] = lista[indeks_minimum], lista[i]

    return lista


print("Test 1:", sortowanie_wybor([64, 25, 12, 22, 11]))
print("Test 2:", sortowanie_wybor([5, 3, 1, 4, 2]))
print("Test 3:", sortowanie_wybor([1]))
print("Test 4:", sortowanie_wybor([3, 3, 1, 1, 2]))

# ### Kluczowa cecha sortowania przez wybór
# 
# Niezależnie od tego jak wygląda lista - czy jest prawie posortowana, losowa czy odwrócona - algorytm **zawsze wykonuje tyle samo porównań**.
# 
# Dla listy długości `n` = zawsze `n*(n-1)/2` porównań.
# 
# To odróżnia go od bąbelkowego (które może skończyć wcześniej) i od wstawiania (które jest szybsze dla prawie posortowanych danych).


# Weryfikacja: Selection Sort zawsze robi tyle samo porównań

def sortowanie_wybor_licz(lista):
    n = len(lista)
    lista = lista[:]
    liczba_porownań = 0

    for i in range(n - 1):
        indeks_minimum = i
        for j in range(i + 1, n):
            liczba_porownań += 1
            if lista[j] < lista[indeks_minimum]:
                indeks_minimum = j
        lista[i], lista[indeks_minimum] = lista[indeks_minimum], lista[i]

    return liczba_porownań


n = 5
oczekiwane = n * (n - 1) // 2
print(f"Dla listy 5 elementów, wzór n*(n-1)/2 = {oczekiwane}")
print()
print(f"Lista losowa:       {sortowanie_wybor_licz([3, 1, 4, 5, 2])} porównań")
print(f"Lista posortowana:  {sortowanie_wybor_licz([1, 2, 3, 4, 5])} porównań")
print(f"Lista odwrócona:    {sortowanie_wybor_licz([5, 4, 3, 2, 1])} porównań")
print()
print("-> Zawsze tyle samo - bez względu na dane wejściowe.")

# ---
# 
# ### Ćwiczenie 2.1 — Śledzenie algorytmu


# ĆWICZENIE 2.1
# Przed uruchomieniem - odpowiedz na pytania:
#
# Lista: [4, 2, 9, 6, 1]
#
# 1. Co będzie elementem listy po 1. przejściu?
# 2. Ile zamian wykona algorytm łącznie?
# 3. Ile porównań wykona algorytm łącznie?
#    (Wskazówka: n*(n-1)/2, n=5)
#
# Odpowiedzi zapisz jako komentarze, potem sprawdź uruchamiając kod:

# 1. Po 1. przejściu: ?
# 2. Liczba zamian: ?
# 3. Liczba porównań: ?

sortowanie_wybor_z_krokami([4, 2, 9, 6, 1])

# ---
# 
# ### Ćwiczenie 2.2 — Sortowanie rekordów


# ĆWICZENIE 2.2
# Masz listę wyników uczniów z testu (liczba punktów).
# Użyj sortowania przez wybór, żeby ułożyć je od najgorszego do najlepszego.
#
# Następnie wypisz:
# - najsłabszy wynik
# - najlepszy wynik
# - medianę (środkowy element)

wyniki_testu = [78, 45, 92, 61, 88, 34, 75, 90, 52, 67]

# Twój kod tutaj:
# posortowane = sortowanie_wybor(wyniki_testu)
# print("Posortowane wyniki:", posortowane)
# print("Najsłabszy:", ?)
# print("Najlepszy:", ?)
# print("Mediana:", ?)

# ---
# ---
# 
# # 3. Sortowanie przez wstawianie
# ## *(ang. Insertion Sort)*
# 
# ---
# 
# ### Jak to działa?
# 
# Pomyśl o układaniu kart w ręce podczas gry:
# - Bierzesz kolejną kartę z talii.
# - Porównujesz ją z kartami, które już trzymasz (a które są już ułożone).
# - Wstawiasz ją we właściwe miejsce.
# 
# Algorytm **buduje posortowaną listę od lewej strony**, wstawiając kolejne elementy w odpowiednie miejsce.
# 
# ---
# 
# ### Przykład krok po kroku
# 
# Lista: `[5, 2, 4, 6, 1, 3]`
# 
# ```
# Start:   [5] | [2, 4, 6, 1, 3]   (1 element jest „posortowany")
# 
# Krok 1:  Bierzemy 2 -> wstawiamy przed 5
#          [2, 5] | [4, 6, 1, 3]
# 
# Krok 2:  Bierzemy 4 -> 4 > 2, ale 4 < 5, wstawiamy między 2 i 5
#          [2, 4, 5] | [6, 1, 3]
# 
# Krok 3:  Bierzemy 6 -> 6 > 5, nie ruszamy
#          [2, 4, 5, 6] | [1, 3]
# 
# Krok 4:  Bierzemy 1 -> mniejszy od wszystkich, wstawiamy na początku
#          [1, 2, 4, 5, 6] | [3]
# 
# Krok 5:  Bierzemy 3 -> 3 > 2, ale 3 < 4, wstawiamy
#          [1, 2, 3, 4, 5, 6]
# ```


# ============================================================
# SORTOWANIE PRZEZ WSTAWIANIE - wersja z krokami
# ============================================================

def sortowanie_wstawianie_z_krokami(lista):
    n = len(lista)
    lista = lista[:]
    liczba_porownań = 0
    liczba_przesuniec = 0

    print(f"Startowa lista: {lista}")
    print("=" * 50)

    for i in range(1, n):               # zaczynamy od drugiego elementu
        klucz = lista[i]                # element do wstawienia
        j = i - 1                       # j wskazuje na ostatni posortowany element

        print(f"\n--- Krok {i} ---")
        print(f"  Wstawiam: {klucz}")
        print(f"  Posortowane: {lista[:i]} | Reszta: {lista[i:]}")

        # Przesuń elementy większe od klucza o jedno miejsce w prawo
        while j >= 0 and lista[j] > klucz:
            liczba_porownań += 1
            liczba_przesuniec += 1
            lista[j + 1] = lista[j]     # przesuń element w prawo
            print(f"    {lista[j]} > {klucz}: przesuwam {lista[j]} w prawo → {lista}")
            j -= 1

        if j >= 0:
            liczba_porownań += 1        # ostatnie porównanie (warunek nie był spełniony)

        lista[j + 1] = klucz            # wstaw klucz na właściwe miejsce
        print(f"  Wstawiam {klucz} na pozycję {j + 1}  ->  {lista}")

    print("\n" + "=" * 50)
    print(f"Wynik:              {lista}")
    print(f"Liczba porównań:    {liczba_porownań}")
    print(f"Liczba przesunięć:  {liczba_przesuniec}")
    return lista


sortowanie_wstawianie_z_krokami([5, 2, 4, 6, 1, 3])

# ============================================================
# SORTOWANIE PRZEZ WSTAWIANIE - czysta implementacja
# ============================================================

def sortowanie_wstawianie(lista):
    """
    Sortowanie przez wstawianie.
    Buduje posortowaną listę od lewej, wstawiając kolejne elementy.
    """
    lista = lista[:]

    for i in range(1, len(lista)):    # dla każdego elementu (poza pierwszym)
        klucz = lista[i]              # zapamiętaj element do wstawienia
        j = i - 1                     # zacznij od elementu po lewej

        # Przesuń elementy większe od klucza o jedno miejsce w prawo
        while j >= 0 and lista[j] > klucz:
            lista[j + 1] = lista[j]   # przesuń w prawo
            j -= 1

        lista[j + 1] = klucz          # wstaw na właściwe miejsce

    return lista


print("Test 1:", sortowanie_wstawianie([5, 2, 4, 6, 1, 3]))
print("Test 2:", sortowanie_wstawianie([1, 2, 3, 4, 5]))    # już posortowana
print("Test 3:", sortowanie_wstawianie([5, 4, 3, 2, 1]))    # odwrócona
print("Test 4:", sortowanie_wstawianie([3, 1, 1, 2, 3]))    # duplikaty

# ### Dlaczego wstawianie jest lepsze dla prawie posortowanych list?
# 
# Gdy lista jest prawie posortowana, pętla `while` wewnętrzna prawie nigdy nie wykonuje żadnych przesunięć - element od razu trafia na właściwe miejsce. Algorytm staje się wtedy prawie liniowy.
# 
# Bąbelkowe i przez wybór nie korzystają z tego - zawsze robią tyle samo pracy.


# Demonstracja: wstawianie vs bąbelkowe na prawie posortowanej liście

def sortowanie_babelkowe_licz(lista):
    n = len(lista)
    lista = lista[:]
    licznik = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            licznik += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return licznik

def sortowanie_wstawianie_licz(lista):
    lista = lista[:]
    licznik = 0
    for i in range(1, len(lista)):
        klucz = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > klucz:
            licznik += 1
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = klucz
    return licznik


# Lista prawie posortowana - tylko kilka elementów nie na miejscu
prawie_posortowana = [1, 2, 3, 5, 4, 6, 7, 8, 10, 9]  # zamienione 2 pary
losowa = [7, 2, 9, 1, 5, 3, 8, 6, 4, 10]

print("=== Prawie posortowana lista ===")
print(f"  Bąbelkowe:  {sortowanie_babelkowe_licz(prawie_posortowana)} operacji")
print(f"  Wstawianie: {sortowanie_wstawianie_licz(prawie_posortowana)} operacji")

print("\n=== Lista losowa ===")
print(f"  Bąbelkowe:  {sortowanie_babelkowe_licz(losowa)} operacji")
print(f"  Wstawianie: {sortowanie_wstawianie_licz(losowa)} operacji")

# ### Ćwiczenie 3.1 — Śledzenie wstawiania


# ĆWICZENIE 3.1
# Przed uruchomieniem prześlij ręcznie dla: [3, 8, 1, 7, 2]
#
# Uzupełnij tabelę (na papierze lub w komentarzu):
# Krok | Wstawiamy | Posortowana część | Cała lista
#  1   |     8     |   [3, 8]          | ...
#  2   |     1     |   [1, 3, 8]       | ...
#  3   |     ?     |   ?               | ...
#  4   |     ?     |   ?               | ...
#
# Sprawdź:
sortowanie_wstawianie_z_krokami([3, 8, 1, 7, 2])

# ---
# 
# ### Ćwiczenie 3.2 - Litery i słowa


# ĆWICZENIE 3.2
# Posortuj wstawianiem następujące listy:
#
# a) litery z imienia (każda litera to osobny element)
# b) temperatury z tygodnia
#
# Wypisz wyniki.

imie = ['P', 'y', 't', 'h', 'o', 'n']
temperatury = [22.5, 18.0, 25.3, 19.8, 23.1, 17.5, 20.0]

# a) Posortuj litery:
# ...

# b) Posortuj temperatury:
# ...


# ---
# 
# ### Ćwiczenie 3.3 — Napisz od zera


# ĆWICZENIE 3.3 - trudniejsze
# Napisz sortowanie przez wstawianie od zera, korzystając TYLKO z opisu słownego
# (bez podglądania implementacji wyżej).
#
# Opis:
# 1. Iteruj przez listę zaczynając od indeksu 1.
# 2. Zapamiętaj bieżący element jako 'klucz'.
# 3. Cofaj się w lewo, przesuwając elementy większe od klucza o 1 w prawo.
# 4. Wstaw klucz na zwolnione miejsce.

def moje_sortowanie_wstawianie(lista):
    # Twój kod tutaj
    pass


# Test - powinno dać [1, 2, 3, 4, 5]
print(moje_sortowanie_wstawianie([3, 1, 5, 2, 4]))

# ---
# ---
# 
# # 4. Porównanie z `.sort()` i `sorted()`
# 
# ---
# 
# Python ma wbudowane narzędzia do sortowania, które są **znacznie szybsze** od algorytmów, które właśnie poznałeś. Używają algorytmu **Timsort** - hybrydy sortowania przez scalanie i wstawianie, zaprojektowanej przez Tima Petersa w 2002 roku specjalnie dla Pythona.
# 
# ### Dwie metody:
# 
# | | `lista.sort()` | `sorted(lista)` |
# |-|----------------|------------------|
# | Działa na | liście | dowolnym iterowalnym |
# | Zwraca | `None` (modyfikuje listę) | nową posortowaną listę |
# | Oryginał | zostaje zmieniony | nie jest zmieniany |


# ============================================================
# sort() vs sorted() - różnice
# ============================================================

liczby = [5, 2, 8, 1, 9, 3]

# sorted() - zwraca NOWĄ listę, oryginał bez zmian
posortowana = sorted(liczby)
print(f"sorted() zwróciło: {posortowana}")
print(f"Oryginał po sorted(): {liczby}")  # NIE zmieniony

print()

# sort() - modyfikuje ORYGINAŁ, zwraca None
wynik = liczby.sort()
print(f"sort() zwróciło: {wynik}")          # None!
print(f"Oryginał po sort(): {liczby}")      # zmieniony

print()
print("  Częsty błąd: posortowana = lista.sort()")
print("  Wynik to None, bo sort() nic nie zwraca!")

# ============================================================
# Parametry: reverse i key
# ============================================================

liczby = [5, 2, 8, 1, 9, 3]

# Sortowanie malejące
print("Malejąco:", sorted(liczby, reverse=True))

# Sortowanie po kluczu - tu: po wartości bezwzględnej
z_minusami = [-3, 1, -7, 4, -2, 6]
print("Według |x|:", sorted(z_minusami, key=abs))

print()

# Sortowanie napisów - domyślnie: alfabetycznie
imiona = ["Zofia", "Adam", "Maria", "Bartek", "anna"]
print("Alfabetycznie:     ", sorted(imiona))
print("Bez rozróżniania:  ", sorted(imiona, key=str.lower))  # ignoruje duże litery

print()

# Sortowanie po długości słowa
slowa = ["python", "kot", "programowanie", "las", "szkoła"]
print("Według długości:   ", sorted(slowa, key=len))

# ============================================================
# Sortowanie złożonych struktur - lista słowników
# ============================================================

# Wyniki uczniów z kilku przedmiotów
uczniowie = [
    {"imie": "Anna",    "srednia": 4.8, "klasa": "3B"},
    {"imie": "Bartek",  "srednia": 3.2, "klasa": "3A"},
    {"imie": "Celina",  "srednia": 4.2, "klasa": "3B"},
    {"imie": "Damian",  "srednia": 3.8, "klasa": "3A"},
    {"imie": "Ela",     "srednia": 4.8, "klasa": "3A"},
]

# Sortowanie po średniej (rosnąco)
print("=== Ranking według średniej ===")
ranking = sorted(uczniowie, key=lambda u: u["srednia"], reverse=True)
for miejsce, uczen in enumerate(ranking, 1):
    print(f"  {miejsce}. {uczen['imie']:10} | klasa {uczen['klasa']} | śr. {uczen['srednia']}")

print()

# Sortowanie po klasie, a w ramach klasy po nazwisku
print("=== Posortowani wg klasy, potem imienia ===")
wg_klasy = sorted(uczniowie, key=lambda u: (u["klasa"], u["imie"]))
for uczen in wg_klasy:
    print(f"  {uczen['klasa']} | {uczen['imie']:10} | śr. {uczen['srednia']}")

# ---
# 
# ### Ćwiczenie 4.1 — Praktyczne użycie sorted()


# ĆWICZENIE 4.1
# Masz listę słów. Wykonaj poniższe sortowania używając sorted() z parametrem key:

slowa = ["komputer", "pies", "rower", "słoń", "abecadło", "byk", "żyrafa"]

# a) Posortuj słowa według ich DŁUGOŚCI (od najkrótszego)
# b) Posortuj słowa według OSTATNIEJ LITERY
#    Wskazówka: last = lambda s: s[-1]
# c) Posortuj słowa malejąco według DŁUGOŚCI (od najdłuższego)

# a)
# ...

# b)
# ...

# c)
# ...

# ---
# 
# ### Ćwiczenie 4.2 — Ranking gier


# ĆWICZENIE 4.2
# Ranking graczy. Posortuj listę według punktów malejąco.
# Jeśli punkty są równe, wyżej jest gracz z mniejszą liczbą śmierci.
# Wypisz ranking z miejscami.

gracze = [
    {"nick": "Shadow99",  "punkty": 1540, "smierci": 12},
    {"nick": "ProGamer",  "punkty": 2100, "smierci": 8},
    {"nick": "KingSlayer","punkty": 1540, "smierci": 7},
    {"nick": "Noob2024",  "punkty": 890,  "smierci": 25},
    {"nick": "EliteX",    "punkty": 2100, "smierci": 5},
]

# Wskazówka: key=lambda g: (g["punkty"], -g["smierci"])
# Minus przy śmierciach, bo chcemy MNIEJ śmierci = wyżej, a sortujemy rosnąco.

# Twój kod tutaj:


# ---
# ---
# 
# # 5. Wydajność algorytmów
# 
# ---
# 
# ### Notacja O — jak mierzymy "szybkość" algorytmu?
# 
# Zamiast mierzyć czas w sekundach (który zależy od komputera), opisujemy **jak rośnie liczba operacji** gdy rośnie liczba elementów `n`.
# 
# Piszemy to jako **O(f(n))** — czytamy: "algorytm jest rzędu f(n)".
# 
# | Notacja | Nazwa | Co to znaczy |
# |---------|-------|---------------|
# | O(1) | stały | Czas nie zależy od rozmiaru danych |
# | O(n) | liniowy | 2x więcej danych = 2x więcej pracy |
# | O(n²) | kwadratowy | 2x więcej danych = 4x więcej pracy |
# | O(n log n) | liniowo-logarytmiczny | Trochę gorzej niż liniowy |
# 
# ---
# 
# ### Nasze algorytmy
# 
# | Algorytm | Najlepszy | Przeciętny | Najgorszy |
# |----------|-----------|------------|-----------|
# | Bąbelkowe | O(n) | O(n²) | O(n²) |
# | Przez wybór | O(n²) | O(n²) | O(n²) |
# | Wstawianie | O(n) | O(n²) | O(n²) |
# | `.sort()` (Timsort) | O(n) | O(n log n) | O(n log n) |
# 
# Wszystkie trzy "ręczne" algorytmy są O(n²) w typowym przypadku — to znaczy **wolne dla dużych danych**.


# ============================================================
# ZMIERZMY TO W PRAKTYCE
# ============================================================

import time
import random

def zmierz_czas(funkcja, lista, nazwa):
    """Mierzy czas sortowania i zwraca wynik."""
    kopia = lista[:]
    start = time.perf_counter()
    funkcja(kopia)
    koniec = time.perf_counter()
    czas_ms = (koniec - start) * 1000
    print(f"  {nazwa:30}: {czas_ms:8.3f} ms")
    return czas_ms


# Generujemy losowe listy różnych rozmiarów
rozmiary = [100, 500, 1000, 3000]

for n in rozmiary:
    dane = [random.randint(1, 10000) for _ in range(n)]
    print(f"\n=== Lista {n} elementów ===")

    zmierz_czas(sortowanie_babelkowe,   dane, "Bąbelkowe")
    zmierz_czas(sortowanie_wybor,       dane, "Przez wybór")
    zmierz_czas(sortowanie_wstawianie,  dane, "Wstawianie")
    zmierz_czas(sorted,                 dane, "sorted() — Python")

# ============================================================
# Wykresy porównawcze - wizualizacja wzrostu
# ============================================================

import time
import random

def zmierz_ms(funkcja, lista):
    kopia = lista[:]
    start = time.perf_counter()
    funkcja(kopia)
    return (time.perf_counter() - start) * 1000


rozmiary = [100, 200, 400, 600, 800, 1000, 1500, 2000]
czasy_babelkowe  = []
czasy_wybor      = []
czasy_wstawianie = []
czasy_python     = []

for n in rozmiary:
    dane = [random.randint(1, 10000) for _ in range(n)]
    czasy_babelkowe.append(zmierz_ms(sortowanie_babelkowe, dane))
    czasy_wybor.append(zmierz_ms(sortowanie_wybor, dane))
    czasy_wstawianie.append(zmierz_ms(sortowanie_wstawianie, dane))
    czasy_python.append(zmierz_ms(sorted, dane))


# Prosty wykres tekstowy (bez bibliotek)
print("\n=== Czasy sortowania (ms) ===")
print(f"{'n':>6} | {'Bąbelk.':>10} | {'Wybór':>10} | {'Wstaw.':>10} | {'Python':>10}")
print("-" * 58)
for i, n in enumerate(rozmiary):
    print(f"{n:>6} | {czasy_babelkowe[i]:>10.2f} | {czasy_wybor[i]:>10.2f} | {czasy_wstawianie[i]:>10.2f} | {czasy_python[i]:>10.4f}")

print("\n→ Zauważ: gdy n rośnie 2x, czas O(n²) rośnie ~4x")
print("→ Python's sorted() jest tak szybki, że trudno go zmierzyć")

# ============================================================
# Wykres z matplotlib (jeśli masz zainstalowane)
# ============================================================

try:
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Lewy wykres: wszystkie algorytmy
    ax1.plot(rozmiary, czasy_babelkowe,  'o-', label='Bąbelkowe',     color='#e74c3c', linewidth=2)
    ax1.plot(rozmiary, czasy_wybor,      's-', label='Przez wybór',   color='#e67e22', linewidth=2)
    ax1.plot(rozmiary, czasy_wstawianie, '^-', label='Wstawianie',    color='#3498db', linewidth=2)
    ax1.plot(rozmiary, czasy_python,     'D-', label='sorted() — Python', color='#2ecc71', linewidth=2)
    ax1.set_title('Porównanie czasu sortowania', fontsize=13)
    ax1.set_xlabel('Liczba elementów (n)')
    ax1.set_ylabel('Czas (ms)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Prawy wykres: tylko Python's sorted (żeby było widać)
    ax2.plot(rozmiary, czasy_python, 'D-', color='#2ecc71', linewidth=2)
    ax2.set_title('sorted() - Python (Timsort)', fontsize=13)
    ax2.set_xlabel('Liczba elementów (n)')
    ax2.set_ylabel('Czas (ms)')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

except ImportError:
    print("matplotlib niedostępne. Zainstaluj: !pip install matplotlib")

# ============================================================
# Porównanie na różnych typach danych wejściowych
# ============================================================

import random

n = 1000

# Różne typy list
losowa        = [random.randint(1, 10000) for _ in range(n)]
posortowana   = list(range(n))
odwrocona     = list(range(n, 0, -1))
prawie        = list(range(n))
# Zamień 5 losowych par
for _ in range(5):
    a, b = random.sample(range(n), 2)
    prawie[a], prawie[b] = prawie[b], prawie[a]

typy = [
    ("Losowa",          losowa),
    ("Posortowana",     posortowana),
    ("Odwrócona",       odwrocona),
    ("Prawie posort.",  prawie),
]

print(f"{'Typ danych':20} | {'Bąbelkowe':>12} | {'Wybór':>12} | {'Wstawianie':>12}")
print("-" * 65)

for nazwa, dane in typy:
    t_b = zmierz_ms(sortowanie_babelkowe,  dane)
    t_w = zmierz_ms(sortowanie_wybor,      dane)
    t_i = zmierz_ms(sortowanie_wstawianie, dane)
    print(f"{nazwa:20} | {t_b:10.2f} ms | {t_w:10.2f} ms | {t_i:10.2f} ms")

print()
print("Obserwacje:")
print("-> Bąbelkowe + wstawianie są szybkie na posortowanej liście (O(n))")
print("-> Przez wybór zawsze tyle samo (O(n²)) - bez względu na dane")
print("-> Wstawianie jest najszybsze na 'prawie posortowanej' liście")

# ---
# 
# ### Ćwiczenie 5.1 — Obliczenia O(n²)


# ĆWICZENIE 5.1
# Oblicz ile operacji wykona algorytm O(n²) dla różnych rozmiarów danych.
# Uzupełnij tabelę.

print(f"{'n':>10} | {'n² (operacji)':>20} | {'Wzrost względem n=100':>25}")
print("-" * 62)

baza = 100 ** 2
for n in [100, 500, 1000, 5000, 10000, 100000]:
    operacje = n ** 2
    wzrost = operacje / baza
    print(f"{n:>10} | {operacje:>20,} | {wzrost:>23.0f}x")

print()
print("-> Lista 1000 elementów to 100x więcej pracy niż lista 100 elementów!")
print("-> Lista 100 000 elementów to 1 000 000x więcej pracy.")
print("   Stąd biorą się sekundy zamiast milisekund.")

# ---
# 
# ### Ćwiczenie 5.2 - Kiedy używać którego algorytmu?


# ĆWICZENIE 5.2 - Pytania do przemyślenia
#
# Dla każdej sytuacji napisz w komentarzu który algorytm wybrałbyś
# i dlaczego. Możesz uruchomić testy, żeby sprawdzić swój wybór.
#
# Sytuacja A:
# Sortujesz listę 10 elementów. Nie zależy ci na wydajności.
# Który algorytm jest najprostszy do napisania?
# Odpowiedź A: ...
#
# Sytuacja B:
# Masz dane z czujników temperatury. Co minutę dostajesz 1 nowy odczyt
# i chcesz zawsze mieć posortowaną listę (prawie posortowana + 1 nowy element).
# Odpowiedź B: ...
#
# Sytuacja C:
# Sortujesz 100 000 rekordów w bazie danych.
# Odpowiedź C: ...
#
# Sytuacja D:
# Piszesz program na mikrokontroler z bardzo małą pamięcią.
# Chcesz algorytm wykonujący jak najmniej zamian w pamięci.
# Odpowiedź D: ...

print("Przemyśl odpowiedzi i zapisz je jako komentarze powyżej.")

# ---
# ---
# 
# # Zadanie podsumowujące — Pełny projekt
# 
# ---
# 
# Napisz program, który:
# 1. Zawiera implementacje wszystkich trzech algorytmów sortowania.
# 2. Wczytuje od użytkownika listę liczb (oddzielonych spacjami).
# 3. Sortuje je każdym algorytmem i wyświetla wyniki.
# 4. Podaje czas sortowania dla każdego algorytmu.
# 5. Wskazuje który był najszybszy.
# 
# Gotowy szkielet poniżej — uzupełnij brakujące fragmenty.


# ============================================================
# ZADANIE PODSUMOWUJĄCE - Kalkulator sortowania
# ============================================================

import time

def kalkulator_sortowania():
    print("=" * 55)
    print(" KALKULATOR SORTOWANIA")
    print("=" * 55)
    print("Wpisz liczby oddzielone spacjami (np: 5 3 8 1 9 2 7):")

    try:
        wejscie = input("> ")
        lista = list(map(int, wejscie.strip().split()))
    except ValueError:
        print(" Błąd: wpisz tylko liczby całkowite oddzielone spacjami.")
        return

    if len(lista) < 2:
        print(" Potrzeba co najmniej 2 elementów.")
        return

    print(f"\nTwoja lista ({len(lista)} elementów): {lista}")
    print()

    # Słownik algorytmów do przetestowania
    algorytmy = {
        "Bąbelkowe":     sortowanie_babelkowe_v2,
        "Przez wybór":   sortowanie_wybor,
        "Wstawianie":    sortowanie_wstawianie,
        "sorted() Python": sorted,
    }

    wyniki = {}

    print(f"{'Algorytm':20} | {'Wynik':35} | {'Czas':>12}")
    print("-" * 75)

    for nazwa, funkcja in algorytmy.items():
        kopia = lista[:]
        start = time.perf_counter()
        posortowana = funkcja(kopia)
        czas = (time.perf_counter() - start) * 1_000_000  # mikrosekundy

        wyniki[nazwa] = czas
        wynik_str = str(posortowana[:8]) + ("..." if len(posortowana) > 8 else "")
        print(f"{nazwa:20} | {wynik_str:35} | {czas:10.2f} μs")

    # Najszybszy (pomijamy sorted bo to nieporównywalny poziom)
    wlasne = {k: v for k, v in wyniki.items() if k != "sorted() Python"}
    najszybszy = min(wlasne, key=wlasne.get)

    print()
    print(f" Najszybszy z własnych algorytmów: {najszybszy} ({wlasne[najszybszy]:.2f} μs)")


kalkulator_sortowania()

# ---
# ---
# 
# # Podsumowanie lekcji
# 
# ---
# 00B2
# ## Trzy algorytmy — jak je zapamiętać?
# 
# | Algorytm | Metafora | Kluczowa operacja | O(n²)? |
# |----------|----------|-------------------|--------|
# | **Bąbelkowe** | Bąbel unosi się do góry | Zamiana sąsiadów | Tak |
# | **Przez wybór** | Wybierasz najmniejszy z talii | Szukanie minimum | Tak |
# | **Wstawianie** | Układanie kart w ręce | Wstawianie w odpowiednie miejsce | Tak |
# 
# ---
# 
# ## Kiedy które?
# 
# ```
# Mała lista (< 100 elementów)?  -> Cokolwiek. Różnica jest niewidoczna.
# 
# Prawie posortowana lista?       -> Wstawianie (O(n) w najlepszym przypadku).
# 
# Mało pamięci, mało zamian?      -> Przez wybór (1 zamiana na przejście).
# 
# Produkcja, duże dane?           → sorted() / .sort() - zawsze.
# ```
# 
# ---
# 
# ## Co zapamiętać z wydajności?
# 
# - O(n²) znaczy: 10x więcej danych = 100x więcej czasu.
# - O(n log n) znaczy: 10x więcej danych ~ 33x więcej czasu.
# - Dla 1000 elementów różnica między O(n²) a O(n log n) to już dziesiątki razy.
# - Dla 1 000 000 elementów to przepaść.
# 
# ---
# 
# ## Kod do zapamiętania
# 
# ```python
# # Bąbelkowe
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if lista[j] > lista[j + 1]:
#             lista[j], lista[j + 1] = lista[j + 1], lista[j]
# 
# # Przez wybór
# for i in range(n - 1):
#     min_idx = i
#     for j in range(i + 1, n):
#         if lista[j] < lista[min_idx]:
#             min_idx = j
#     lista[i], lista[min_idx] = lista[min_idx], lista[i]
# 
# # Wstawianie
# for i in range(1, n):
#     klucz = lista[i]
#     j = i - 1
#     while j >= 0 and lista[j] > klucz:
#         lista[j + 1] = lista[j]
#         j -= 1
#     lista[j + 1] = klucz
# ```