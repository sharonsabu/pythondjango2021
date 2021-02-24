#usage of constructor

class employee:

    company_name="ctc"

    def __init__(self,age,name):
        self.age=age
        self.name=name

    def print_person(self):
        print(self.age)
        print(self.name)
        print(employee.company_name)

emp=employee(24,"amal")
print(emp.name)
print(emp.company_name)