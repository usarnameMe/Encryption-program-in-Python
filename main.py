import random
import string

chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"Chars: {chars}")
print(f"key: {key}")


#ENCRYPT
plaint_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plaint_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message : {plaint_text}")
print(f"Encrypted message : {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plaint_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plaint_text += chars[index]

print(f"Encrypted message : {cipher_text}")
print(f"Original message : {plaint_text}")
import random
import string

chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"Chars: {chars}")
print(f"key: {key}")


#ENCRYPT
plaint_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plaint_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message : {plaint_text}")
print(f"Encrypted message : {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plaint_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plaint_text += chars[index]

print(f"Encrypted message : {cipher_text}")
print(f"Original message : {plaint_text}")
