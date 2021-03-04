n1=int(input("enter n1"))
n2=int(input("enter n2"))

try:
    res=n1/n2
    print(res)

except Exception as e:
    n2=int(input("enter n2"))
    try:
        res=n1/n2
        print(res)
    except Exception as e:
        print(e.args)
finally:
    print("data base operation")
    print("file write")