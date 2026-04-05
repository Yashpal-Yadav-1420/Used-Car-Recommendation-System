# Write a program to find out wether a student has passed or failsd if it requires a total of 40% and atleast of 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
marks1 = int(input("Enter your marks1: "))
marks2 = int(input("Enter your marks2: "))
marks3 = int(input("Enter your marks3: "))

percent = ((marks1 + marks2 + marks3)*100)/300

if(percent>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:", percent)

else:
    print("Try again next year:", percent)
   


    
