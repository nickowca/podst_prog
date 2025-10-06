import math

"""
wyliczanie rozwiazan funkcji kwadratowej
"""


def funkcja_kwadratowa():
    a = int(input("parametr a: "))
    b = int(input("parametr b: "))
    c = int(input("parametr c: "))

    delta = (b ** 2) - (4 * (a * c))

    if delta > 0:
        x1 = (- b - math.sqrt(delta)) / (2*a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        print("mozliwe rozwiazania: \n x = ", x1, "\n x = ", x2)
    elif delta == 0:
        x = (-b) / (2*a)
        print(x)
    else:
        print("rownanie nie ma rozwiazania")


"""
instrukcja zagnizdzona
"""

def instrukcja_zagniezdzona():
    x = int(input("podaj liczbe: "))
    if x > 0:
        if x % 2 == 0:
            print("liczba dodatnia i parzysta")
        else:
            print("liczba dodatnia i nieparzysta")
    elif x < 0:
        if x % 2 == 0:
            print("liczba ujemna i parzysta")
        else:
            print("liczba ujemna i nieparzysta")
    else:
        print("x = 0")

"""
prosty kalkulator w pythonie
"""


def kalkualtor():

    def addition():
        a = int(input("first num: "))
        b = int(input("second num: "))
        print(f"{a} + {b} = {a + b}")

    def subtraction():
        a = int(input("first num: "))
        b = int(input("second num: "))
        print(f"{a} - {b} = {a - b}")

    def multiplication():
        a = int(input("first num: "))
        b = int(input("second num: "))
        print(f"{a} x {b} = {a * b}")

    def division():
        a = int(input("first num: "))
        b = int(input("second num: "))
        print(f"{a} / {b} = {a / b}")

    def end():
        print("see you later")
        return

    while True:
        choice = input("what would you like to do? \n [1- add, 2 - subtract, 3 - multiply or 4 - divide two numbers]: ")
        if choice == '1':
            addition()
        elif choice == '2':
            subtraction()
        elif choice == '3':
            multiplication()
        elif choice == '4':
            division()
        elif choice == '5':
            end()

        nextcalc = input("run program again? ")
        if nextcalc == "no":
            break
    else:
        print("invalid input")


def labirynt():
    import random
    wins = 0
    print('masz do pokonania trzy rozwidlenia dróg')
    print('przed kazdym z nich musisz wybrac odpowiednia droge')
    print('jesli zle wybierzesz droge na pewnym etapie to przegrywasz')

    ver = int(input("chcesz zagrac w 0 - latwiejsza wersje czy 1 - trudniejsza wersje? "))
    if ver == 0:
        while wins < 3:
            d = int(input("wybierz droge lewo (1) prawo (2) prosto (3): "))

            liczba = random.sample(range(1,4), 2)
            if d == liczba:
                print("Dobrze trafiłeś, przechodzisz dalej")
                wins += 1
            else:
                print("wpadles w przepasc, poprawna odpowiedz to byla: ", liczba)
                break
        if wins == 3:
            print("Gratulacje! Przeszedłeś przez labirynt!")
    elif ver == 1:
        while wins < 3:
            d = int(input("wybierz droge lewo (1) prawo (2) prosto (3): "))

            liczba = random.randint(1, 3)
            if d == liczba:
                print("Dobrze trafiłeś, przechodzisz dalej")
                wins += 1
            else:
                print("wpadles w przepasc, poprawna odpowiedz to byla: ", liczba)
                break
        if wins == 3:
            print("Gratulacje! Przeszedłeś przez labirynt!")


def temperatura():

    temp = int(input("wprowadz temperature: "))
    humid = int(input("wprowadz wilgotnosc: "))

    if temp < 20 and humid > 70:
        print("weź parasol i kurtke")
    elif temp < 20:
        print("wez tylko kurtke")
    elif humid > 70:
        print("wez parasol")
    else:
        print("pogoda jest idealna idz dotknij trawy w koncu")

temperatura()
