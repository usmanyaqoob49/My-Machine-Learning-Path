#Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above
#40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should useraw_input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input - assume the user types numbers properly.
#use try except block
hours = input("Enter the hours: ")
rate = input("Enter the rate: ")
try:
    hours = int(hours)
    rate = float(rate)
except:
    print("Please enter the integer.")
    quit()
#quit() ends the program
h = 40
#Pay for 40 hours
pay_upto_40 = h * rate
#Pay for extra hours
if hours > 40:
    rate = rate * 1.5
    p = (hours - h) * rate
    pay = pay_upto_40 + p
print("Pay is: ",pay)
