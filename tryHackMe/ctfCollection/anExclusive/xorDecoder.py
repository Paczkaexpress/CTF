import codecs

toDecode = "44585d6b2368737c65252166234f20626d"
key = "1010101010101010101010101010101010"

toDecode = codecs.decode(toDecode, 'hex')
keyHex = codecs.decode(key,'hex')

xored = [chr(toDecode[i]^keyHex[i]) for i in range(len(toDecode))]


#print(toDecode)
#print(xored)

solution = "".join(xored)


print(solution)

