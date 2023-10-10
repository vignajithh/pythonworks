f=open("C:\\Users\\user\\Desktop\\vigpy\\fileoperaton\\numbers.txt")
all_numbers=[line.rstrip("\n") for line in f]
# print(all_numbers)

kerala_num=[num for num in all_numbers if num.startswith("kl")]
print(kerala_num)