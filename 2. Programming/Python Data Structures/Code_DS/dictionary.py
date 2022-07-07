dictionary = dict()
names = ['Usman','Ali','zain','zain','Usman']
for name in names:
    if name not in dictionary:
        dictionary[name] =1
    else:
        dictionary[name] = dictionary[name] + 1
print(dictionary)

#another way of doing it
diction = dict()
names = ['Usman','Ali','zain','zain','Usman']
for name in names:
    diction[name] = diction.get(name,0)+1
print(diction)
