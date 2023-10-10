text="hi hellom hai goodafternoon zython"

words=text.split(" ")

#longest word
# l_word=max(words,key=lambda w:len(w))

# print(l_word)

#sort

srt=sorted(words,reverse=True,key=lambda w:len(w))
print(srt)