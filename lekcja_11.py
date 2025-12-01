# def check(ssn):
#     if len(ssn) != 11 or not ssn.isdigit():
#         return False
#     weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
#     checksum = sum(int(ssn[i]) * weights[i] for i in range(10))
#     control_digit = (10 - (checksum % 10)) % 10
#     return control_digit == int(ssn[10])
#
#
#
# ssn = input("podaj numer PESEL: ")
# if check(ssn):
#     print("poprwany")
# else:
#     print("n poprawny")
#
#
#
# kolory = ['czerwony', 'zielony', 'niebieski', 'żółty']
# liczby = [4,5,6,7]
# imiona = ['Ania', 'Bartek', 'Cezary', 'Dorota']
#
# for kolor, liczba, imie in zip(kolory, liczby, imiona):
#     print(f"{imie} ma {liczba} {kolor} jabłek")



### rekurencja

def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n-1)

print(silnia(5))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(int(input('ktory element w ciagu: '))))
for n in range(1,int(input('ile elementow ciagu: '))+1):
    print(fibonacci(n), end=' ')

#funckja rekurencyjna obliczania sumy liczb 1 do n

def suma(n):
    if n == 1:
        return 1
    return n + suma(n-1)
print("\n\nsuma liczb od 1 do n:")
print(suma(10))

# rekurencyjna wersja liczenia cyfr liczby
def liczba_cyfr(n):
    if n < 10:
        return 1
    return 1 + liczba_cyfr(n // 10)
print("\nliczba cyfr w liczbie:")
print(liczba_cyfr(2325))




