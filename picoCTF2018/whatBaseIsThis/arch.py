# cannot solve it so I will brute force the solution:

import re
import time
import socket 


if __name__ == "__main__":

    web = "2018shell.picoctf.com"
    port = 63299

    print("Lets do a brute force for the desrouleuax task")

    print("Web page {} on socket {} \n".format(web, socket))
   
    for solution in range(0,200):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Trying new number {}".format(solution))
            s.connect((web, port))
            data = s.recv(1024)
            #print(data)
            s.send(b'186.120.220.162\n')

            data = s.recv(1024)
            if("43.113.162.172" in data.decode('utf-8')):
                s.send(b'2\n')
            elif("186.120.220.162?" in data.decode('utf-8')):
                s.send(b'3\n')
            elif("34.104.29.49" in data.decode('utf-8')):
                s.send(b'2\n')
            else:
                s.send(b'1\n')

            data = s.recv(1024)
            #print(data)
            sol = ("{:.2f}".format(solution/100) + '\n').encode('utf-8')
            print(sol)
            s.send(sol)

            data = s.recv(1024)
            print(data)

    print("Job finished")
