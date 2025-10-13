import math

# pobieranie dlugosci bokow trojkata

a, b, c = map(int, input("Podaj trzy boki trojkata oddzielone spacją: ").split())


# sprawdzanie czy trojkat jest prostokatny
def prostokatny(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Trojkat jest prostokatny")
    else:
        print("Trojkat nie jest prostokatny")

# pole trojkata

def pole(a, b, c):
    p = (a + b + c) / 2
    print("     Pole trójkąta = ", math.sqrt(p * (p - a) * (p - b) * (p - c)))

# obwod trojkata

def obwod(a, b, c):
    print("     Obwód trójkąta = ", a + b + c)


# sprawdzanie czy trojkat jest mozliwy do zbudowania
if a + b > c and a + c > b and b + c > a:
    print("Trójkat jest możliwy do zbudowania")
    if a == b == c:
        print("Trójkat jest równoboczny")
        pole(a, b, c)
        obwod(a, b, c)
        prostokatny(a, b, c)
    elif a == b or a == c or b == c:
        print("Trójkat jest równoramienny")
        pole(a,b, c)
        obwod(a, b, c)
        prostokatny(a, b, c)
    else:
        print("Trójkat jest różnoboczny")
        pole(a, b, c)
        obwod(a, b, c)
        prostokatny(a, b, c)
else:
    print("Trójkat nie jest możliwy do zbudowania")








