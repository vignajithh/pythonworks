from re import *

text="python @ 123"
# pattern="[a-z]" #lowercase
# pattern="[A-Z]" #uppercare
# pattern="[a-zA-Z0-9]" #alphanumaric
# pattern="[0-9]" #numbwr

#predefined characters
# pattern="\d" #[0-9]
# pattern="\D" #[^0-9]
# pattern="\w" #alphabets and numbers #[a-zA-Z0-9]
pattern="\W" #special characters

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())

