#firstly we will make a infinte loop
#break make the execution of program exits the loop
while True:
    x = input("> ")
    if x == "exit":
        break   #whenever this statement will be executed loop will be terminated
    print(x)
print("i am out of loop.")
