text="hello hai hello hai"
words=text.split(" ")
txt={}
for tx in words:
    if tx in txt:
        txt[tx]+=1
    else:
        txt[tx]=1
print(txt)