from pwn import *
import re

KEY_LEN = 50000
USED_PASS = 0

r = remote('mercury.picoctf.net', 36449, ssl=False)
r.recvuntil('This is the encrypted flag!\n')
flag = r.recvlineS(keepends = False)
log.info(f"flag {flag}")

bin_flag = unhex(flag)
bin_flag = b"a"*32
print(f"bin flag {bin_flag}")

counter = KEY_LEN - len(bin_flag)
with log.progress("Causing wrap-around") as p:
    while counter > 0:
        p.status(f"{counter} bytes left")
        chunk_size = min(1000, counter)
        r.sendlineafter("What data would you like to encrypt? ", "a"*chunk_size)
        counter -= chunk_size
    print(bin_flag)
    r.sendafter("What data would you like to encrypt? ", bin_flag)
    # r.recvlineS()
    # flag_raw = r.recv(numb = 32)
    flag_raw = r.recvline()
    log.success(f"The flag_raw: {flag_raw}")
    flag = unhex(flag_raw)
    log.success(f"The flag: {flag}")
