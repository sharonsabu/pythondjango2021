class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return (self.pages+other.pages)
    def __sub__(self, other):
        return self.pages-other.pages
    def __mul__(self, other):
        return self.pages*other.pages
    def __truediv__(self, other):  #division
        return self.pages/other.pages
    def __str__(self):
        return self.pages

obj=Book(100)
obj1=Book(200)
print(obj+obj1)
print(obj1-obj)
print(obj*obj1)
print(obj/obj1)
