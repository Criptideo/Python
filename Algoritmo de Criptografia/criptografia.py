import random
import string #import digits, ponctuation, letters, etc

characters = " " + string.punctuation + string.digits + string.ascii_letters + "ã" + "õ" + "ç"
characters = list(characters) #take each of the characters and compile them into a list (kinda explains itself)
mainKey = characters.copy()
random.shuffle(mainKey) #they're all in a random order

#print(f"Characters: {characters}")
#print(f"Key: {mainKey}")
#encryption
message = input("Enter your password here to encrypt: ")
encrypt_message = ""

for letter in message:
    indicator = characters.index(letter)
    encrypt_message += mainKey[indicator]

print(f"original message: {message}")
print(f"encrypted message: {encrypt_message}")

#dencryption
encrypt_message = input("Enter your password here to decrypt: ")
message = ""

for letter in encrypt_message:
    indicator = mainKey.index(letter)
    message += characters[indicator]

print(f"original message: {message}")
print(f"encrypted message: {encrypt_message}")
import string #import digits, ponctuation, letters, etc

characters = " " + string.punctuation + string.digits + string.ascii_letters
characters = list(characters) #take each of the characters and compile them into a list (kinda explains itself)
mainKey = characters.copy()
random.shuffle(mainKey) #they're all in a random order

#print(f"Characters: {characters}")
#print(f"Key: {mainKey}")
#encryption
message = input("Enter your password here to encrypt: ")
encrypt_message = ""

for letter in message:
    indicator = characters.index(letter)
    encrypt_message += mainKey[indicator]

print(f"original message: {message}")
print(f"encrypted message: {encrypt_message}")

#dencryption
encrypt_message = input("Enter your password here to decrypt: ")
message = ""

for letter in encrypt_message:
    indicator = mainKey.index(letter)
    message += characters[indicator]

print(f"original message: {message}")
print(f"encrypted message: {encrypt_message}")