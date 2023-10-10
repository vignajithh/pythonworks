text="abcdab"
wc={}
for ch in text:
    if ch in wc:
        print(ch ,"is the first recersive chacter")
        break
    else:
        wc[ch]=1