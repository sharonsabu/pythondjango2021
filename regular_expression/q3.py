from re import *
pattern="a{2,3}"         #checks for min 2 and max 3 no of "a"
matcher=finditer(pattern,"aaaacaabbaaab")

for match in matcher:
    print(match.start())
    print(match.group())