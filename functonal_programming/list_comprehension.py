lst1=[1,2,3]
lst2=[3,4,5]

op=[]
for i in lst1:
    for j in lst2:
        op.append((i,j))
print(op)

#or

ops=[(i,j)for i in lst1 for j in lst2]
print(ops)

square=[i**2 for i in lst1]
print(square)

even_no=[i for i in lst1 if i%2==0]
print(even_no)

common_elements=[i for i in lst1 for j in lst2 if i==j]
print(common_elements)