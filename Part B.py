#2. Write a function grade(percent), where percent is a number given as a percentage.
#The function will return a string that represents the letter grade for the percentage.
#Note: The function will return the string ‘error’ if the parameter is invalid.

def plusorminus(grade):
    if int(grade) % 10 in [1, 2, 3]:
        return " - "
    elif int(grade) % 10 in [7,8,9]:
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
    elif int(grade)>=91:
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


doubleven(n=input("What number would you like? "))
grade_percent(grade=int(input("What grade did you get? ")))


def diceroll(num1, num2, num3):
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

diceroll(num1=input("What number do you want? "), num2=input("What number do you want? "), num3=input("What number do you want? "))

#Write a function sumDice(Dice, numRolls),
# where Dice simulate a dice of Dice sides and numRolls represent the number of times the dice is rolled.
# The function will return the sum of rolling the dice numRolls times..
#sumDice(4, 3) returns 6
# (although, the answer may vary as a four sided dice is rolled three times and the sum is returned.).
