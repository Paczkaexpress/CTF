# need to download all pages from the webside
wget http://2018shell.picoctf.com:35349/ --no-check-certificate
wget http://2018shell.picoctf.com:35349/mycss.css --no-check-certificate
wget http://2018shell.picoctf.com:35349/myjs.js --no-check-certificate

cat * | egrep 'flag:.{24}' >> solution.txt
