# Description: A program that decides if a company gives a certian retirement gift to a worker depending on the the worker's age and some company requirements
# Contact: Akshay Rajaram; akshay.rajaram@temple.edu
#Date created: 5/21/2019
#Date Last Modified: 5/21/2019

age = int(input("What is the age of the retiree: "))
yearsWorked = int(input("How many years has the retiree worked at the company: "))

if age >=65:
    print("The retiree gets a gold watch.")
elif age<65 and yearsWorked>=25:
    print("The retiree will receive a silver watch.")
else:
    print("The retiree will receive a really nice pen.")
