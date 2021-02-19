f=open("demo","r")
lst=[]

#to print all in demo
for lines in f:
    print(lines)
#to append into list
    lst.append(lines.rstrip("\n"))   #rstrip is used to remove \n from right side of output and if \n is in left side lstrip is used
print(lst)

#to avoid duplicates (convert into set)
st=set(lst)
print(st)


