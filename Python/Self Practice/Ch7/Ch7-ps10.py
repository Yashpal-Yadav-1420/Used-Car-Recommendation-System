# Write a program to print multiplication table of n using for loops in reversed 
# order.
n = int(input("Enter a number:"))
k =  10   #int(input("Enter a number:"))
while(k-1>=0):
    print(f" {n} X {k} = ", n*k)
    k = k -1

# Using for Loop 
'''n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} X {11 -i} = {n*(11-i)}")'''