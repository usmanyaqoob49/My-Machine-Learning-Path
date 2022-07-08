fname = input("Enter the name of file: ")
opening = open(fname,"r")
count = 0
floatadd = 0.0
for reading in opening:
    if not reading.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    y = reading.find('0')
    x = reading[y:]
    x = float(x)
    floatadd = floatadd + x
average = floatadd/count
print("Average spam confidence:",average)
