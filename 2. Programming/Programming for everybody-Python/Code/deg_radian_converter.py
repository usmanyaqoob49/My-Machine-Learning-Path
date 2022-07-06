import math
def radian(deg):
    print("Enter angle in degree: ")
    rad = deg * float(math.pi/180)
    print("Angle in radian is:",rad)

def degree(r):
    print("Enter angle in radian: ")
    d = r * float(180/math.pi)
    print("Angle in degree is:",d)

choice = input("If you want to enter angel in degree press d and otherwise r: ")
num = input("Enter the angle now: ")
num = float(num)
if choice == "r":
    degree(num)
elif choice == "d":
    radian(num)
else:
    print("Sorry Sir.")
