from re import *

pattern='[^a-zA-Z0-9]'       #checks for other than alphabets and digits
source="ab Zk@9c"
matcher=finditer(pattern,source)
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("")
print(count)