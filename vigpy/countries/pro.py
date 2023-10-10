from json import load

path="C:\\Users\\user\\Desktop\\vigpy\\countries\\countries.json"
with open(path,encoding="utf-8") as f:
    countries=load(f)

# print(len(countries))    

country_names=[c.get("name") for c in countries ]
# print(country_names)

#capital of china
country_capital=[c.get("capital") for c in countries if c.get("name")=="China"]
# print(country_capital)

#print regions

county_region={c.get("region") for c in countries }
# print(county_region)

#india borders

# country_borders=[c.get("borders") for c in countries if c.get("name")=="India"][0]

# border_name=[c.get("name") for c in countries if c.get("alpha3Code") in country_borders]
# print(border_name)


#print indipendent country names
#print currency of india
#

currency_details=[c.get("currencies") for c in countries if c.get("name")=="India"][0][0]
# print(currency_details.get("name"))

country_curriencies=[c for c in countries if "currencies" in c]
currencies=[c.get("currencies")[0].get("symbol") for c in country_curriencies]
wc={}
for c in currencies:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1

print(max((v,k)for k,v in wc.items()))
