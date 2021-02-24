#inheritance
#multilevel
class Parent:
    def m1(self):
        print("inside m1")

class Subchild(Parent):
    def m2(self):
        print("inside m2")

class Child(Subchild):
    def m3(self):
        print("inside m3")

ch=Child()
ch.m3()
ch.m2()
ch.m1()
print("")

sb=Subchild()
sb.m1()
sb.m2()
print("")

p=Parent()
p.m1()