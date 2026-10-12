#Classify manufactured resistors into tolerance bins continuously until stopped
count_1_percent = 0
count_5_percent = 0
count_reject = 0
while True:
    resistance = float(input("Enter measured resistance value(0 to stop): "))
    if resistance ==0:
        break
    if 99.0<=resistance<=101.0:
        count_1_percent +=1
    elif 95.0<=resistance<=105.0:
        count_5_percent +=1
    else:
        count_reject +=1
print("1% tolerance:",count_1_percent)
print("5% tolerance:",count_5_percent)
print("reject:",count_reject)
