import cs50
import sys
import cs50


def caesar(char, key):
    if char.isupper():
        return chr(((ord(char) - 65 + key) % 26) + 65)
    else:
        return chr(((ord(char) - 97 + key) % 26) + 97)


if len(sys.argv) != 2:
    print("Error: Please enter one argument as the Caesar encryption key!")
    exit(1)

key = int(sys.argv[1])
translated = []
print("plaintext: ", end='')
message = cs50.get_string()
for symbol in message:
    if symbol.isalpha():
        translated.append(caesar(symbol, key))
    else:
        translated.append(symbol)

ciphertext = "".join(translated)

print("ciphertext: {}".format(ciphertext))
exit(0)