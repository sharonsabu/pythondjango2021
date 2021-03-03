#rule for validating phone number

from re import *

rule='[+]91\d{10}'
variable_name=input("enter variable name")

matcher=fullmatch(rule,variable_name)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")