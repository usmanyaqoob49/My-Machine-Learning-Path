def computepay(h,r):
    #pay for 40 hours
    pay = 40 * r
    if h > 40:
        r = 1.5 * r
        bonus_pay = (h - 40) * r
        pay = bonus_pay + pay
    return pay
hours = input("Enter the hours: ")
rate = input("Enter the rate: ")
hours = float(hours)
rate = float(rate)
print("Pay is",computepay(hours,rate))
