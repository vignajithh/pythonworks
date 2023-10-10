text="cofeekjgheiorgy9iwerygowi"

# for ch in text:
#     if ch in["a","e","i","o","u"]:
#         print(ch)

v_count=0
c_count=0

for ch in text:
    if ch in ["a","e","i","o","u"]:
        v_count+=1
    else:
        c_count+=1

print("vowels",v_count)
print("constnats",c_count)
              