num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
def max(a,b,c):
    if a>b and a>c:
        print("num1 is greatest", a)
    elif b>a and b>c:
        print("num2 is greatest", b)
    else:    
        print("largesst is c", c)

max(num1,num2,num3)
