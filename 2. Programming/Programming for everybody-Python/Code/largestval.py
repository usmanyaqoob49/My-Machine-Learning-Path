largest = None  #None means nothing
smallest = None
sum = 0
x = [3,4,5,6,7,8]
for i in x:
    #just like if largest == None
    if largest is None:
        largest = i
    elif i>largest:
        largest = i
    #for the sum of numbers in list
    sum = sum + i
print("Largest number in the list is",largest)
print("Sum of all number:",sum)
for i in x:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i


print("Smallest number is:",smallest)
