import sys
from colorama import Fore, init
init()

def caesar_cipher(message, key, decrypt=False):
    result = ""
    for characters in message:
        if characters.isalpha():
            shift = key if not decrypt else -key
            if characters.islower():
                 result += chr(((ord(characters) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(characters) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += characters
    return result
    

text_to_Encrypt = input(f"{Fore.GREEN}[+]Enter your Message: ")
key = int(input(f"{Fore.GREEN}[+]Specify the shift length: "))
if key > 25 or key < 0:
    print(f"{Fore.RED}[!]Invalid Shift length")
    sys.exit()

encrypted_text = caesar_cipher(text_to_Encrypt, key)
print(f"{Fore.GREEN}[=]Encrypted Text: {encrypted_text}")
