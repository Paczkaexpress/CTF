import sys

try:
    code =sys.argv[1]
    key = sys.argv[2]
except:
    print("Need to provide two arguments")
    quit()

decoded = ""

if(len(code) <= len(key)):
    for n in range(len(code)):

        decoded += chr(ord('a') +  (ord(code[n]) - ord('a') - (ord(key[n]) - ord('a'))) % ((ord('z')+1-ord('a'))))

decoded = decoded.upper()

print("picoCTF{{{}}}".format(decoded))

