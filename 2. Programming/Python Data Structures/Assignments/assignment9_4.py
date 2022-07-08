#Write a program to read through the mbox-short.txt and figure out who has sent the greatest,
#number of mail messages. The program looks for 'From ' lines and takes the second word,
#of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number,
# of times they appear in the file. After the dictionary is produced,
#the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter the file name: ")
fname = open(name,'r')
dictionary = dict()
for lines in fname:
    lines = lines.rstrip()
    words = lines.split()
    if len(words)<3 or words[0]!='From':
        continue
    else:
        important = words[1]
        dictionary[important] = dictionary.get(important,0) + 1
mostemail_adress = None
mostemail_number = None
for adress,number in dictionary.items():
    if mostemail_number is None or number > mostemail_number:
        mostemail_number = number
        mostemail_adress = adress
print(mostemail_adress,mostemail_number)
