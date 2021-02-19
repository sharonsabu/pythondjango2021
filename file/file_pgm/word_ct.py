f=open("word","r")
dict={}
for lines in f:
    word=lines.rstrip("\n").split(" ")
    for w in word:
        if w not in dict:
            dict[w]=1
        else:
            dict[w]+=1
for k,v in dict.items():
    print(k,"-",v)
