#find least +ve missing integer
arr=[1,3,4,6,5]

arr.sort()
for i in range(0,len(arr)-1):
    cur=arr[i]
    nex=arr[i+1]
    if nex-cur !=1:
        print(cur+1,"is missing")
        break




