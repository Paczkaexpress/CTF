binwalk -e hell.jpg
cd _hell.jpg.extracted
cat hello_there.txt | grep THM{.* >> ../solution.txt
cat ../solution.txt | xclip -sel clipboard
