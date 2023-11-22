import stepic
from PIL import Image
from cryptography.fernet import Fernet


print("---------------------------------")

print("---------------------------------")

key = input("Entre la cle : ")
dec = Fernet(key)

file = input("Photo:   ")

img = Image.open(file)
decoded = stepic.decode(img)
text_dec = dec.decrypt(decoded.encode())



print("---------------------------------")

print("le message est  :"+ text_dec.decode())

print("---------------------------------")

input ("Complete (Appuyer sur la touche <Enter> to exit")

print("---------------------------------")
