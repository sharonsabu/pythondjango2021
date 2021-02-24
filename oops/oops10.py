#overriding

class Parent:
    def phone(self):
        print("have nokia phone")

class Child(Parent):
    def phone(self):
        print("iphone")

ch=Child()
ch.phone()