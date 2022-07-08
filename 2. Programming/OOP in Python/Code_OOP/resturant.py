import re


class resturant():
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe(self):
        print("Name of Resturant is: " + self.name.title())
        print("Cuisine type is: "+ self.cuisine_type.title())
    def open(self):
        print("Resturant is open.")
    def update_number_serverd(self,val):
        self.number_served = val
    def increment_served(self,no):
        self.number_served+=no
rest1 = resturant("Grand Hayat","Karahi")
rest1.open()
rest1.describe()
print("Number of custromer served are: "+str(rest1.number_served))
rest1.update_number_serverd(20)
print("Now number of cutomer served: "+ str(rest1.number_served))
rest1.increment_served(20)
print("Now number of cutomer served: "+ str(rest1.number_served))


class Icecreamstand(resturant):
    def __init__(self, name, cuisine_type,flavours):
        super().__init__(name, cuisine_type)
        self.flavours = flavours
    def displayflavour(self):
        print("Flavour of Ice cream is: " + self.flavours)
    
ice1 = Icecreamstand("grand hayat","nothin","Stawberry")
ice1.displayflavour()
ice1.describe()

        


