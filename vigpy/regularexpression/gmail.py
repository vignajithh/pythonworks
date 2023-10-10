


from re import*

gamil_id=input("enter gmail id:>")

rule="[a-z0-9]+[@]gmail[.]com"
matcher=fullmatch(rule,gamil_id)
print("invald" if matcher==None else "valid")