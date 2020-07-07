scores = input().split()
# put your python code here
amount_correct_answers = 0
amount_incorrect_answers = 0
for answer in scores:
    if answer == "C":
        amount_correct_answers += 1
    else:
        amount_incorrect_answers += 1
        if amount_incorrect_answers >= 3:
            print("Game over")
            print(amount_correct_answers)
            break
else:
    print("You won")
    print(amount_correct_answers)