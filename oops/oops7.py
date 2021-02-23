class parent:
    def m1(self):
        print("inside m1")

class subchild:
    def m2(self):
        print("inside m2")

class child(parent,subchild):
    def m3(self):
        print("inside m3")

ch=child()
ch.m2()
ch.m1()
ch.m3()