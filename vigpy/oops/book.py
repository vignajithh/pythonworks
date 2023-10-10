class book:
    book_name:str
    author:str
    price:str
    pages:str

    def __init__(self,book_name,author,price,pages):

        self.book_name=book_name
        self.author=author
        self.price=price
        self.pages=pages

    def get(self):
        print(self.book_name,self.author)

    def __str__(self):
        return self.book_name+str(self.price)
    


obj=book("harry potter","jk rolling",800,500)

print(obj)

# print(obj.book_name,obj.author)

obj1=book("wings of fire","apj",600,500)
# print(obj1.author,obj1.book_name)