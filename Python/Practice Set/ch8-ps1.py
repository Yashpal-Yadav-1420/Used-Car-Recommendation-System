# Write a program using functions to find greatest of three numbers.


a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

def greatest(a, b, c):
    if (a>b and b>c):
        return a
    elif(a<b and b>c):
        return b
    elif(b<c and b<c):
        return c

print(greatest(a, b, c ))