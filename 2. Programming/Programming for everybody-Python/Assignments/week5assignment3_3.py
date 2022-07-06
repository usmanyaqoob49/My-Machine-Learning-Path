#Write a program to prompt for a score between 0.0 and 1.0.
#If the score is out of range, print an error.
#If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit.
#For the test, enter a score of 0.85.
score = input("Enter score bwtween 0.0 and 1.0: ")
try:
    score = float(score)
except:
    print("Please enter float values or integer.")
    quit()

if score < 0.0:
    print("Error: Input is out of range.")

if score > 1.0:
        print("Error: Input is out of range.")

else:
    if score >= 0.9:
        grade = "A"
        print("Your grade is: ",grade)
    elif score >= 0.8:
        grade = "B"
        print("Your grade is: ",grade)
    elif score >= 0.7:
        grade = "C"
        print("Your grade is: ",grade)
    elif score >= 0.6:
        grade = "D"
        print("Your grade is: ",grade)
    elif score < 0.6:
        grade = "F"
        print("Your grade is: ",grade)
