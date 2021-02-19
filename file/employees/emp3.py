employees={1000:{"eid":1000,"ename":"ram","desig":"developer","salary":30000},
           1001:{"eid":1001,"ename":"raj","desig":"tester","salary":25000},
           1002:{"eid":1002,"ename":"rahul","desig":"programmer","salary":30000}}

def details(**kwargs):
    id=kwargs["eid"]
    if id in employees:
        print(employees[id]["ename"])
        pro=kwargs["property"]
        print(employees[id][pro])
    else:
        print("id doesn't exist")
id=int(input("enter the employee id"))
property=input("enter the details to be searched").lower()