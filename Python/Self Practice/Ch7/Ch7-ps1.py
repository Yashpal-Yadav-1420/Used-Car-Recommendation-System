# Write a program to print multiplication table of a given number using for loop.
a = int(input("Enter a number:"))
for i in range(11):
    print(f"The product of {a} X {i} =",a*i)