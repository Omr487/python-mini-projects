
import random
import string

chars = list(string.punctuation + string.digits + string.ascii_letters + " ")
key = chars.copy()
random.shuffle(key)
#encrypt
plain_text = input("enter a message to encrypt: ")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypted message : {cipher_text}")
#decrypt
cipher_text = input("ENter a message to encrypt")
plain_text = ""
for letter in cipher_text :
    index = key.index(letter)
    plain_text += chars[index]
print (f"encrypted message : {cipher_text}")
print (f"orignal message : {plain_text}")
