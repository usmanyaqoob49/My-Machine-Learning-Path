x = input("Enter a number: ")
x = int(x)
y = 10
if x > 0:
    print("x is a positive number.")
    if x > y:
        print("x is also greater than y.")
    elif x < y:
        print("x is less than y.")
    else:
        print("x is equals to y.")
elif x < 0:
    print("x is negative.")
else:
    print("x is equal to zero.")
