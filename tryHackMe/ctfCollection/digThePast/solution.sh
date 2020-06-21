# we need to open the web archive and get the old version of the webpage
date=20200102
webArch=https://web.archive.org/web/
web=/https://www.embeddedhacker.com/

link=$webArch$date'?'$web
echo "I will look at $link"
wget $link
cat * | grep -Po "THM{(.){10,}}" > flag.txt
cat flag.txt | xclip -sel clipboard
