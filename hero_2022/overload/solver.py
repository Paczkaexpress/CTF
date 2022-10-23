raw = ""
with open('/home/paczkaexpress/software/CTF/hero_2022/overload/overload.txt','r') as f:
    raw = f.read()

for i in range(100):
    if(raw[i] == 'H'):
        print(f"{i} {'H'}")

# offset = 46
offset = 59
for i in range(20,200):
    print(raw[offset::i])

decoded = ""
dictionary = set('}{qwertyuioplkjhgfdsazxcvbnm')


for c in raw:
    if(c in dictionary):
        decoded += c

print(decoded)