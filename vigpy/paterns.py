#   #   #
#   #   #
#   #   #

# for row in range(1,4):
#     for column in range(1,4):
#         print("#",end="\t")
#     print()


# 1
# 1   2
# 1   2   3

# for row in range(1,4):
#     for column in range(row):
#         print(column+1,end="\t")
#     print()


# 1
# 1  #
# 1  #  3  #
# 1  #  3  #  5
# 1  #  3  #  5  #

for row in range(1,7):
    for column in range(row):
        val=column+1
        if val%2==0:
            print("#",end="\t")
        else:
            print(val,end="\t")    
    print()