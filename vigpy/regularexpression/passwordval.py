#atleast one uppercase
#atealst 1 special character
#min 8 char
#atlest 1 digit
#
from re import*
password="Password@123"

rule="(?=.*[A-Z])(?=.*[\W](?=.*[\d])).{8,}"

matcher=fullmatch(rule,password)

print("invald" if matcher==None else "valid")
