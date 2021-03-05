"""
Caesar Cipher Encryption Program
"""
import sys


def textEncryption(plain_txt, n):   ## encrypts the text entered by user
    txt_result = ""

    for char in plain_txt:
        if (char.isupper()):  ## encrypts uppercase characters
            txt_result += chr((ord(char) - 65 + n) % 26 + 65)

        elif (char.islower()): ## encrypts lowercase characters
            txt_result += chr((ord(char) - 97 + n) % 26 + 97)

        else:
            txt_result += char

    return txt_result



if (len(sys.argv)) == 2:     ## there must be no more than two arguments in the system: the name of  the file and the first argument
    num = int(sys.argv[1])
    usr_txt = input("plaintext: ")

    encrypt_result = textEncryption(usr_txt, num)
    print("ciphertext: " + encrypt_result + "\n")

else:
    print("ERROR. EXIT CODE 1. -- Non-negative number 'n' as argument is required.")
    print("Usage: python caesar.py n")
