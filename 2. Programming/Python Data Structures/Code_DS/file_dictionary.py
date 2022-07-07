name = input("Enter name of the file: ")
fname = open(name,'r')
dictionary = dict()
for lines in fname:
    lines = lines.rstrip()
    words = lines.split()
    for word in words:
        dictionary[word] = dictionary.get(word,0)+1
bigcount = None #most occuring number of a specific letter
bigword = None  #the most occuring letter
for word,count in dictionary.items():
    if bigcount is None or count>bigcount:
        bigcount = count
        bigword = word
print(bigword,bigcount)
