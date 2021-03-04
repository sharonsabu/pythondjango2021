age=int(input("enter age"))

try:
    if age<18:
        raise Exception("invalid age")
except Exception as e:
    print(e.args)