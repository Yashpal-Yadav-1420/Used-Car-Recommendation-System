#  Write a program to find the greatest of four numbers entered by the user.
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
d = int(input("Enter a number:"))

if(a>b and b>c and c>d):
    print("The biggest number is:",a)
elif(a<b and b>c and c>d):
    print("The biggest number is:",b)
elif(a<b and b<c and c>d):
    print("The biggest number is c",c)
elif(a<b and b<c and c<d):
    print("The biggest number is d:",d)