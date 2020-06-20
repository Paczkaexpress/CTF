# needs to parse the text and convert given text to word format

import re 
import time
import socket

if __name__ == "__main__":

    webpage = "2018shell.picoctf.com"
    port = 64706

    print("Lets pars what is need to be parsed")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Receive the data from the socket")
        
        s.connect((webpage, port))
        while(1): 
            data = s.recv(1024)

            print(data)

            b = re.findall('[0-1]{8}',data.decode('utf-8'))
            h = re.findall('^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$/', data.decode('utf-8'))
            d = re.findall('[0-9]{3}',data.decode('utf-8'))

            print("b: {}, len of b: {}".format(b, len(b)))
            print("d: {}, len of d: {}".format(d, len(d)))
            if(len(b) > 3):
                sol = ("".join([chr(int(x,2)) for x in b ])+'\n').encode('utf-8')
            elif(len(d)>3):
                sol = ("".join([chr(int(x,8)) for x in d ])+'\n').encode('utf-8')
            else:
                txt = data.decode('utf-8').split(' ')
                print(txt)
                print(txt[4])
                sol = (bytearray.fromhex(txt[4]).decode()+'\n').encode('utf-8')
            print(sol)
            time.sleep(1)
            s.send(sol)

            time.sleep(1)

