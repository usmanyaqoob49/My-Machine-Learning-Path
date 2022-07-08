import re
class back():
    def __init__(self,date,time):
        self.date  = date
        self.time = time
        self.val = 0    #default

    def printdate(self):
        print("today is " + str(self.date))

    def printtime(self):
        print("Time right now is "+str(self.time))

b = back(22,"12:32")
b.printdate()
b.printtime()
class hello(back):
    def __init__(self,date,time):
        super().__init__(date,time)

    def printsem(self):
        print("my semester is: " + str(self.date))
    
    def printuni(self):
        print("my uni is:" + self.time)


