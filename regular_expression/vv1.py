#rule for validation kerala vehicle registration number
#example--> KL08BN4970

from re import *

rule='[K][L]\d{2}[A-Z]{2}\d{1,4}'
variable_name=input("enter variable name")

matcher=fullmatch(rule,variable_name)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid")