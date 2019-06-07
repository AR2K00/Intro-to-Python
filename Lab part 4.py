#Description: The purpose of this proram is in
#Contact Info:
#

from random import*
seed()
num1 = randint(0, 9)
num2 = randint(0, 9)
num3 = randint(0, 9)
print("Numbers: ", num1, num2, num3)
answer = 'Y'
while answer == 'Y':
    if ((num1 == num2) or (num1 == num3) or (num2 == num3)) and (not((num1 == num2 and num2 == num3))):
        print("You have two matching numbers!")
    elif num1 == num2 == num3:
        print("You have three matching numbers!")
    else:
        print("You have no matching numbers.")
    answer = input("Do you want to play, press Y if yes: ")


print("Thanks for playing!")