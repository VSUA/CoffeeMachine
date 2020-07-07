array = list()
big_amount_of_cats = ["", 0]

while True:
    name = input().strip()
    if name == "MEOW":
        break
    else:
        array.append(name.split())

for cafe in array:
    if int(cafe[1]) > int(big_amount_of_cats[1]):
        big_amount_of_cats = cafe
else:
    print(big_amount_of_cats[0])
