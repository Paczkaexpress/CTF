# The task is very simple we need to use a hex editor to read the flag
wget https://2018shell.picoctf.com/static/e1230cc4fc0b9b6d8fa6da0b4b918b4f/hex_editor.jpg --no-check-certificate
cat hex_editor.jpg | grep -ao picoCTF{.*} >> solution.txt
cat solution.txt | xclip -sel clipboard

