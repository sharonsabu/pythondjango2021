#polymorphism
#overloading
class Maths:

    def add(self):
        print("inside no arg math method")
    def add(self,num1):
        print("inside single arg math method")
    def add(self,num1,num2):
        print("inside double arg math method")

math=Maths()
math.add(10,20)