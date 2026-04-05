# Write a program using functions to find greatest of three numbers.
def gret():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    if(a>b>c):
        print(a)
    elif(a<b>c):
        print(b)
    elif(a<b<c):
        print(c)


gret()