#Description: Converts grades into letter grades
#Contact info: Akshay Rajaram; akshay.rajaram2000@gmail.com
#

grade = int(input("What is the number grade: "))

if grade<=100 and grade>=0:
    if grade >90 and grade<=100:
        print("The letter grade is A.")
    elif grade >=80 and grade<90:
        print("The letter grade is B.")
    elif grade >=70 and grade<80:
        print("The letter grade is C.")
    elif grade>=60 and grade<70:
        print("The letter grade is D.")
    elif grade>=0 and grade<60:
        print("The letter grade is F.")
else:
    print("The number grade is invalid.")