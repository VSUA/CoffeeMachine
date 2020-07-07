array = list()
while True:
    number = input()
    if number == ".":
        break
    else:
        array.append(float(number))

print(min(array))