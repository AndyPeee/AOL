import random


def plus_or_minus(grade):
    if int(grade) % 10 in [1, 2, 3]:
        return " - "
    elif int(grade) % 10 in [7, 8, 9]:
        return " + "
    else:
        return " "


def grade_percent(grade):
    if 0 <= int(grade) <= 49:
        print("You got an F")
        return "F"
    elif 50 <= int(grade) <= 60:
        print("You got a D" + plus_or_minus(grade))
        return "D" + str(plus_or_minus(grade))
    if 61 <= int(grade) <= 70:
        plus_or_minus(grade)
        print("You got a C" + str(plus_or_minus(grade)))
        return "C" + str(plus_or_minus(grade))
    elif 71 <= int(grade) <= 80:
        plus_or_minus(grade)
        print("You got a B" + str(plus_or_minus(grade)))
        return "B" + str(plus_or_minus(grade))
    if 81 <= int(grade) <= 90:
        plus_or_minus(grade)
        print("You got an A")
        return "A" + str(plus_or_minus(grade))
    elif int(grade) >= 91:
        print("You got an A +")
        return "A +"


def double_even(n):
    if int(n) % 2 != 0:
        print(-1)
        return -1
    if int(n) % 2 == 0:
        n = int(n)*2
        print(n)
        return n
    else:
        print(-1)
        return -1


def highest_number(num1, num2, num3):
    if int(num1) > int(num2) and int(num1) > int(num3):
        print(num1)
        return num1
    elif int(num2) > int(num1) and int(num2) > int(num3):
        print(num2)
        return num2
    if int(num3) > int(num1) and int(num3) > int(num2):
        print(num3)
        return num3
    elif int(num1) == int(num2) == int(num3):
        print(num1)
        return num1
    if int(num1) == int(num2) and int(num1) > int(num3):
        print(num1)
        return num1
    elif int(num3) == int(num2) and int(num3) > int(num1):
        print(num3)
        return num3
    if int(num1) == int(num3) and int(num1) > int(num2):
        print(num1)
        return num1


def sum_of_dice(dice, numrolls):
    amount = 0
    for x in range(0, int(numrolls)):
        amount = int(amount) + random.randint(1, dice)
    print(amount)
    return amount


double_even(n=input("What number would you like? "))
grade_percent(grade=int(input("What grade did you get? ")))
highest_number(num1=input("What do you want as your first number?? "), num2=input("What do you want as your second number? "), num3=input("What do you want as your third number? "))
sum_of_dice(dice=int(input("How many sides are on the dice? ")), numrolls=int(input("How many times do you want to roll this dice? ")))