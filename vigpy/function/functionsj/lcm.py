#lcm

def least_common_multiple(n1,n2):
    max=n1 if n1>n2 else n2
    flag=True

    while(flag):
        if max%n1==0 and max%n2==0:
            print(f"lcm of{n1},{n2} is {max}")
            break
        else:
            max+=1
least_common_multiple(30,25) 