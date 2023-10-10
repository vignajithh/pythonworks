#first three charactes must be upper case radon alphabets
#4t place must be alphabet (PCFHTA)
#5th place any randon uppercase alphabets
#4digit
#one alphabet

from re import*

pan_num=input("enter the pan number:>")

rule="[A-Z]{3}[PCFHTA]{1}[A-Z]{1}[\d]{4}[A-Z]{1}"

matcher=fullmatch(rule,pan_num)
print("invalid" if matcher==None else "valid")