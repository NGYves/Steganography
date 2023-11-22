import stepic
from PIL import Image
from cryptography.fernet import Fernet


print("---------------------------------")
print("---------------------------------")

key = Fernet.generate_key()
print("Votre cle cryptographique :")
print(key)
enc = Fernet(key)

text = input("Message: ")
text_enc = enc.encrypt(text.encode())


file = input("Photo:   ")

img = Image.open(file)
img_stegano = stepic.encode(img, text_enc)


img_stegano.save("stegano.png")

print("---------------------------------")

input("Complete (press enter to exit")


print("----------------------------------")
