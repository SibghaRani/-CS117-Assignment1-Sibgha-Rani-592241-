#Find the smallest and largest resistors values using if/else comparisons
resistor_1=int(input("ENTER THE VALUE OF RESISTOR 1:"))
resistor_2=int(input("ENTER THE VALUE OF RESISTOR 2:"))
resistor_3=int(input("ENTER THE VALUE OF RESISTOR 3:"))
#Find smallest resistor
if resistor_1<=resistor_2 and resistor_1<=resistor_3:
    print("SMALLEST RESISTOR HAS VALUE:",resistor_1)
elif resistor_2<=resistor_1 and resistor_2<=resistor_3:
    print("SMALLEST RESISTOR HAS VALUE:",resistor_2)
else:
    print("SMALLEST RESISTOR HAS VALUE:",resistor_3)
#Find largest resistor
if resistor_1>=resistor_2 and resistor_1>=resistor_3:
    print("LARGEST RESISTOR HAS VALUE:",resistor_1)
elif resistor_2>=resistor_1 and resistor_2>=resistor_3:
    print("LARGEST RESISTOR HAS VALUE:",resistor_2)
else:
    print("LARGEST RESISTOR HAS VALUE:",resistor_3)
