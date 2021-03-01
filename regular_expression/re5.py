from re import *

pattern='[A-Z]'       #checking for upper case alphabets from a to z
source="ab Zk@9c"
matcher=finditer(pattern,source)
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("")
print(count)