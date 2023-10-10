lst=[4,5,6,7,8,2,1]

cubes=[n**3 for n in lst]

print(cubes)

evens=[n for n in lst if n%2==0]
print(evens)

odds=[n for n in lst if n%2!=0]
print(odds)

num_grtfive=[n for n in lst if n>=5]
print(num_grtfive)