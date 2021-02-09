lst1=[10,11,12,13]
lst2=[9,10,11,82]
res=[]
for num1 in lst1:
    for num2 in lst2:
        if(num1==num2):
            res.append(num1)
print(res)
