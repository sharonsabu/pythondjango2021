#print only the valid regriestration number from the file
f=open("vv4_file","r")

from re import *

rule='[K][L]\d{2}[A-Z]{2}\d{1,4}'
variable_name=input("enter variable name")

matcher=fullmatch(rule,variable_name)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")