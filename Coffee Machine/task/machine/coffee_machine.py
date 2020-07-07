# Write your code here

# STAGE 2
# MASS_WATER = 200
# MASS_MILK = 50
# MASS_BEANS = 15
# number_of_cups = int(input("Write how many cups of coffee you will need:"))
# print("For" + str(number_of_cups) + "cups of coffee you will need:")
# print(number_of_cups * MASS_WATER, "ml of water")
# print(number_of_cups * MASS_MILK, "ml of milk")
# print(number_of_cups * MASS_BEANS, "g of coffee beans")

# STAGE 3
# MASS_WATER = 200
# MASS_MILK = 50
# MASS_BEANS = 15
# print("Write how many ml of water the coffee machine has:")
# avaliable_water = int(input())
# print("Write how many ml of milk the coffee machine has:")
# avaliable_milk = int(input())
# print("Write how many grams of coffee beans the coffee machine has:")
# avaliable_beans = int(input())
# print("Write how many cups of coffee you will need:")
# wish_cup = int(input())
#
# max_cups_water = avaliable_water // MASS_WATER
# max_cups_milk = avaliable_milk // MASS_MILK
# max_cups_beans = avaliable_beans // MASS_BEANS
# max_amount_of_cups = min(max_cups_milk, max_cups_beans, max_cups_water)
#
# if max_amount_of_cups > wish_cup:
#     print("Yes, I can make that amount of coffee (and even "
#           + str(max_amount_of_cups - wish_cup) + " more than that)")
# elif max_amount_of_cups == wish_cup:
#     print("Yes, I can make that amount of coffee")
# elif max_amount_of_cups < wish_cup:
#     print("No, I can make only " + str(max_amount_of_cups) + " cups of coffee")

# STAGE 4
# ESPRESSO_WATER = 250
# ESPRESSO_BEANS = 16
# ESPRESSO_PRICE = 4
#
# LATTE_WATER = 350
# LATTE_MILK = 75
# LATTE_BEANS = 20
# LATTE_PRICE = 7
#
# CAPPUCCINO_WATER = 200
# CAPPUCCINO_MILK = 100
# CAPPUCCINO_BEANS = 12
# CAPPUCCINO_PRICE = 6
#
# def avaliable_products():
#     print("The coffee machine has:")
#     print(str(avaliable_water) + " of water")
#     print(str(avaliable_milk) + " of milk")
#     print(str(avaliable_beans) + " of coffee beans")
#     print(str(avaliable_cups) + " of disposable cups")
#     print(str(avaliable_money) + " of money")
#
# def buy_coffee():
#     global avaliable_water
#     global avaliable_milk
#     global avaliable_beans
#     global avaliable_cups
#     global avaliable_money
#
#     number = int(input("What do you want to buy? 1 - espresso, 2 - latte, "
#                        "3 - cappuccino:"))
#
#     if number == 1:
#         if avaliable_water >= ESPRESSO_WATER and avaliable_beans >= ESPRESSO_BEANS and avaliable_cups >= 1:
#             avaliable_water -= ESPRESSO_WATER
#             avaliable_beans -= ESPRESSO_BEANS
#             avaliable_cups -= 1
#             avaliable_money += ESPRESSO_PRICE
#     elif number == 2:
#         if avaliable_water >= LATTE_WATER and avaliable_milk >= LATTE_MILK and avaliable_beans >= LATTE_BEANS and avaliable_cups >= 1:
#             avaliable_water -= LATTE_WATER
#             avaliable_milk -= LATTE_MILK
#             avaliable_beans -= LATTE_BEANS
#             avaliable_cups -= 1
#             avaliable_money += LATTE_PRICE
#     elif number == 3:
#         if avaliable_water >= CAPPUCCINO_WATER and avaliable_milk >= CAPPUCCINO_MILK and avaliable_beans >= CAPPUCCINO_BEANS and avaliable_cups >= 1:
#             avaliable_water -= CAPPUCCINO_WATER
#             avaliable_milk -= CAPPUCCINO_MILK
#             avaliable_beans -=CAPPUCCINO_BEANS
#             avaliable_cups -= 1
#             avaliable_money += CAPPUCCINO_PRICE
#
# def fill_machine():
#     global avaliable_water
#     global avaliable_milk
#     global avaliable_beans
#     global avaliable_cups
#
#     avaliable_water +=  int(input("Write how many ml of water do you want to add:"))
#     avaliable_milk += int(input("Write how many ml of milk do you want to add:"))
#     avaliable_beans += int(input("Write how many grams of coffee beans do you want to add:"))
#     avaliable_cups += int(input("Write how many disposable cups of coffee do you want to add:"))
#
# def take_money():
#     global avaliable_money
#     print("I gave you $" + str(avaliable_money))
#     avaliable_money = 0
#
# avaliable_water = 400
# avaliable_milk = 540
# avaliable_beans = 120
# avaliable_cups = 9
# avaliable_money = 550
#
# avaliable_products()
#
# action = input("Write action (buy, fill, take) :").strip()
# if action == "buy":
#     buy_coffee()
# elif action == "fill":
#     fill_machine()
# elif action == "take":
#     take_money()
#
# avaliable_products()

# STAGE 6
# ESPRESSO_WATER = 250
# ESPRESSO_BEANS = 16
# ESPRESSO_PRICE = 4
#
# LATTE_WATER = 350
# LATTE_MILK = 75
# LATTE_BEANS = 20
# LATTE_PRICE = 7
#
# CAPPUCCINO_WATER = 200
# CAPPUCCINO_MILK = 100
# CAPPUCCINO_BEANS = 12
# CAPPUCCINO_PRICE = 6
#
# def avaliable_products():
#     print("The coffee machine has:")
#     print(str(avaliable_water) + " of water")
#     print(str(avaliable_milk) + " of milk")
#     print(str(avaliable_beans) + " of coffee beans")
#     print(str(avaliable_cups) + " of disposable cups")
#     print(str(avaliable_money) + " of money")
#
# def buy_coffee():
#     global avaliable_water
#     global avaliable_milk
#     global avaliable_beans
#     global avaliable_cups
#     global avaliable_money
#
#     number = input("What do you want to buy? 1 - espresso, 2 - latte, "
#                        "3 - cappuccino, back - to main menu:")
#
#     if number == "1":
#         if avaliable_water >= ESPRESSO_WATER and avaliable_beans >= ESPRESSO_BEANS and avaliable_cups >= 1:
#             avaliable_water -= ESPRESSO_WATER
#             avaliable_beans -= ESPRESSO_BEANS
#             avaliable_cups -= 1
#             avaliable_money += ESPRESSO_PRICE
#         else:
#             print("I have enough resources, making you a coffee!")
#     elif number == "2":
#         if avaliable_water >= LATTE_WATER and avaliable_milk >= LATTE_MILK and avaliable_beans >= LATTE_BEANS and avaliable_cups >= 1:
#             avaliable_water -= LATTE_WATER
#             avaliable_milk -= LATTE_MILK
#             avaliable_beans -= LATTE_BEANS
#             avaliable_cups -= 1
#             avaliable_money += LATTE_PRICE
#         else:
#             print("I have enough resources, making you a coffee!")
#     elif number == "3":
#         if avaliable_water >= CAPPUCCINO_WATER and avaliable_milk >= CAPPUCCINO_MILK and avaliable_beans >= CAPPUCCINO_BEANS and avaliable_cups >= 1:
#             avaliable_water -= CAPPUCCINO_WATER
#             avaliable_milk -= CAPPUCCINO_MILK
#             avaliable_beans -=CAPPUCCINO_BEANS
#             avaliable_cups -= 1
#             avaliable_money += CAPPUCCINO_PRICE
#         else:
#             print("I have enough resources, making you a coffee!")
#     elif number == "back":
#         pass
#
# def fill_machine():
#     global avaliable_water
#     global avaliable_milk
#     global avaliable_beans
#     global avaliable_cups
#
#     avaliable_water +=  int(input("Write how many ml of water do you want to add:"))
#     avaliable_milk += int(input("Write how many ml of milk do you want to add:"))
#     avaliable_beans += int(input("Write how many grams of coffee beans do you want to add:"))
#     avaliable_cups += int(input("Write how many disposable cups of coffee do you want to add:"))
#
# def take_money():
#     global avaliable_money
#     print("I gave you $" + str(avaliable_money))
#     avaliable_money = 0
#
# avaliable_water = 400
# avaliable_milk = 540
# avaliable_milk = 120
# avaliable_cups = 9
# avaliable_money = 550
#
# while True:
#     action = input("Write action (buy, fill, take, remaining, exit) :").strip()
#     if action == "buy":
#         buy_coffee()
#     elif action == "fill":
#         fill_machine()
#     elif action == "take":
#         take_money()
#     elif action == "remaining":
#         avaliable_products()
#     elif action == "exit":
#         break


ESPRESSO_WATER = 250
ESPRESSO_BEANS = 16
ESPRESSO_PRICE = 4

LATTE_WATER = 350
LATTE_MILK = 75
LATTE_BEANS = 20
LATTE_PRICE = 7

CAPPUCCINO_WATER = 200
CAPPUCCINO_MILK = 100
CAPPUCCINO_BEANS = 12
CAPPUCCINO_PRICE = 6

class CofeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.avaliable_water = water
        self.avaliable_milk = milk
        self.avaliable_beans = beans
        self.avaliable_cups = cups
        self.avaliable_money = money

    def avaliable_products(self):
        print("The coffee machine has:")
        print(str(self.avaliable_water) + " of water")
        print(str(self.avaliable_milk) + " of milk")
        print(str(self.avaliable_beans) + " of coffee beans")
        print(str(self.avaliable_cups) + " of disposable cups")
        print(str(self.avaliable_money) + " of money")

    def buy_coffee(self):

        number = input("What do you want to buy? 1 - espresso, 2 - latte, "
                       "3 - cappuccino, back - to main menu:")

        if number == "1":
            if self.avaliable_water >= ESPRESSO_WATER and self.avaliable_beans >= ESPRESSO_BEANS and self.avaliable_cups >= 1:
                self.avaliable_water -= ESPRESSO_WATER
                self.avaliable_beans -= ESPRESSO_BEANS
                self.avaliable_cups -= 1
                self.avaliable_money += ESPRESSO_PRICE
            else:
                print("I have enough resources, making you a coffee!")
        elif number == "2":
            if self.avaliable_water >= LATTE_WATER and self.avaliable_milk >= LATTE_MILK and self.avaliable_beans >= LATTE_BEANS and self.avaliable_cups >= 1:
                self.avaliable_water -= LATTE_WATER
                self.avaliable_milk -= LATTE_MILK
                self.avaliable_beans -= LATTE_BEANS
                self.avaliable_cups -= 1
                self.avaliable_money += LATTE_PRICE
            else:
                print("I have enough resources, making you a coffee!")
        elif number == "3":
            if self.avaliable_water >= CAPPUCCINO_WATER and self.avaliable_milk >= CAPPUCCINO_MILK and self.avaliable_beans >= CAPPUCCINO_BEANS and self.avaliable_cups >= 1:
                self.avaliable_water -= CAPPUCCINO_WATER
                self.avaliable_milk -= CAPPUCCINO_MILK
                self.avaliable_beans -= CAPPUCCINO_BEANS
                self.avaliable_cups -= 1
                self.avaliable_money += CAPPUCCINO_PRICE
            else:
                print("I have enough resources, making you a coffee!")
        elif number == "back":
            pass

    def fill_machine(self):

        self.avaliable_water += int(input("Write how many ml of water do you want to add:"))
        self.avaliable_milk += int(input("Write how many ml of milk do you want to add:"))
        self.avaliable_beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.avaliable_cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take_money(self):

        print("I gave you $" + str(self.avaliable_money))
        self.avaliable_money = 0

    def start_machine(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit) :").strip()
            if action == "buy":
                self.buy_coffee()
            elif action == "fill":
                self.fill_machine()
            elif action == "take":
                self.take_money()
            elif action == "remaining":
                self.avaliable_products()
            elif action == "exit":
                break


coffee_machine = CofeeMachine(400, 540, 120, 9, 550)
coffee_machine.start_machine()