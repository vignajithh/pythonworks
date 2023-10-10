#3digit
#/
#2digitR
#2digit
#/
#2digitalphabet

from re import*
tyre_code=input("enter the ttrye code>")
rule="[\d]{3}/[\d]{2}[R][\d]{2}/[\d]{2}[A-z]"
matcher=fullmatch(rule,tyre_code)
print("invalid" if matcher==None else "valid")