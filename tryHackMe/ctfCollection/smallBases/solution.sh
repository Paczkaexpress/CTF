python3 decToHexToAscii.py | grep -o THM{.*} > flag.txt
cat flag.txt | xclip -sel clipboard
