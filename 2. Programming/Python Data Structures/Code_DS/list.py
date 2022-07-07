x = [1,2,3]
for i in range(len(x)):
    y = x[i]
    print(y)
a = [1,2,3]
b = [4,5,6]
c = b+a     #will concetnate the lists
print(c)
print(c[:3])    #upto 3 but not including 3
print(c[3:])    #from including 3 to end
#making a list
l = list()  #it will be empty list
#print(dir(x))   #function that we can perform on lists
#adding elements to lists
l.append(2)
l.append(1)
print(l)
print(1 in l)
c.sort()    #sort the list
print(c)
print(len(c))   #print the length of lists
print(max(c))   #print the maximum
print(min(c))
print(sum(c))
