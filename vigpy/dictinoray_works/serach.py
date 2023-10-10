lst=[12,14,16,18,20]

element=16
i=0
stop=len(lst)
is_found=False

while(i<stop):
    cur_value=lst[i]
    if cur_value==element:
        is_found=True
        break
    i+=1

print(is_found)