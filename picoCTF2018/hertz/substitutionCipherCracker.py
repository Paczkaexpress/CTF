import os
import sys

if __name__ == "__main__":
    cipherFileName = sys.argv[1]
    cipherFile = open(cipherFileName)
    cipherTxt = cipherFile.read()

    for i in range(26):
        print("{}: {}".format(chr(ord('a') + i), cipherTxt.count(chr(ord('a') + i))))

