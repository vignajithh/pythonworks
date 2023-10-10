class employee:
    id:int
    name:str
    department:str
    gender:str
    salary:int

    def create(self,id,name,depatment,gender,salary):
        self.id=id
        self.name=name
        self.department=depatment
        self.gender=gender
        self.salary=salary

    def get(self):
        print(self.id,self.name,self.department,self.gender,self.salary)

emp1=employee()
emp1.create(100,"vig","it","male",400000000000)
emp2=employee()
emp2.create(200,"vig2","it","malee",542144)

emp1.get()