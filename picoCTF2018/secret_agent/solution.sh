curl  -s --user-agent "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z‡ Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" "http://2018shell.picoctf.com:46162/flag" | grep -o picoCTF{.*} > solution.txt
cat solution.txt | xclip -sel clipboard

