import random


def plusorminus(grade):
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
        print("You got a D" + plusorminus(grade))
        return "D" + str(plusorminus(grade))
    if 61 <= int(grade) <= 70:
        plusorminus(grade)
        print("You got a C" + str(plusorminus(grade)))
        return "C" + str(plusorminus(grade))
    elif 71 <= int(grade) <= 80:
        plusorminus(grade)
        print("You got a B" + str(plusorminus(grade)))
        return "B" + str(plusorminus(grade))
    if 81 <= int(grade) <= 90:
        plusorminus(grade)
        print("You got an A")
        return "A" + str(plusorminus(grade))
    elif int(grade) >= 91:
        print("You got an A plus")
        return "A +"


def doubleven(n):
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


def highestnumber(num1, num2, num3):
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


def sumdice(dice, numrolls):
    amount = 0
    for x in range(0, int(numrolls)):
        amount = int(amount) + random.randint(1, dice)
    print(amount)
    return amount


doubleven(n=input("What number would you like? "))
grade_percent(grade=int(input("What grade did you get? ")))


highestnumber(num1=input("What number do you want? "), num2=input("What number do you want? "), num3=input("What number do you want? "))


sumdice(dice=int(input("How many sides are on the dice? ")), numrolls=int(input("How many times do you want to roll this dice? ")))