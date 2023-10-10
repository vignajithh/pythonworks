# 1  1  1
# 2  2  2
# 3  3  3

# for row in range(1,4):
#     for column in range(1,4):
#         print(row,end="\t")
#     print()

    #trangle

for row in range(4,0,-1):
    for col in range(row):
        print("#", end="\t")
    print()