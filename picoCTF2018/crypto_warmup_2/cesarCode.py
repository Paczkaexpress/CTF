import sys

code = "cvpbPGS{guvf_vf_pelcgb!}"

decoded = ""
for n in range(len(code)):
    if(code[n].isalpha() and code[n].isupper()):
        decoded += chr(((ord(code[n])- ord('A') - 13) % (ord('Z') - ord('A') + 1)) + ord('A'))
    elif(code[n].isalpha()):
         decoded += chr(((ord(code[n]) - ord('a') - 13) % (ord('z') - ord('a') + 1)) + ord('a'))
    else:
        decoded += code[n]

print(decoded)
