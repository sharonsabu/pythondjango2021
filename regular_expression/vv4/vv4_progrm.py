#print only the valid regriestration number from the file
from re import *

f=open("vv4_file","r")
lst=[]
rule='[K][L]\d{2}[A-Z]{2}\d{1,4}'
for lines in f:
    words=lines.rstrip("\n")

    matcher=fullmatch(rule,words)
    if matcher!=None:
        lst.append(words)
print(lst)