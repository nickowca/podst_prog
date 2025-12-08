num = open("Pliki/liczby.txt").read().split()
num = list(map(int, num))

print(f"Suma: {sum(num)}")
print(f"Srednia: {sum(num) / len(num)}")