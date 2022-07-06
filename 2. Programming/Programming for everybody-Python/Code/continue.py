while True:
    print("loop starting here.")
    n = input("> ")
    if n == "Start again":
        continue
    if n == "exit":
        break
    print(n)
print("I am out of loop.")
