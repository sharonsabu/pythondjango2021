#rule for validating phone number

from re import *

rule='[+]?9?1?\d{10}'   #? means +91 can be optional
variable_name=input("enter variable name")

matcher=fullmatch(rule,variable_name)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")