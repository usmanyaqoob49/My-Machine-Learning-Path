class car():
    def __init__(self,make,price,model):
        self.make = make
        self.price = price
        self.model = model
        self.odometer_reading = 0 #default attribute 
    def desciption(self):
        des = str(self.make.title()+" "+str(self.model)+" and cost is: "+str(self.price))
        return des.title()
    def read_odometer(self):
        print("Our car start with "+str(self.odometer_reading)+" milage.")
    def update_odometer(self,milage):
        self.odometer_reading = milage
    def fill_gas_tank(self):
        print("Tank is filled.")
mycar = car("Audi",20,2022)
print(mycar.make)
print(mycar.desciption())
mycar.read_odometer()
#changing value of default attribute
mycar.odometer_reading = 23
mycar.read_odometer()
#second way
mycar.update_odometer(24)
mycar.read_odometer()
mycar.fill_gas_tank()

#making a class battery that will be added to the electric car as attribute
class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("The size of battery is: "+str(self.battery_size))
    def range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go "+ str(range)
        message+=" miles on full charge."
        print(message)
    
#inheritance
class electric_car(car):
    def __init__(self,make,price,model):
        super().__init__(make,price,model)
        #here it is class is added as a attribute
        self.battery = Battery()
    
#over riding the methode of parent class
#As electric cars do not need gas so we will over ride it by declaring same methode in child class
    def fill_gas_tank(self):
        print("This car does not need gas.")   
my_tesla = electric_car("tesla",12222,2022)
print(my_tesla.desciption())
#here accessing battery first 
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.range()
