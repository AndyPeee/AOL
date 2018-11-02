#2. Write a function grade(percent), where percent is a number given as a percentage.
#The function will return a string that represents the letter grade for the percentage.
#Note: The function will return the string ‘error’ if the parameter is invalid.

#grade(65)
#returns ‘C’
#grade(93)
#returns ‘A +’
#grade(49)
#returns ‘F’

def grade_percent(grade):
    if int(grade) <= 49:
        print("You got an F")
        return "F"
    elif 50 >= int(grade) >= 64:
        print("You got a C")
        return "C"
    elif 65 >= int(grade) >= 79:
        print("You got a B")
        return "B"
    elif 80 >= int(grade) >= 94:
        print("You got an A")
        return "A"
    elif int(grade) >= 95:
        print("You got an A+!!!!")
        return "A+"


grade_percent(grade=int(input("What grade did you get? ")))

def doubleEven(n):
    if int(n) % 2 != 0:
        print(-1)
        return -1
    if int(n) % 2 == 0:
        n=int(n)*2
        print(n)
        return n
    else:
        print(-1)
        return -1


doubleEven(n=input("What number would you like? "))
