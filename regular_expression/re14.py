from re export *
pattern="\w"       #checks for all alphabets both upper and lower case
source="ab Zk@_9c"     #doesn't check for special charaters except underscore
matcher=finditer(pattern,source)
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("")
print(count)