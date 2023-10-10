class Person:
    def __init__(self):
        self.name="vig"

    def bio(self):
        self.adr="abc"
        self.course="xya"

obj=Person()
# print(obj.name)

class Book:
    def __init__(self):
     self.id=int(input("enter the id"))
     self.title=input("enedtr a name")
     self.author=input("enetr a auther")
     self.price=input("enter the price")

    def getauthor(self):
        print(self.author)
    def gettitle(self):
        print(self.title)
    def setprice(self):
        self.price=int(input("enter price"))
    def settitle(self):
        self.title=input("enter the title")

b1=Book()
b1.getauthor()
b1.gettitle()


