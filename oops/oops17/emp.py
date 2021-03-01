class Employee:
    def __init__(self,eid,name,des,salary,exp):
        self.eid=eid
        self.name=name
        self.des=des
        self.salary=salary
        self.exp=exp
    def print_details(self):
        print(self.eid,self.name,self.des,self.salary,self.exp)
    def __str__(self):
        return self.name

f=open("employee","r")
employees=[]
for lines in f:
    eid,name,des,salary,exp=lines.rstrip("\n").split(",")
    employees.append(Employee(eid,name,des,salary,exp))



for emp in employees:
    print(emp)
print("")

salary=[]
for emps in employees:
    salary.append(emps.salary)
print(max(salary))
print(emp)
print("")

nm=list(map(lambda empl:empl.name,employees))  #empl is a object created by us --- same as "for empl in employees"
print(nm)
print("")

#names of empl whose designation is developer
dev=list(filter(lambda emp:emp.des=="developer",employees))
names=list(map(lambda emp:emp.name,dev))
print(names)
print("")

#count of employees whose design is quality analyst
count=len(list(filter(lambda emp:emp.des=="quality analyst",employees)))
print(count)

#highest salary
hs=max(list(map(lambda emp:emp.salary,employees)))
print(hs)

details=[]
explist=[details.append(emp.eid,emp.name)for emp in list(filter(lambda emp:))]