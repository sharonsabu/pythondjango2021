lst=[11,10,13,14,18,15,20,19]
element=int(input("enter the element to be searched"))

#first sorting should be performed (to arrange in ascending order)
lst.sort()

flag=0
lower=0
upper=len(lst)-1
while(lower<=upper):
    mid=(lower+upper)//2
    if(element>lst[mid]):
        lower=mid+1

    elif(element<lst[mid]):
        upper=mid-1

    elif(element==lst[mid]):
        flag=1
        break

if(flag==0):
    print("element not found")
else:
    print("element found")
