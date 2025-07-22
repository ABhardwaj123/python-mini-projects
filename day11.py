#encrypter and decrypter
import string


def encrypt(message, key):
    encryption = ""

    for char in message:
        if char.isalpha():
            ref = ord('A') if char.isupper() else ord('a')
            shift = ((ord(char) - ref + key) % 26) + ref
            encryption += chr(shift)
        else:
            encryption += char #if char is not an alphabet

    return encryption

def decrypt(message , key):
    return encrypt(message , -key)

print("welcome to message encryter/decryter!")
print("Encrypt->E\nDecrypt->D")

choice = input("enter your choice: ").lower()

if choice == 'e':
    message = input("enter your message: ")

    try:
        key = int(input("enter your key(from 1 to 25): "))
        encryption = encrypt(message , key)
        print("your enctryted message is: \n")
        print(encryption)
    except ValueError:
        print("invalid key")

elif choice == 'd':
    message = input("enter your message: ")

    try:
        key = int(input("enter your key(from 1 to 25): "))
        decryption = decrypt(message , key)
        print("your decrypted message is: \n")
        print(decryption)
    except ValueError:
        print("invalid key")

else:
    print("invalid choice")
