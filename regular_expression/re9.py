from re import *

pattern='[^0-9]'       #checking for other than digits from 0 to 9
source="ab Zk@9c"
matcher=finditer(pattern,source)
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("")
print(count)