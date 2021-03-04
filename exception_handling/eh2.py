lst=[10,20,30,40]

pos=int(input("enter position"))

try:
    print(lst[pos])

#except:
    #print("exception occured")

except Exception as e:     #this specifies the exception
    print(e.args)