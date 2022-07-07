handle = open("romeo.txt","r")
dictionary = dict()
list1 = list()
#going line by line in code
for lines in handle:
    #removing the white space
    lines = lines.rstrip()
    #making a list of words of lines
    words = lines.split()
    #going through those words
    for word in words:
        #getting number of times the word occur
        dictionary[word] = dictionary.get(word,0) + 1
for key,value in dictionary.items():
    list1.append((value,key))
#When we will make reverse true it means it will start from highest number
#list1 = sorted(list1, reverse = True)
list1.sort(reverse = True)
for val,key in list1[0:10]:
    print(val,key)
