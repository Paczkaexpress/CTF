# downlaod the files provided by the task
wget https://2018shell.picoctf.com/static/f36d468a19d53f9fe375b4e8f4bb84a4/passwd --no-check-certificate
wget https://2018shell.picoctf.com/static/f36d468a19d53f9fe375b4e8f4bb84a4/shadow --no-check-certificate

# then we need to download a software johny the ripper
# sudo apt install john

# then we need to unshodw the provided files
unshadow passwd shadow >> password.txt

# the results of this command will give us the user name and the password
# username: root
# password: password1

# then we need to use this pieces of information to the webserver under the:
nc 2018shell.picoctf.com 5221

