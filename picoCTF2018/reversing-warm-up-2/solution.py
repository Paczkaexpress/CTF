import base64
import sys
import re

f = open("input.txt", "r")

print("picoCTF{{{}}}".format(str(base64.b64decode(f.read()))[2:-1]))
