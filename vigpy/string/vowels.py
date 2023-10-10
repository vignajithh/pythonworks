text='pythonis is a programming languge'

vowels=("a","e","i","o","u")
words=text.split(" ")

for w in words:
    if w.casefold().startswith(vowels):
        print(w)