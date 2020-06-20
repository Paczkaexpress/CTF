import sys
import os
import re

def decodeCeasar(cipher: str) -> str:
    decoded = "picoCTF"
    cipher = re.search("{.*}",cipher).group(0)

    for m in range(26):
        decoded = "picoCTF"
        for n in range(len(cipher)):
            if cipher[n].isalpha():
                c = cipher[n]
                ceasar = m 
                decoded += chr(ord('a') + (ord(c) + 1 - ord('a') - ceasar) % (ord('z') + 1 - ord('a')))
            else:
                decoded += cipher[n]
        print("{} {}".format(m, decoded))
        
    return decoded

if __name__ == "__main__":
    cipherFile = sys.argv[1]
    f = open(cipherFile)
    cipher = f.read()
    print(decodeCeasar(cipher))
