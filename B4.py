#Find the longest strictly decreasing streak in voltage readings using a loop
voltages = [12.6,12.5,12.5,12.3,12.1,11.9,12.0,11.8,11.6,11.5,11.5,11.2]
max_streak_length = 1
start_voltage = voltages[0]
end_voltage = voltages[0]
current_length = 1
current_start = voltages[0]
current_end = voltages[0]
for i in range(1,len(voltages)):
    if voltages[i]<voltages[i-1]:
        current_length +=1
        current_end = voltages[i]
    else:
        if current_length>max_streak_length:
            max_streak_length = current_length
            start_voltage = current_start
            end_voltage = current_end
        current_length = 1
        current_start = voltages[i]
        current_end = voltages[i]
if current_length>max_streak_length:
    max_streak_length = current_length
    start_voltage = current_start
    end_voltage = current_end
drop_minutes = max_streak_length-1
print("LONGEST CONTINUOUS DROP:",drop_minutes,"minutes")
print("STARTED AT:",start_voltage,"V")
print("ENDED AT:",end_voltage,"V")
