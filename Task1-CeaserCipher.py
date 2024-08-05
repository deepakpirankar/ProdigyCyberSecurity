#TASK-01

#Encryption
def encrypt(plaintext,s):
    result = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if (char==" "):
            result += " ";
        else:
            if(char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
    return result

plaintext = input("Enter text to encrypt : ")
s = 3
print("Plain Text : " + plaintext)
print("Shift Pattern : " + str(s))
print("Cipher : " + encrypt(plaintext,s))


#Decryption
def decrypt(ciphertext,s):
    result = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if (char==" "):
            result += " ";
        else:
            if(char.isupper()):
                result += chr((ord(char) - s - 65) % 26 + 65)
            else:
                result += chr((ord(char) - s - 97) % 26 + 97)
    return result

ciphertext = input("Enter text to decrypt : ")
s = 4
print("Plain Text : " + ciphertext)
print("Shift Pattern : " + str(s))
print("Cipher : " + decrypt(ciphertext,s))