number = int(input())
amount_of_divisiors = 0

for i in range(1, number + 1):
    if (number % i) == 0:
        amount_of_divisiors += 1

if number > 1 and amount_of_divisiors == 2:
    print("This number is prime ")
else:
    print("This number is not prime")