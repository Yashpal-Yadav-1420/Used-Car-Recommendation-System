# Write a program to print the following star pattern.

'''n = int(input("Enter a number: "))

for i in range(n + 2):
    print("*")'''

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")    # This line give spaces form starting
    print("*"* (2*i-1), end="")      # This line prints no.of sars based on the condition
    print("")                    # This line will give you next line 