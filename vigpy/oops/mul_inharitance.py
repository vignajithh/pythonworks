class p1:
    def m1(self):
        print("inside class p1 m1 method")

class p2:
    def m2(self):
        print("inside class p2 m2 method")


class child(p2,p1):
    def m3(self):
        print("inside class child m3 method")

obj=child()
obj.m3()
obj.m2()
obj.m1()