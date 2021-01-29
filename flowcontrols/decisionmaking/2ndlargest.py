num1=int(input("enter the 1st number"))
num2=int(input("enter the 2nd number"))
num3=int(input("enter the 3rd number"))
#if((num1>num2)&(num1<num3))|((num1<num2)&(num1>num3)):
 #   print("num1 is 2nd largest")
#elif((num2>num3)&(num2<num1))|((num2<num3)&(num2>num1)):
 #   print("num2 is 2nd largest ")
#else:
 #   print("num3 is largest")

 #OR
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("num2 is 2nd largest")
    else:
        print("num3 is 2nd largest")
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("num1 is 2nd largest")
    else:
        print("num3 is 2nd largest")
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("num1 is 2nd largest")
    else:
        print("num2 is 2nd largest")
elif(num1==num2)&(num1==num3):
    print("all are equal")
else:
    pass