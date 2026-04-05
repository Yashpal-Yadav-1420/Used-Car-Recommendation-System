"""import numpy as np

def check_linear_independence(vectors):
    
    if not vectors:
        return "Independent"  # Empty set is considered linearly independent

    matrix = np.array(vectors)
    rank = np.linalg.matrix_rank(matrix)
    num_vectors = len(vectors)

    if rank == num_vectors:
        return "Independent"
    else:
        return "Dependent"
  #Define three vectors:
v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
v3 = np.array([1, 0, 1])

  # Stack the vectors into a matrix.
vector_set = [v1, v2, v3]

  #Use np.linalg.matrix_rank() to check independence.
result = check_linear_independence(vector_set)

# Return whether the set is independent or dependent.
print(result)"""

"""def count_even(lst):
    
  count = 0
  sumofeven = 0
  for i in lst:
    if i%2 == 0:
       count += 1
    if i % 2 == 0:
        sumofeven += i
  print("No. of even elements in the list:", count)
  print("Sum of all the even number in the list:", sumofeven)

count_even([1, 2, 3, 4, 5, 6, 7])"""

"""def valid_number(phone_number):
   
   if len(phone_number) == 10:
     print("It is a valid phone number")
   elif len(phone_number) > 10 or len(phone_number) < 10:
     print("It is not a valid phone number")


phone_number = input("Enter your phone number: ")
valid_number(phone_number)"""

"""def sum_of_factorial(n):
    sum= 0
    product = 1
    for i in range(1, n + 1):
        sum += i
        product *= i
    print("Sum of digits of factorial:",sum)
    print(f"Product of {n}! factorial:",product)
n = int(input("Enter your number: "))
sum_of_factorial(n)"""

"""def pattern(n):
   for i in range(1,n + 1):
    p = i,[i]*2 ,[i]*3, [i]*4, [i]*5
    print(p)
    
n = int(input("Enter your number: "))
pattern(n)"""
    

