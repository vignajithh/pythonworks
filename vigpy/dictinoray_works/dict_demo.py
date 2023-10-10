mobile={"mobile name":"mi","price":10000,"offer":100}
# print(mobile["mobilename"])

# print(mobile["price"])

#add new key

# mobile["display"]="amoled"

# print(mobile)

# #to check weather key present in dict

# if "offer" in mobile:
#     print("exists")
# else:
#     print("not existts")

#if offer present add current offer price+50 else add offer as 50

if "offer" in mobile:
    mobile["offer"]+=50
else:
    mobile["offer"]=50

print(mobile)