#question in book

pow=int(input("enter number"))
ll=int(input("enter lowerlimit"))
ul=int(input("enter upperlimit"))

for num in range(1,ul+1):
    a=num**pow
    if((a>=ll)&(a<=ul)):  #if a in range(ll,(ul+1)):
        print(a)
