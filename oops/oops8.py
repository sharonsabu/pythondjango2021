class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name


p=Person(27,"ram")
p1=Person(26,"varun")
p2=Person(24,"nikhil")

employees=[]
employees.append(p)
employees.append(p1)
employees.append(p2)

for emp in employees:
    if emp.age>25:
        print(emp.name)

age=[]
for emps in employees:
    age.append(emps.age)
print(max(age))
