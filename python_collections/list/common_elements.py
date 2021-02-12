lst1=[10,11,12,13]
lst2=[9,10,11,82]
res=[]
for num1 in lst1:
    for num2 in lst2:
        if(num1==num2):
            res.append(num1)
print(res)
print("")

#same type program using while

arr1=[10,20,21,22,23]
arr2=[8,9,20,21,25,26]
pos1=0
pos2=0
while((pos1<len(arr1))&(pos2<len(arr2))):
    if arr1[pos1]==arr2[pos2]:
        print(arr1[pos1])
        pos1+=1
        pos2+=1
    elif arr1[pos1]>arr2[pos2]:
        pos2+=1
    else:
        pos1+=1