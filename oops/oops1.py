class Person:
    def set_person(self,name,age):
        self.name=name
        self.age=age

    def print_person(self):
        print(self.name)
        print(self.age)

obj=Person()
obj.set_person("amalu",24)
obj.print_person()

obj1=Person()
obj.set_person("sha",22)
obj.print_person()