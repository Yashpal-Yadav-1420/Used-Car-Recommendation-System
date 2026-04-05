#b = "ABCDEFGHI"
#print(b[-5:-2])
#print(b[-9:-1])

"""a = "Hello, World!"
print(a.lower())"""
"""a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']"""

"""price = 45
txt = f"The price is {price:.2f} dollars"
print(txt)"""


"""def sum_list_elements(lst):
   sum = 0
   count = 0
   for i in lst:
    sum += i
   if i > 10:
     count += 1

   return sum, count

x ,y = sum_list_elements([3, 11, 15, 7, 2, 18])
print("Sum:", x)
print("Count of numbers > 10:", y)"""   


"""def sum_list_elements(lst):
    
    total_sum = 0
    count_greater_than_ten = 0
    

    for num in lst:
        
        total_sum += num
        
        if num > 10:
            count_greater_than_ten += 1
    
    
    return total_sum, count_greater_than_ten

example_list = [3, 11, 15, 7, 2, 18]
result_sum, result_count = sum_list_elements(example_list)
print(f"Sum: {result_sum}")
print(f"Count of numbers > 10: {result_count}")"""

"""def swap_with_temp(x, y):
    it = x  + y      #it is a temproary variable
    x = it - x
    y = it - x
    return x, y
a = int(input("Enter a: "))
b = int(input("Enter b: "))
a, b = swap_with_temp(a, b)
print("Swapped value of a:",a)
print("Swapped value of b:",b)


def range_sum_for(n):
    total = 0
    for i in range(n):
        total += i
    return total


n = 5
print(f"Using for loop: Sum = {range_sum_for(n)}")"""

"""def range_sum_while(n):
    total = 0
    i = 0
    while i < n:
        total += i
        i += 1
    return total


print(f"Using while loop: Sum = {range_sum_while(5)}")"""


def range_sum_bottom_check(n):
    total = 0
    i = 0
    while True:
        if i >= n:
            break
        total += i
        i += 1
    return total


print(f"Using bottom-check loop: Sum = {range_sum_bottom_check(5)}")
