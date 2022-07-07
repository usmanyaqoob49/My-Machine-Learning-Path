info = {'Usman':20,'Ali':21,'hassan':22}
for key in info:
    print(key,info[key])
#converting dictionary to list
list = list(info)
print(list)
print(info.keys())  #to print keys of dictionary
print(info.values())    #to print the vlaues of dictionay
print(info.items())
#iterating through items
for key,value in info.items():
    print(key,value)
