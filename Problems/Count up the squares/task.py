# put your python code here
sum = 0
sum_of_squeres = 0

while True:
    number = int(input())
    sum += number
    sum_of_squeres += number * number

    if sum == 0:
        print(sum_of_squeres)
        break