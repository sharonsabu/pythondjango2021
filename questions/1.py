# if input is 2
#
# output should be 24 (2+22)
# 3
# 3+33+333=369
# 4
# 4+44+444+4444=...

num=int(input("enter the number"))
for i in range(1,num+1):
    a=str(num)*i
    print(a)   #if here input is 2, output will be 2 and 22
                        # if input 3, output 3,33,and 333
    b=int(a)
    for j in range(b,b+1):
    print(b)