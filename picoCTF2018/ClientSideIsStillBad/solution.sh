cat index.html | grep -oE \'.*\' | cut -d "'" -f2 | tac | tr -d "\n" >> solution.txt
cat solution.txt | xclip -sel clip

