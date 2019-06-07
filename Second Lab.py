#Description: Calculate the area of the triangle using Heron's Formula
#Contact: Akshay Rajaram; akshay.rajaram@temple.edu
#Date Created: 5/16/2019
#Date Last Modified: 5/16/2019

import math

a = int(input("What length is side X of the triangle?: "))
b = int(input("What length is side Y of the triangle?: "))
c = int(input("What length is side Z of the triangle?: "))
s = (a+b+c)/2
triangleArea = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle with sides", a, ",", b, ", and", c, "is", triangleArea)