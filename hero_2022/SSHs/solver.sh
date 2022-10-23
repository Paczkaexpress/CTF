#!/usr/bin/env bash

for i in 250; do
    echo $i
    echo "StrictHostKeyChecking=accept-new" > .ssh/config; ./getSSHKey > rsa; chmod 600 rsa; ssh "user{$i}@chall.heroctf.fr" -p 10003 -i rsa
    done



for i in {2..250}; do echo $i; echo "StrictHostKeyChecking=accept-new" > .ssh/config; ./getSSHKey > rsa; chmod 600 rsa; ssh "user${i}@chall.heroctf.fr" -p 10079 -i rsa; done

touch .ssh/config; echo "StrictHostKeyChecking=accept-new" > .ssh/config; ./getSSHKey > rsa; chmod 600 rsa; scp "user${i}@chall.heroctf.fr":~/rcp "user${i}@chall.heroctf.fr":~/rcp${i} -p 10079

scp -i rsa -p 10079 "user${i}@chall.heroctf.fr":~/rcp "user${i}@chall.heroctf.fr":~/rcp${i}
scp -i rsa -p 10079 ~/rsa "user1@chall.heroctf.fr":~/rsa${i}



echo "RSAAuthentication yes" >> .ssh/config
echo "PubkeyAuthentication yes" >> .ssh/config
echo "PasswordAuthentication no" >> .ssh/config

systemctl restart sshd


mkdir .ssh; echo "StrictHostKeyChecking=accept-new" > .ssh/config; ./getSSHKey > rsa; chmod 600 rsa; ssh "user${i}@chall.heroctf.fr" -p 10020 -i rsa 'i=$i+1; echo "echo 'test'" > script.sh; chmod +x script.sh; ./script.sh'

echo 'mkdir .ssh; echo "StrictHostKeyChecking=accept-new" > .ssh/config; ./getSSHKey > rsa; chmod 600 rsa; ssh "user${i}@chall.heroctf.fr" -p 10020 -i rsa' > script.sh; chmod +x script.sh; ./script.sh; echo $i; cat script.sh