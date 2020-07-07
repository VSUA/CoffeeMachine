# put your python code here
array = list()
while True:
    number = int(input())

    if 10 <= number <= 100:
        array.append(number)
    elif number > 100:
        break

for number in array:
    print(number)