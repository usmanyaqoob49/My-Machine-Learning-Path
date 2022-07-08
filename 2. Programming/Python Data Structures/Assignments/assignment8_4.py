#Open the file romeo.txt and read it line by line. For each line,
#split the line into a list of words using the split() method.
#The program should build a list of words. For each word on each line check
#to see if the word is already in the list and if not append it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.
opening = open("romeo.txt","r")
list = []
for lines in opening:
    line =lines.rstrip()
    y = lines.split()
    for words in y:
        if words not in list:
            list.append(words)
list.sort()
print(list)
