"""n = int(input("Enter your number:" ))
for i in range(1, n+1):"""

# Inputing Natural Number
"""
number = int(input("Enter the Natural Number: "))

# j ranges from 1 to n
for j in range(1, number+1):

    # Initializing List
    a = []

    # i loop ranges from 1 to j
    for i in range(1, j+1):
        print(i, sep=" ", end=" ")
        if(i < j):
            print("+", sep=" ", end=" ")
        a.append(i)
    print("=", sum(a))

print()"""

import math
n = int(input("Enter your number: "))
x = int(math.sqrt(n))
for i in range(2, x+1):
    a = n%i
if a == 0 :
     print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")
