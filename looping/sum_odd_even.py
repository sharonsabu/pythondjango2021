i=1
n=int(input("enter the limit to be sum:"))
otot=0
etot=0
while i<=n:
    if i%2==0:
        etot=etot+1
    else:
        otot=otot+1

    i+=1
print("total of even no.s",etot)
print("total of odd no.s:",otot)