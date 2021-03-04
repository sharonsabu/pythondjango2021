#dd-mm-yy

from re import *

rule='[0-3][0-9][-][0-1][1-9][-]\d{4}'
variable_name=input("enter variable name")

matcher=fullmatch(rule,variable_name)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")