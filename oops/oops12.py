#duck typing

class swift:
    def start(self):
        print("swift starts")
    def accelerate(self):
        print("swift accelerates")
    def stop(self):
        print("swift stops")

class seltos:
    def start(self):
        print("seltos starts")
    def accelerate(self):
        print("seltos accelerates")
    def stop(self):
        print("seltos stops")
class person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.stop()

sw=swift()
p=person()
p.drive(sw)
print("")
sl=seltos()
p.drive(sl)