def my_phone(func):
    def innerFun(pno):
        if len(pno)<10:
            raise Exception("invalid")
        else:
            return func(pno)
    return innerFun

@my_phone
def val_phone(pno):
    return "valid"+pno

print(val_phone("9876543210"))
