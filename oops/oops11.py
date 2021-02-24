#overriding
class person:
    def __init__(self,age,name):
        self.age=age
        self.name=name

    def __str__(self):
        return self.name+str(self.age)

p=person(24,"amal")
p1=person(25,"ajay")
print(p)
print(p1)