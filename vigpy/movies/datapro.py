from json import load
path="C:\\Users\\user\\Desktop\\vigpy\\read_json\\mdb.json"

with open(path,encoding="utf-8")as f:
    filims=load(f)

    #print total number of filims

    print(len(filims))

    #print all movies released in 2015

movie_filter=[f.get("title") for f in filims if f.get("year")=="2015"]
    # print(movie_filter)

    #print comedy genere movies

com_mov=[f.get("title") for f in filims if "Comedy" in f.get("genres")]
# print(com_mov)

#id in range(20,30) and runtime >110

f_fil=[f.get("title") for f in filims if f.get("id") in range(10,21) and f.get("runtime")>="110"]
# print(f_fil)


#print movies with single word title

title_filter=[f.get("title") for f in filims if len(f.get("title").split(" "))==1]
# print(title_filter)

#print genres=drama which has hiogest runtime

drama_flm=[f for f in filims if "Drama"in f.get("genres")]
longest_filim=max(drama_flm,key=lambda f:int(f.get("runtime")))
# print(longest_filim)

#print all genres

#in which year more movies relesed

wc={}

for m in filims:
    year=m.get("year")

    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1

out=max(wc,key=lambda k:wc.get(k))
# print(out)

print(max((v,k) for k,v in wc.items()))
