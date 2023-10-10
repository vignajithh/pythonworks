#50,20
#10
#50-10

def get_discound_price(actual_price,discound):
    sp=actual_price-(actual_price*discound)/100
    return sp
print(get_discound_price(50,10))