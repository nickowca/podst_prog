### program nr 1 ###

# suma liczb parzystych podzielnych przez 3
start = int(input("Podaj poczatek zakresu: "))
end = int(input("Podaj koniec zakresu: "))
suma = 0
for i in range(start, end + 1):
    if i % 2 == 0 and i % 3 == 0:
        suma += i
print("Suma liczb parzystych podzielnych przez 3 w zakresie od", start, "do", end, "wynosi:", suma)

### program nr 2 ###

# choinka z gwiazdek o podanej wysokosci (noga stala 2 gwiazdki) (zagniezdzony for)
wysokosc = int(input("Podaj wysokosc choinki: "))
for i in range(wysokosc):
    for j in range(wysokosc - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
for l in range(2):
    for m in range(wysokosc - 1):
        print(" ", end="")
    print("*")
