class Student:
    def set_studeny(self,name,age,total):
        self.name=name
        self.age=age
        self.total=total

    def print_student(self):
        print(self.name)

        print(self.age)
        print(self.total)

obj=Student()
obj.set_studeny("amal",24,95)
obj.print_student()
