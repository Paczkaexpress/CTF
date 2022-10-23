raw = [1096770097,1952395366,1600270708,1601398833,1716808014,1734293296,842413104,1684157793]

password = ""
for x in raw:
    password += chr((x >> 24))
    password += chr((x >> 16) & 0xFF)
    password += chr((x >> 8) & 0xFF)
    password += chr((x >> 0) & 0xFF)

print(f"picoCTF{{{password}}}") 