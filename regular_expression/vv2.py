#rule for validating all gmail id's

from re import *

rule=''
variable_name=input("enter variable name")

matcher=fullmatch(rule,variable_name)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")