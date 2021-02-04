#        1              *
#        2 2            * *
#        3 3 3          * * *
#        4 4 4 4        * * * *

row=4
for num in range(1,row+1):
    for i in range(num):
        print(num,end=" ")
    print(" ")

for i in range (0,row):
    for j in range (0,i+1):
        print("*",end=" ")b
    print(" ")


