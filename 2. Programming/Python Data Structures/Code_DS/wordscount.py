text = input("Enter any text: ")
#we have lines so split them to get words list
words = text.split()
print(words)
dictionary = dict()
for word in words:
    #if we have a word add one to its value if we do not have it start from value 1
    dictionary[word] = dictionary.get(word,0)+1
print(dictionary)
