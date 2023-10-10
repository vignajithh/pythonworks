enquires=["django","testing","django","bigdata","testing","php","testing","bigdata"]

enq_count={}
 
for enq in enquires:
    if enq in enq_count:
        enq_count[enq]+=1
    else:
        enq_count[enq]=1
print(enq_count)