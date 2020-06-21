# in order to find a flag in this tash is it required to use a binwalk

# after a short investigation we can find that the main file contains other files inside thus it is worthy to check with binwalk
# aslo after using "grep flag" we can find file flag.txt so maybe after the binwalk we will be able to find it

binwalk -e flag.pcapng
grep -Pro "THM{(.*){10,}}" * > flag.txt
cat flag.txt | xclip -sel clipboard

