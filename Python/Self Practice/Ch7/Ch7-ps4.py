# Write a program to find whether a given number is prime or not.

n = int(input("Enter a number: "))
i = 2
while(i < n):
    if(n%i != 0):
        print("This is prime")
        break
    i = i+1
else:
  print("This is not Prime")
  