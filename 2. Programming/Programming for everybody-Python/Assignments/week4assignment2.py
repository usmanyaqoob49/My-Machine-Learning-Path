#Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
#Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
#You should use raw_input to read a string and float() to convert the string to a number.
#Do not worry about error checking or bad user data.
hours = input("Enter the hours: ")
rate_per_hour = input("Enter Rate per hour: ")
#by defalut hours and rate_per_hour will be in string format so we will type cast them first
hours = int(hours)
rate_per_hour = float(rate_per_hour)
gross_pay = hours * rate_per_hour
print("Gross pay is:",gross_pay)
