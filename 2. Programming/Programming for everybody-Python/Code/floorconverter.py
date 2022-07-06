#In US ground floor is 1 floor and in other world ground floor is 1 efloor
#so we will convert euorpean floor to US floor number
efloor = input("Enter Euoropean floor number: ")
#efloor will be string defaultly
efloor = int(efloor)
#we converted so that we can add int to it
USfloor = efloor + 1
print("US floor number is",USfloor)
