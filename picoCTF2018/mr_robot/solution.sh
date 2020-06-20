# in order to get the flag we need to first download page using wget with recursion
wget -r http://2018shell.picoctf.com:10157/ --no-check-certificate
# after that we can ispect the content of the created folder
# then we can gat a new index to look at:
var=$(cat 2018shell.picoctf.com:10157/robots.txt | tail -1 | cut -b 12-34)
wget "http://2018shell.picoctf.com:10157/${var}" --no-check-certificate
cat 1* | grep -ao picoCTF{.*} >> solution.txt
cat solution.txt | xclip -sel clipboard

