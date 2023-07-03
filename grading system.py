counter = 0
gpa = 0
letterGrades = ""

while counter >= 0:
    score = input("Enter an integer score or press 'Enter' to finish calculation: ")
    if score.isdigit():
        if 0 <= int(score) <= 100:
            counter = counter + 1
            if int(score) < 60:
                letterGrades += "F"
                gpa = gpa
            elif 60 <= int(score) < 70:
                letterGrades += "D"
                gpa = gpa + 1
            elif 70 <= int(score) < 80:
                letterGrades += "C"
                gpa = gpa + 2
            elif 80 <= int(score) < 90:
                letterGrades += "B"
                gpa = gpa + 3
            else:
                letterGrades += "A"
                gpa = gpa + 4

        else:
            print("Input is out of the valid range.")
    elif score == "":
        if counter == 0:
            print("Error no input")
        else:
            print("Total number of students is =", counter)
            print("Their letter grades are")
            for grades in letterGrades:
                print(grades, end=" , ")
            print("the average gpa = ", gpa / counter)