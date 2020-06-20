wget https://2018shell.picoctf.com/static/ed5cc27f269a3a4653f0a65b2e8a2d46/run --no-check-certificate

chmod +x run

./run >> solution.txt

cat solution.txt | xclip -selection clipboard
