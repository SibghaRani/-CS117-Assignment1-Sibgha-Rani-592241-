# Analyze voltage readings using a single loop to find counts,highest and lowest values, and average
readings = (3.3,3.1,3.4,2.9,3.6,3.0,3.2)
count_above3_2 = 0
total_sum = 0
total_count = 0
highest = readings[0]
lowest = readings[0]
for r in readings:
    if r>3.2:
        count_above3_2 +=1
    if r >highest:
        highest=r
    if r<lowest:
        lowest=r
    total_sum +=r
    total_count +=1
average = total_sum/ total_count
print("READING ABOVE 3.2V:",count_above3_2)
print("HIGHEST READING:",highest)
print("LOWEST READING:",lowest)
