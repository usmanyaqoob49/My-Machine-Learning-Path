dictionary = dict() #empty dictionary
dictionary['Name'] = 'Usman'
dictionary['Age'] = 20
print(dictionary)
print(dictionary['Name'])
dict2  = {'Hello':'World','Number':1}
print(dict2)
print(dict2['Hello'])
dict2['Number'] = dict2['Number']+1
print(dict2)
x = dict2.get('Name','There is no such key') #get the value of key Name if it is not their return value 0
print(x)
x = dictionary.get('Name','There is no such key') 
print(x)
