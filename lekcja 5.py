"""
13 october 2025
lekcja 5 - pętle w pythonie
"""

"""
pętla for

pętla for służy do wielokrotnego wykonywania określonego bloku kodu, dla każdego elementu w sekwencji (takiej jak lista, krotka, słownik, zbiór lub ciąg znaków).
"""

for i in [1, 2, 3, 4, 5]:
    print("nr ", i)

# iteracja po znakach w stringu
for char in "Python":
    print("char: ", char)

#wypisz wszystkie litery w imieniu oddzielone znakiem '#'
name = "Nikodem"
for char in name:
    print(char, end="#")

"""
funckja range()

pętla for jest często używana w połączeniu z funkcją range(), która generuje sekwencję liczb całkowitych w określonym zakresie.
"""

for i in range(5):  # od 0 do 4
    print("range - nr ", i)

# zadanie - wypisz wszystkie liczby od 50 do 60 (włącznie)
for i in range(50, 61):
    print("liczba: ", i)

# mozna podac trzeci argument - krok
for i in range(0, 21, 2):  # od 0 do 20 co 2
    print("liczba parzysta: ", i)



"""
pętle while

pętla while wykonuje blok kodu tak długo, jak długo warunek jest prawdziwy.
"""

x = 10
while x > 0:
    print("x = ", x)
    x -= 1  # zmniejszanie wartości x o 1

"""
instrukcja break i continue
instrukcja break służy do natychmiastowego zakończenia pętli, natomiast instrukcja continue pomija bieżącą iterację i przechodzi do następnej.
"""

for i in range(10):
    if i == 5:
        print("przerywam pętlę na i = 5")
        break  # przerywa pętlę gdy i równa się 5
    print("i = ", i)