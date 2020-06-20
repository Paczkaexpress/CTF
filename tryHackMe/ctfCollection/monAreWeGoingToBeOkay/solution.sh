steghide --extract -sf Extinction.jpg
cat Final_message.txt | grep THM{.*} > solution.txt
cat solution.txt | xclip -sel clipboard 
