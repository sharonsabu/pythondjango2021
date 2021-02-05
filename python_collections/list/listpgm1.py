lst=[]
print(type(lst))

#or

num=int("10")
lst=list()
print(type(lst))

#next
lst=[10,11,11,12,'hello',10.5]
print(lst)

#next (update pgm)
lst=[10,20,30,40]
print(lst[0]) #prints the number in postion 0
lst[1]=200 #updates the value in postion 1
print(lst)

#next
lst=[1,2,3,4,5]
for num in lst:
    print(num)

    #or
for i in range(0,len(lst)):
    print(lst[i])