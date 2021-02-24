#ducktyping
class pycharm:
    def create_file(self):
        print("pycharm file created")
    def execute_program(self):
        print("pycharm program executed")

class vscode:
    def create_file(self):
        print("vscode file created")
    def execute_program(self):
        print("vscode program executed")


class programmer:
    def coding(self,ide):
        ide.create_file()
        ide.execute_program()o  

py=pycharm()
vs=vscode()
pg=programmer()
pg.coding(py)
print("")
pg.coding(vs)