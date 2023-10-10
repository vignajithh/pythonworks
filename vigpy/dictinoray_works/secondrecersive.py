text="abacdce"

wc={}
dup_lst=[]
for ch in text:
    if ch in wc:
        dup_lst.append(ch)
    else:
        wc[ch]=1
print(dup_lst[1])

non_dup=[]

dup_lst=[]

for ch in text:
    if ch in non_dup:
        non_dup.append(ch)
    else:
        dup_lst.append(ch)

print(dup_lst[1])
