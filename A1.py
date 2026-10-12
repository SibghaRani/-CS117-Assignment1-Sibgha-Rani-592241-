#Calculate current using Ohm's law and check if the fuse will blow
voltage=int(input("ENTER VOLTAGE IN VOLTS"))
resistance=int(input("ENTER RESISTANCE IN OHM"))
if resistance>=0:
    current=voltage/resistance
    if current>=2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
else:
    print("Invalid resistance")
            
