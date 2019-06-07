# Description: A program to calculate the area of geometric shapes
# Contact : akshay.rajaram@temple.edu
# Date created: 2019-05-14
# Date last modified: 2019-05-14
# Area of the square

squareSide = int(input("Enter the side of the square: "))
squareArea = squareSide *squareSide
print("The area of the square with side", squareSide, "is:", squareArea)

# Area of the isosceles triangle
triangleHeight = int(input("Enter the height of the triangle:"))
triangleBase = int(input("Enter the base of the triangle:"))
triangleArea = 0.5*triangleBase*triangleHeight
print("The area of the triangle with base", triangleBase,"and height", triangleHeight,"is:", triangleArea)

# Area of circle
pi=3.14159
circleDiameter = int(input("Enter the diameter of the circle:"))
circleRadius = 0.5*circleDiameter
circleArea = pi*circleRadius*circleRadius
print("The radius of the circle wih diameter", circleDiameter, "is", circleRadius)
print("The area of the circle with diameter", circleDiameter, "is", circleArea)





