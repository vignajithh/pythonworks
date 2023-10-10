
for row in range(1,7):
    for sp in range(1,7-row,):
        print( end="")
    for sp in range(row):
        print("*",end="")
    print()