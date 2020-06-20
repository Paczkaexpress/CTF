wget https://2018shell.picoctf.com/static/69b2020b48082fb24714bf93707183e8/2018.png --no-check-certificate
strings 2018.png | grep picoCTF{.*} > solution.txt
cat solution.txt | xclip -sel clipboard
