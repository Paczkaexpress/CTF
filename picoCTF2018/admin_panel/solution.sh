wget https://2018shell.picoctf.com/static/19129d64f5676ff5661da65b9772aff5/data.pcap --no-check-certificate
cat * | grep -ao picoCTF{.*} >> solution.txt
cat solution.txt | xclip -sel clipboard
