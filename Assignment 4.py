

# call function that is called menu
selection = 0
grade = 0
total = 0
lowestNum = 0
highestNum = 0
count = 0
daList = list()
while selection <= 3:
    print("Welcome to the menu", '\n', "1. Enter new grades", '\n', "2. Print all grades entered so far", '\n',
    "3. Print a report", '\n', "4: Exit")
    selection = int(input("Please select one of the above: "))
    if selection == 1:
        endCount = int(input("How many grades will you be adding:"))
        while grade >= 0 and endCount > 0:
            grade = float(input("What is the grade, put -1 to stop: "))
            if grade >= 0:
                total += grade
                endCount -= 1
                count += 1
                daList.append(grade)
                if count == 1:
                    highestNum = grade
                    lowestNum = grade
                    daList.append(grade)
                else:
                    if grade > highestNum:
                        highestNum = grade
                    if grade < lowestNum:
                        lowestNum = grade
    elif selection == 3:
        if count > 0:
            mean = total / count
            print("The total number of grades entered is ", count)
            print("The lowest grade is ", lowestNum)
            print("The highest grade is ", highestNum)
            print("The mean grade is ", mean)
        else:
            print("No grade was entered")
    elif selection == 2:
        if count >0:
            print(daList)
        else:
            print("No grade was entered")
