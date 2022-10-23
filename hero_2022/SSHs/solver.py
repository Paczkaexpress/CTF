# API_TOCKEN = "9f34f9ff3dd06fb85b373363b57a2b5cc5cb10057eed34b5f3d2e81726571070"

from pwn import *

# Helpers for many common tasks 
# p.sendline(), p.recvline
# p.recvuntil(':'), pack()

# 1. To ssh into a machine 
# ssh change_me@chall.heroctf.fr -p 10003
s=ssh(host='chall.heroctf.fr',user='user1',password='password123',port=10003)
# p=s.process('./ch15')

txt = s.recvuntil('\n')
print(txt)
txt = s.recvuntil('\n')
print(txt)
txt = s.recvuntil('\n')
print(txt)
txt = s.recvuntil('\n')
print(txt)
