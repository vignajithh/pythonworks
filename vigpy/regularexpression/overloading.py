#same method name different number of parameters


class calculator:

    def add(self,n1,n2):
        print(n1+n2)


    def add(self,n1,n2,n3):
        print(n1+n2+n3)

obj=calculator()
obj.add(10,20,80)