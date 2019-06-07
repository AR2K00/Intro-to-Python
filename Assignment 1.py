#Description: Change Maker program for use to calculate the combination of coins that will give the correct change
#Contact: Akshay Rajaram; akshay.rajaram@temple.edu
#Date Created: 5/16/2019
#Date Last Modified: 5/16/2019

import math

amountPrice = int(input("What is the price of the item?: "))
amountPaid = int(input("What is the amount that was paid?: "))

changeLeft = amountPaid - amountPrice

print("Change required:", changeLeft)

a = changeLeft//25  #find the whole number of times the change can be divided by 25 to find number of quarters
aRemainder = changeLeft%25  #use the remainder operator and then divide that by 10 for dimes (then continue)
b = aRemainder//10
bRemainder = aRemainder%10
c = bRemainder//5
cRemainder = bRemainder%5
d = cRemainder//1

print(changeLeft, "cents in coins can be given as:", a, "quarters,", b,"dimes,", c, "nickels, and", d, "pennies.")

