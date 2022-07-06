x = input("Enter a number: ")
try:
    print("Starting try block.")
    x = x + 1
    print("Ending try block.")
except:
    print("Except block.")
    x = int(x)
    x = x + 1
    print("Value of x is",x)
