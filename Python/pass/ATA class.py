"""x = int(input("Enter your number: "))
y = int(input("Enter your number: "))
if x==y:
    print(f"Both x and y are equal and answer od division in {x/y}")
elif x>y:
    print"""

"""def sum(a):
    c = 0 
    c = c + a[0]
    c = c + a[1]
    c = c + a[2]
    c = c + a[3]
    c = c + a[4]

    return c

l = [7, 8, 5, 3, 1]
s = sum(l)
print(s)"""

'''a = 0
for b in [1, 2, 3]:
    a=b
print(a)'''

"""for i in range(10, 0, -1):

  print(i)"""


# Week 11 :- Extracting and Manupulating Individual digits for Algorithmic problem solving

"""x = list(input("Enter yoour number:" ))
sum = 0 
for i in x:
   sum += i
   print(sum)"""

"""t = int(input("Enter your number: "))
sum = 0
num = 0
while(t!=0):
    a = t%10
    sum += a
    t = int(t/10)
print("The sum is:-", sum)"""

"""n = int(input("Enter your number: "))
first = 0
second = 1
next = first + second
print(first, second)
count = 2 
while(count <= n):
    if first%2 !=0 and second%2 !=0:
     print(next)
    
    first = second 
    second = next
    next = first + second
    count += 1  """





"""drivers = ["Alice", "Bob", "Charlie"]
cars = ["SedanX", "EcoDrive", "Speedster"]

for i in drivers:
       for n in cars:
        x = {i:n}
        print(x)"""


"""repair_times = { "Oil Change": [1, 0.8, 1.2], "Brake Repair": [2, 2.5, 2.3], "Battery Replacement": [1.1, 0.9] }

x = repair_times["Brake Repair"]
print(x)
a = 0
for i in x:
  a= a + i
n = i/len(x)
print(n)"""

"""def calculate_average_repair_time(repair_times):
 
  average_times = {} 

  for service, times in repair_times.items():

    total_time = 0
    number_of_appointments = 0

    for time in times:
      total_time = total_time + time  
      number_of_appointments = number_of_appointments + 1 

    if number_of_appointments > 0:
      average_time = total_time / number_of_appointments 
      average_times[service] = average_time 
    else:
      average_times[service] = 0 

  return average_times

repair_times = {"Oil Change": [1, 0.8, 1.2], "Brake Repair": [2, 2.5, 2.3], "Battery Replacement": [1.1, 0.9]}

average_repair_times = calculate_average_repair_time(repair_times)
print(average_repair_times)"""

"""monthly_sales = [35, 40, 38, 42, 37, 39]
x = int(input("Enter your number:"))
y = int(input("Enter your number:"))
a = monthly_sales[x]
b = monthly_sales[y]
c = a - b
if c < 0:
    print("Sales has dropped compared to last month by:",c*-1)
else:
    print("Slaes has increased compared to last month by:",c)""" 

"""def price(x):

    car_prices = { "SedanX": 25000, "Speedster": 34000, "EcoDrive": 21000 }
    a = car_prices[x]
    print("Original price of your car:",a)
    print("Discounted price of your car:",a*0.9)

x = input("Enter your car type : ")
price(x)"""

"""temps = [88, 95, 102, 99, 108, 97]
x = int(input("Enter car engine temprature: "))
if(x>75):
    print("This temp is above threshold temprature by:",x-75)
else:
    print("Temprature is below threshold temprature")"""
"""def flag_high_temps(temps, threshold):
    flagged_temps = []  # Create an empty list to store flagged temperatures

    for temp in temps:  # Loop through each temperature in the list
        if temp > threshold:  # Check if the temperature is greater than the threshold
            flagged_temps.append(temp)  # Add it to the flagged list

    return flagged_temps  # Return the list of flagged temperatures

# Example usage:
temps = [88, 95, 102, 99, 108, 97]
threshold = 100  # Set the threshold value
high_temps = flag_high_temps(temps, threshold)

print("Flagged temperatures:", high_temps)"""



"""n = int(input("Enter your number: "))
factorial = 1
for i in range(1 ,n+1):
    factorial*= i
print(f"Factorial of {n}: {factorial}")
if factorial % 2 == 0:
    print(f"The factorial of {n} is even")
else:
    print(f"The factorial of {n} is odd")"""


"""def product_of_digits(number):
    product = 1
    for digit in str(number):
        
        if digit != '0':
            product *= int(digit)

    return product

num = int(input("Enter a number: "))
result = product_of_digits(num)
print(f"The product of all digits (ignoring zeros) is: {result}")"""


"""def fibonacci_sum_odd_terms(n):
    
    fib = [0, 1]

    
    for i in range(2, n):
        next_term = fib[-1] + fib[-2]
        fib.append(next_term)

    odd_sum = sum(term for term in fib if term % 2 != 0)
    return odd_sum

n = int(input("Enter the number: "))
result = fibonacci_sum_odd_terms(n)
print(f"The sum of odd numbers in the first {n} terms of the Fibonacci series is: {result}")"""



num = 24853

count = 0

while num > 0:

    digit = num % 10

    if digit % 2 == 0:

        count += 1

    num //= 10

print(count)



num = 10203

product = 1

while num > 0:

    digit = num % 10

    if digit != 0:

        product *= digit

    num //= 10

print(product)