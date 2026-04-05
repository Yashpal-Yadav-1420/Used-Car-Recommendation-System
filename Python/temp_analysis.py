temperatures = [31, 35, 30, 38, 32]

total = 0
for temp in temperatures:
    total += temp   # adds each value to total


average = total / len(temperatures)


threshold = 33
count = 0

for temp in temperatures:
    if temp > threshold:
        count += 1   

print("Temperature Data:", temperatures)
print("Average Temperature:", average)
print("Values above", threshold, ":", count)