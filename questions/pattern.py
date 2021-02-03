# if input is 2
#
# output should be 24 (2+22)
# 3
# 3+33+333=369
# 4
# 4+44+444+4444=...

num=int(input("enter the number"))
pattern=""
tot=0
for i in range(1,(num+1)):
    pattern=str(num)*i
    print(pattern)  #if here input is 2, output will be 2 and 22
                        # if input 3, output 3,33,and 333
    tot+=int(pattern)
print(tot)
