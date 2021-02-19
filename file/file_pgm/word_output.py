f=open("word","r")

lst=[]
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for w in words:
        lst.append(w)
for w in lst:
    print(w)