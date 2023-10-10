orders=["vegmeals","fishmeals","vegmeals","fishmeals","vb","cb","bb","vb","cb","bb","bb","vb","fried rice"]

order_count={}

for items in orders:
    if items in order_count:
        order_count[items]+=1
    else:
        order_count[items]=1

print(order_count)