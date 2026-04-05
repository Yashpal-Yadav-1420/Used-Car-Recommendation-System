# Write a program to find the greatest of four numbers entered by the user
a  = int(input("Enter number 1: "))
a1 = int(input("Enter number 2: " ))
a2 = int(input("Enter number 3: " ))
a3 = int(input("Enter number 4: " ))

if(a>a1 and a1>a2 and a2>a3):
    print("Greatest number is a:", a)

elif(a<a1 and a1>a2 and a2>a3):
    print("Greatest number is a1:", a1)

elif(a<a1 and a1<a2 and a2>a3):
    print("Greatest number is a2:", a2)

elif(a<a1 and a1<a2 and a2<a3):
    print("Greatest number is a3: ", a3)
