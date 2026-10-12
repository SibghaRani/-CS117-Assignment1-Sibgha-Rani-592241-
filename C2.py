#Compute equivalent parallel resistance from a list of resistors value
def parallel_resistance(resistors):
    reciprocal_sum = 0
    for r in resistors:
        reciprocal_sum +=1/r
    return 1/reciprocal_sum
ans1 = parallel_resistance([10,10])
ans2 = parallel_resistance([100,200,300])
print("Parallel resistance([10,10]):",ans1)
print("Parallel resistance([100,200,300]):",ans2)
