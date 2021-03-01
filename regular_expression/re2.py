from re import *

pattern='[ab]'   #checks a or b in each position
source="abababbbab"                        #a b a b a b b b a b
matcher=finditer(pattern,source)           #0 1 2 3 4 5 6 7 8 9
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("")
print(count)