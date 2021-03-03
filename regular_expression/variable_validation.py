#rules--> first character must be alphabet between a-k
#         second character must be a digit divisible by 3
#         followed by any number of characters

from re import *

rule='[a-kA-K][369][a-zA-Z0-9]*'
variable_name=input("enter variable name")

matcher=fullmatch(rule,variable_name)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")