# Description: Determines the type of triangle and calculates the area
# Contact: Akshay Rajaram; akshay.rajaram@temple.edu
# Date created: 5/21/2019
# Date Last Modified: 5/28/2019
# Due: 5/28/2019
import math
a = float(input("What is the length of the first side: "))
b = float(input("What is the length of the second side: "))
c = float(input("What is the length of the third side: "))

if (a<(b+c) and b<(a+c) and c<(a+b)):
    if a == b ==c:
        print("The triangle is an equilateral triangle.")
    elif ((a**2)+(b**2)==(c**2)) or((c**2)+(b**2)==(a**2))or ((a**2)+(c**2)==(b**2)):
        print("The triangle is a right triangle.")
    elif ((a**2)+(b**2)<(c**2))or((a**2)+(c**2)<(b**2))or((c**2)+(b**2)<(a**2)):
        print("The triangle is an obtuse triangle.")
    else:
        print("The triangle is an acute triangle.")
    if (a == b or a == c or b == c) and (not((a == b == c))):
        print("The triangle is an isosceles triangle.")
    s = 1/2*(a+b+c)
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the triangle is: ",area)

else :
    print("The given sides do not create a valid triangle.")
