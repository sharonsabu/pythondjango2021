from re import *
pattern="a*"         #checks for one or more than one 'a' also checks the position where there is no 'a'
matcher=finditer(pattern,"aaaacaaabbaaab")       #where there is no 'a' the output will print a space

for match in matcher:
    print(match.start())
    print(match.group())