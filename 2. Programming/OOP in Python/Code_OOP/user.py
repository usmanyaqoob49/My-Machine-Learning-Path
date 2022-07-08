from re import A, L


class user():
    def __init__(self,first_name,second_name,age,login_attempt):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.login_attempt = login_attempt
    def describe(self):
        print("User name is: "+self.first_name+" "+self.second_name)
        print("Age of user is: "+str(self.age))
    def greet(self):
        print("Welcome "+self.first_name.title()+" "+self.second_name)
    def inc_login_attempts(self):
        self.login_attempt+=1
    def reset_login_attempt(self):
        self.login_attempt = 0
u1 = user("Usman","yaqoob",20,2)
u1.describe()
u1.inc_login_attempts()
print(str(u1.login_attempt))
u1.reset_login_attempt()
print(u1.login_attempt)
class privilliages():
    def __init__(self,privilliages):
        self.privilliages = privilliages
    def show_priv(self):
        print("Admin roles: ")
        print(self.privilliages)


class admin(user):
    def __init__(self,first_name,second_name,age,login_attempt,privilliages):
        super().__init__(first_name,second_name,age,login_attempt)
        self.privilliages = privilliages()
a1= admin("Usman","Yaqoob",20,2, ["can delete post","can ban the user","can detect user"])
a1.privilliages.show_priv()