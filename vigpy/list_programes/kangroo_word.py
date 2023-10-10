sorce_word="chicken"
target_word="hen"
kangroo_string=""
sorce_wordd=[]

for ch in sorce_word:
    if ch in sorce_word:
        sorce_wordd.append(ch)
for ch in target_word:
    if ch in sorce_word:
        sorce_wordd.pop(sorce_wordd.index(ch))
        kangroo_string+=ch

print(kangroo_string==target_word)
    



