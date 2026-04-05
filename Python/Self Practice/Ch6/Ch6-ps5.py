# Write a program which finds out whether a given name is present in a list or not.
l = ["Harry", "Rohan", "Shubham", "Divya"]
a = input("Enter a name:")

if(a in l):
    print("Name is in list")
elif(a not in l):
    print("Name is not in list")