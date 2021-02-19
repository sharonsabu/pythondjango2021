employees={1000:{"eid":1000,"ename":"ram","desig":"developer","salary":30000},
           1001:{"eid":1001,"ename":"raj","desig":"tester","salary":25000},
           1002:{"eid":1002,"ename":"rahul","desig":"programmer","salary":30000}}

eid=int(input("enter employee id"))
property=input("enter property value")
if eid in employees:
    print(employees[eid]["ename"])
    if property in employees[eid]:
        print(employees[eid][property])
    else:
        print("invalid property")
else:
    print("invalid employee")



