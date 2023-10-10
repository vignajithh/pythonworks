
#starts with KL
#2 digit
#alphabet min 1 max 2
#4 digit





from re import*
vehicle_num=input("enter vehicle num>")

rule="(KL)-[\d]{2}-[A-Z]{1,2}-[\d]{4}"

matcher=fullmatch(rule,vehicle_num)
print("in valid" if matcher==None else "valid")
