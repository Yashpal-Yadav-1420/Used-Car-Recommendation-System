# Write a program to find the sum of first n natural numbers using while loop.
n = int(input("Enter your number: "))
sum = 0
for i in range (n+1):
    sum = sum + i
    print(sum)