'''Write a program to find whether a given username contains less than 10
characters or not.'''
a = input("Enter your username:")
if(len(a)<10):
    print("Characters are less than 10")

elif(len(a)>=10):
    print("Characters are greater than 10")