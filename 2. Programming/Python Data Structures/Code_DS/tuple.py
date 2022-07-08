x = {"a":1,"c":3,"b":2} #dictionary
y = sorted(x.items())
#or
#it will sort the key of dictionary
#remember items() return the list of tuple and we can sort the keys of tuple
for key,value in sorted(x.items()):
    print(key,value)
#now we will sort values of tuple
l = list()  #making a empty list
for key,value in x.items():
    l.append((value,key))
print(l)
l = sorted(l)
print(l)
