class bank:
    account_number=str
    person_name=str
    ifsc=str
    branch=str
    bank_name=str
    balance=str
    acc_typr=str

    def create(self,account_number,persom_name,ifsc,branch,bank_name,balance,acc_type):
        self.account_number=account_number
        self.person_name=persom_name
        self.ifsc=ifsc 
        self.branch=branch
        self.bank_name=bank_name
        self.balance=balance
        self.acc_typr=acc_type

    def deposit(self,amount):
        self.balace+=amount
        print("your {self.bank_name} ha been credcted with{amount} avalable {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("insuficiant balance transaction declined")
        else:
            self.balance-=amount
            print("your {self.bank_name} ha been debited with{amount} avalable {self.balance}")
    def geṭˍbalance(self):
        print(f"your avalble balance{self.balance}")

obj=bank()
obj.create(1000,"vig","sbk001","kakkand","savings",35000,"sbi")

obj.get()