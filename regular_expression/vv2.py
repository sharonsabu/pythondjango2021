#rule for validating all gmail id's
#recipient name-->upper or lowercase letters or digits 0-9,max 64

from re import *

rule='[a-zA-Z0-9]{1,64}@gmail.com'
variable_name=input("enter variable name")

matcher=fullmatch(rule,variable_name)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")