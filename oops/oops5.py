#inheritance
#single
class parent:
    def phone(self):
        print("inside parents phone method")

class child(parent):
    pass

ch=child()
ch.phone()