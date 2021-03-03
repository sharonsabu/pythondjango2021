from re import *
pattern="a+"         #checks for one or more than one a
matcher=finditer(pattern,"aaaacaaabbaaab")

for match in matcher:
    print(match.start())
    print(match.group())