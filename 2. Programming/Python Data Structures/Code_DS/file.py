#opening a file h.txt for read operation
handle = open("h.txt","r")
count_line = 0
#print statement also prints the new line so to remove it
for line in handle:
    line = line.rstrip()
    #means if word 'Usman' is not in any line
    if not 'Usman' in line:
        continue    #skip that line
    print(line)
    count_line = count_line+1
print("Number of lines:",count_line)
