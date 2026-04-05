'''Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.'''
a = int(input("Enter your maths marks:"))
b = int(input("Enter your Science marks:"))
c = int(input("Enter your English marks:"))

if(a/3>33):
    print("Passed in maths:",a)
elif(b/3>33):
    print("Passed in Science:",b)
elif(c/3>33):
    print("Passed in English:",c)
elif((a+b+c)/3>40):
    print("Passed in all 3 subjects")
