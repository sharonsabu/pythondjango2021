class Employee:
    def __init__(self,eid,name,des,salary,exp):
        self.eid=eid
        self.name=name
        self.des=des
        self.salary=salary
        self.exp=exp
    def __str__(self):
        return self.name

f=open("employee","r")
employees=[]
for lines in f:
    eid,name,des,salary,exp=lines.rstrip("\n").split(",")
    employees.append(Employee(eid,name,des,salary,exp))

for emp in employees:
    print(emp)