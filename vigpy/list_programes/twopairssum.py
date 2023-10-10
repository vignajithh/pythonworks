#two pain of sum

list=[2,3,4,5]
sum=9
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        cur_sum=list[i]+list[j]
        if cur_sum==sum:
            print("paris")
