#2. Write a function grade(percent), where percent is a number given as a percentage.
#The function will return a string that represents the letter grade for the percentage.
#Note: The function will return the string ‘error’ if the parameter is invalid.

#grade(65)
#returns ‘C’
#grade(93)
#returns ‘A +’
#grade(49)
#returns ‘F’

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
