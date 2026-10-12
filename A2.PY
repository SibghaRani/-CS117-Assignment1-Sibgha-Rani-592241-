#Determine current flow direction based on positive,negative,or zero value
current=int(input("ENTER THE CURRENT IN AMPERES"))
if current>=0:
        print("CURRENT FLOWS FROM A TO B")
elif current<=0:
        print("CURRENT FLOWS FROM B TO A")
else:
        print("NO CURRENT FLOWS")
