# count vowels

def count_vc(val): 
    v_count=0
    c_count=0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
           v_count=v_count+1
        else:
            c_count=c_count+1
    print("vowels",v_count)
    print("consonats",c_count)
x=input("enter a string: ")
count_vc(x)