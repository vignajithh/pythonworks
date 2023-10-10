num1=int(input("enter num1"))
num2=int(input("enter num2 must be <num1"))

for i in range(1,num2+1):
    if num1 %i==0 and num2 %i==0:
        hcf=i

print(hcf)  
