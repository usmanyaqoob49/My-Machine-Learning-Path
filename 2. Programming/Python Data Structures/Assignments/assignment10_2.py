#Write a program to read through the mbox-short.txt and figure out the distribution by hour
#of the day for each of the messages. You can pull the hour out from the 'From '
#line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter the name of file: ")
dictionary = dict()
list = list()
fopen = open(name,'r')
for lines in fopen:
    lines = lines.rstrip()
    words = lines.split()
    if len(words)<3 or words[0]!='From':
        continue
    important = words[5]
    i = important[0:2]
    dictionary[i] = dictionary.get(i,0)+1
for key,value in dictionary.items():
    list.append((key,value))
    list.sort()
for key,value in list:
    print(key,value)
