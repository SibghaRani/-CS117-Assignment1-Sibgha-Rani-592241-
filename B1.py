#Print current values for supply voltages from 1V to 10V using for loop
resistance=10
for voltage in range(1,11):
    current = voltage/resistance
    print("VOLTAGE=",voltage,"V,CURRENT=",current,"A")
