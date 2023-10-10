#1800-2024

years=[y for y in range(1800,2025)]
# print(years)

#century years

century_years=[y for y in years if y%100==0]
# print(century_years)

#noncentury yaers

noncentury_years=[y for y in years if y%100!=0]
print(noncentury_years)