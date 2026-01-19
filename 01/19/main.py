n = int(input("Podaj liczbe: "))


def piramida(n):

    if n <= 0:
        print("podaj liczbe wieksza od 0")
        return
    with open("piramida.txt", "w") as f:

        for i in range(1, n + 1):
            print((n - i)  * " " + (2 * i - 1) * "*")
            f.write((n - i)  * " " + (2 * i - 1) * "*" + "\n")

        for i in range(n - 1, 0, - 1):
            print(" " * (n - i) + "*" * (2 * i - 1))
            f.write(" " * (n - i) + "*" * (2 * i - 1) + "\n")

        for i in range(1, n + 1):
            print( "*" * i)
            f.write("*" * i + "\n")

        for i in range(n-1, 0, -1):
            print( "*" * i)
            f.write("*" * i + "\n")



piramida(n)