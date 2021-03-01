from re import *

pattern='[a-zA-Z0-9]'       #checking for lower and upper case alphabets from a to z and also digits between 0 to 9
source="ab Zk@9c"
matcher=finditer(pattern,source)
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("")
print(count)