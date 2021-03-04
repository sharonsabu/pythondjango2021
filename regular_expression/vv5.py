#dd-mm-yy

from re import *

rule='\d{0,31}[-]\d{0,12}[-]\d{4}'
variable_name=input("enter variable name")

matcher=fullmatch(rule,variable_name)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")