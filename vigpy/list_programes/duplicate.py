arr=[5,2,5,3,4,1,2]

#print duplicate numbers from arr
arr.sort()
for i in range(0,len(arr)-1):
    current=arr[i]
    next=arr[i+1]

    if current==next:
        print(current)
