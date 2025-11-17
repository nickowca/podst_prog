
alphabet = {chr(ord('a') + i): i + 1 for i in range(26)}


def l_t_n(letter):
    return alphabet.get(letter.lower())

text = input("input: ")


print()
output = ' '.join(str(l_t_n(letter)) for letter in text if letter.lower() in alphabet)
print("output:", output)

for letter in text:
    i = alphabet[letter.lower()]
    shift_letter = i + 3
    if shift_letter > 26:
        shift_letter -= 26
    for key, value in alphabet.items():
        if value == shift_letter:
            print(key, end='')

# decipher: