def smart_sub(a,b):
    # if a>b:
    #     return a-b
    # else:
    #     return b-a
    return a-b if a<b else b-a
    
print(smart_sub(20,50))
print(smart_sub(50,20))