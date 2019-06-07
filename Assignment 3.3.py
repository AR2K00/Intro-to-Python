#Description: A program that asks a user to enter a set of student grades and reports the total number of grades entered, the lowest grade, the highest grade, and the mean grade
#Contact: Akshay Rajaram; akshay.rajaram@temple.edu
#Date Created: 6/3/2019; Date Last Modified: 6/5/2019
#Date Due: 6/5/2019

grade = 0
total = 0
endCount = int(input("How many grades will you be adding:"))
lowestNum = 0
highestNum = 0
count = 0
while grade >= 0 and endCount > 0:
    grade = float(input("What is the grade, put -1 to stop: "))
    if grade >= 0:
        total += grade
        endCount -= 1
        count += 1
        if count == 1:
            highestNum = grade
            lowestNum = grade
        else:
            if grade > highestNum:
                highestNum = grade
            if grade < lowestNum:
                lowestNum = grade
if count > 0:
    mean = total/count
    print("The total number of grades entered is ", count)
    print("The lowest grade is ", lowestNum)
    print("The highest grade is ", highestNum)
    print("The mean grade is ", mean)
else:
    print("No grade was entered")
