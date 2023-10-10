books=[
    {"id":100,"name":"Python","price":350},
    {"id":101,"name":"Java","price":350},
    {"id":102,"name":"Django","price":350},
    {"id":103,"name":"Html","price":350},
    {"id":104,"name":"Bootstrap","price":350},
]

def retrive_books(id=None,*args,**kwargs):
    obj=[i for i in books if i.get("id")==id]
    return obj

print(retrive_books(id=103))

def update_books(id=None,*args,**kwargs):
    obj=[i for i in books if i.get("id")==id][0]
    obj.update(kwargs)

update_books(id=103,name="css")
# print(books)

def distroy_books(id=None,*args,**kwargs):
    obj=[i for i in books if i.get("id")==id][0]
    books.remove(obj)

distroy_books(id=101)
# print(books)

# print(books)
def list_books(id=None,*args,**kwargs):
    obj=[i for i in books if i.get("name")==name]
    return obj