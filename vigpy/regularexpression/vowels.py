text="aaadaaaaaaffhgfaaaaa" 

#print all vowles using re

from re import *

# pattern="[aeiou]"

#consanants
# pattern="[^aeiou\W\d]"

#one or more cahracters
# pattern="a+"

#0 OR MORE CHARACTERS
# pattern="a*"

#min1 number max 2 num
pattern="a{1,2}"


matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())