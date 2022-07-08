class dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is sitting.")
    def roll(self):
        print(self.name.title() + " is rolling.")

my_dog = dog("shepered",12)
print("Dog name is "+my_dog.name+".")
my_dog.sit()
print("Age of dog is "+str(my_dog.age)+".")

dog2 = dog("Lucy",20)
print("Name is "+dog2.name)
print("age is: "+str(dog2.age))
dog2.roll()