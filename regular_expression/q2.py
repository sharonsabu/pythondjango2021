from re import *
pattern="a{2}"         #checks for max two no of "a"
matcher=finditer(pattern,"aaaacaaabbaaab")

for match in matcher:
    print(match.start())
    print(match.group())