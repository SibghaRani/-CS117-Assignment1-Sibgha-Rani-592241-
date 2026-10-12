#Calculate total series resistance by looping throughu user provided resistor values
resistors=int(input("HOW MANY RESISTORS?"))
total_resistance=0
for i in range(1,resistors+1):
    r_value = int(input("Enter resistance" + str(i) + ":"))
    total_resistance +=r_value
print("THE TOTAL RESISTANCE:",total_resistance,"ohm")
