x = input("Enter any number: ")
x = int(x)
y = 10
if x > 0:
    print("x is a positive number.")
    if x > y:
        print("x is also greater than y.")
    if x < y:
        print("x is positive but less than y.")
    else:
        print("x is equals to y.")
if x < 0:
    print("x is negative.")
else:
    print("x is equals to zero.")
