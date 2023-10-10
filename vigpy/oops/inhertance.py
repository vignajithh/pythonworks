class parent:
    phone="samsung"
    bike="discover"
    def mobile(self):
        print(self.phone)
    def vehicle(self):
        print(self.bike)

class child(parent):
    pass

obj=child()
obj.mobile()