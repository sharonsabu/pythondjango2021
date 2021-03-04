n1=int(input("enter a no"))

try:
    if n1<0:
        raise Exception("invalid")
except Exception as e:
    print(e.args)