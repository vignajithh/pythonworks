from re import*
f=open("C:\\Users\\user\\Desktop\\vigpy\\regularexpression\\deata.txt")
phone_rule="\d{10}"
email_rule="[a-z][\w\W]+[@]gmail[.]com"
mail_id=[]
phone_num=[]

for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        p_matcher=fullmatch(phone_rule,w)
        e_matcher=fullmatch(email_rule,w)
        if p_matcher!=None:
            phone_num.append(w)
        elif e_matcher!=None:
            mail_id.append(w)

print(phone_num)
print(mail_id)