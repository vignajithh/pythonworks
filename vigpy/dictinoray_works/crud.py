items=[
    {"id":100,"name":"cb","price":160},
    {"id":101,"name":"vb","price":140},
    {"id":102,"name":"ghhe roast","price":120},
    {"id":103,"name":"afm","price":130},
    {"id":104,"name":"cf","price":90},
    {"id":105,"name":"porotta","price":10},

]

def add_item(*args,**kwargs):
    print(kwargs)
    items.append(kwargs)

# add_item(id=106,name="bb",price=180)

# print(items)

def retrive_items(id=None,*args,**kwargs):
    obj=[i for i in items if i.get("id")==id]
    return obj
# print(retrive_items(id=104))

def distroy_item(id=None,*args,**kwargs):
    obj=[i for i in items if i.get("id")==id][0]
    # items.remove(obj)

distroy_item(id=102)
# print(items)

def update_item(id=None,*args,**kwargs):
    obj=[i for i in items if i.get("id")==id][0]
    obj.update(kwargs)

update_item(id=102,name="ghee roast")

print()