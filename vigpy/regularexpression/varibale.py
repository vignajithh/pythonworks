from re import*

variable=input("enetr a variable name")

rule="[a-zA-Z][0-9a-zA-Z_]*"

matcher=fullmatch(rule,variable)
print("invalid" if matcher==None else "valid")