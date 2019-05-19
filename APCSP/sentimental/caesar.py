import sys
from cs50 import get_string
def encrypt(oldletter, key):
    if oldletter.isalpha():
        if oldletter.isupper():
            newletter = (((ord(oldletter) - 65) + key) % 26) + 65
        if oldletter.islower():
            newletter = (((ord(oldletter) - 97) + key) % 26) + 97
    else:
        newletter = oldletter
        return(newletter)
    #print(chr(newletter))
    return(chr(newletter))

newletter = 0
if (len(sys.argv) != 2):
    print("Usage: ./caesar <name>\n")
    exit(1)
key = int(sys.argv[1])
plaintext = get_string("Plaintext: ")
print("ciphertext: ", end ='')
for i in range(len(plaintext)):
    oldletter = plaintext[i]
    newletter = encrypt(oldletter, key)
    print(newletter, end ='')
    i = i + 1
print("\n")