from json import load
path="C:\\Users\\user\\Desktop\\vigpy\\read_json\\data.json"

with open(path) as f:
    records=load(f)
#     print(records)


# fw_names=[f.get('name') for f in records]
# print(fw_names)

top_fw=max(records,key=lambda d:d.get("rating"))
# print(top_fw)

#print python frame works
#backend frameworks

p_works=[f.get("language") for f in records]
print(p_works)

