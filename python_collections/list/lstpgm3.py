lst=[1,2,3,4]
for num1 in lst:
    for num2 in lst:
        if(num1+num2==6)&(num1!=num2):
            print(num1,num2)
