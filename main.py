#coding: utf-8
import os
os.system("pip install colorama")
os.system("pip install pyfiglet")
from colorama import Fore,Style
from colorama import init
from pyfiglet import figlet_format
print(figlet_format("caesar cipher",font="standard"))
print("Created by @i74b")
print("""
 __________________
|                  |
| Twitter: _ii404  | 
|   Insta: i74b    |
|__________________|
    
    """)
init(autoreset = True)
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

choice = str(input(Fore.RESET +Style.RESET_ALL+"[+]Encryption or Decryption ? E or D ?"))
if choice.upper()=="E":

    word = str(input("[+]Enter the word in plain text form "))
    
    key = int(input("[+]Key? "))

    def encrypt(word):
        global cipherText
        cipherText=""
        for i in range(len(word)):
            p=letter.index(word[i].upper())+key
     
            if(p>len(letter)):
                 p-=len(letter)
            cipherText+=letter[p]

    encrypt(word)
    print(Fore.GREEN+"Encrypted message is = "+cipherText) 
elif choice.upper()=="D":
    messagee= str(input("[+]Enter Encrypted message "))
    key = int(input("[+]Enter the key "))
    def decrypt(word):
        global decryption
        decryption=""
        for i in range(len(word)):
            p=letter.index(word[i].upper())-key
            
            if(p>len(letter)):
                p-=len(letter)
            decryption+=letter[p]

    decrypt(messagee)

    print(Fore.GREEN+"Decrypted message is = ",decryption)
