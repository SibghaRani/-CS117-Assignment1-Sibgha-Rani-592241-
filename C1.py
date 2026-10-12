#Calculate and return circuit current and power using separate functions
def ohms_current(v,r):
    return v/r
def power_dissipated(i,r):
    return(i**2)*r
V = 12
R = 6
current = ohms_current(V,R)
power = power_dissipated(current,R)
print("CURRENT=",current,"A")
print("POWER=",power,"W")
