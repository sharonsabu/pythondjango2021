lst=[1,2,3,4]
for i in lst:
    for j in lst:
        if(i+j==6)&(i!=j):
            print(i,",",j)
print("")

#or

lt=[1,2,3,4]
low=0
num=6
upp=len(lt)-1
while(low<upp):
    total=lt[low]+lt[upp]
    if (num==total):
        print(lt[low],lt[upp])
        low+=1
        upp-=1
    elif(total>num):
        upp-=1
    elif(total<num):
        low+=1