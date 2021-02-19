employees={1000:{"eid":1000,"ename":"ram","desig":"developer","salary":30000},
           1001:{"eid":1001,"ename":"raj","desig":"tester","salary":25000},
           1002:{"eid":1002,"ename":"rahul","desig":"programmer","salary":30000}}

def print_employee_details(**kwargs):  #kwargs# ={eid:1000}
    id=kwargs["eid"]  #1000

    if id in employees:
        print(employees[id]["ename"])
        prop=kwargs["property"] #salary
        print(employees[id][prop])
    else:
        print("id doen't exist")


print_employee_details(eid=1000,property="desig")

