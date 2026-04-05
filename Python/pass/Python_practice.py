# Conditional Practice
"""x = int(input("Enter your number: "))
if x % 2==0:
    print(x, "is an even number")
else:
    print(x,"is a odd number")"""

"""a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
flag = bool(input("Enter true or False: "))
if a < 0 or b < 0 and flag == True:
    print("True")
elif a < 0 and b < 0 and flag == "True":
    print("True")
else:
    print("False")"""

"""j_angry = bool(input("Are you angry(True/False): "))
s_angry = bool(input("Are you angry(True/False): "))
if j_angry == "True" and s_angry == "True":
    print("True", "Since both of them are angry,\nso you are in trouble.")
elif j_angry == "False" and s_angry == "False":
    print("True", "Since none of them are angry,\nso you are in trouble.")
else:
    print("Only one of them is angry,\n so we are not in trouble.")"""


"""str = input("Enter your string: ").lower()
a = str.count("cat")
b = str.count("hat")
if a == b:
    print("True",f"cat and hat both are present\n{a} number of times.")
else:
    print("True",f"cat and hat both are present\n{a} number of times.")"""

# Loop Statement

"""n = int(input("Enter your number: "))
m = int(input("Enter your number: "))
for i in range(1, m+1):
    print(n*i)"""

"""str = input("Enter your string: ")
n = len(str)
for i in range(0, n):
    if i%2 == 0:
     print(str[i])"""

"""x = int(input("Enter your number: "))
for i in range(x,0,-1):
    print(i)"""

"""n = int(input("Enter your number: "))
x = int(input("Enter your power: "))
power = 1
while power < n:
    power = power**x
    print(power)
    power += 1"""

"""def pos_and_neg(n):
 if n < 0:
    for i in range(n, 1, 1):
        print(i)
 elif n > 0:
    for i in range(n ,-1, -1):
        print(i)
 else:
    print("n is already zero")

n =  int(input("Enter your number: "))
pos_and_neg(n)"""

"""def nn(n):
    for i in range (1, n):
        if i%2 == 0:
            print(i)
n = int(input("Enter your number: "))
nn(n)"""

"""n = int(input("Enter your number: "))
for i in range(1, n):
    a = []
    a = i.append()
    for j in range(1, i):"""

# Analyze the below code

"""number = int(input("Enter the Natural Number: "))
 
# j ranges from 1 to n
for j in range(1, number+1):
 
    # Initializing List
    a = []
 
    # i loop ranges from 1 to j
    for i in range(1, j+1):
        print(i, sep=" ", end=" ")
        if(i < j):
            print("+", sep=" ", end=" ")
        a.append(i)
    print("=", sum(a))
 
print()"""

"""digit_char = "7"
print(int(ord(digit_char)))"""

"""def hotel_discount(n, hotel_rooms):
    room = {"Single Rooms":1200, "Double Rooms":2000,"Queen Rooms":5000,"Triple Rooms":6000,
            "Studio Rooms":7000,"Deluxe Rooms":8000, "Rooms with a View":9000,
            "Junior Suites":10000,"Suites":12000,"Presidential Suites":13000} #room rent per day
    if n > 3:
        a = room[hotel_rooms] * n * 0.85
        print(f"Your Total amount for {n} days with 15% discount: ₹ {a}")
    else:
        a = room[hotel_rooms] * n
        print(f"Your Total amount for {n} days : ₹ {a}")
        

n = int(input("Enter how many days you have stayed: "))
hotel_rooms = input("Enter your room type: ")
hotel_discount(n, hotel_rooms)"""



"""PIN = "2NCjTGKhFqZ1OB"
for i in range(3):
    m = input("Enter your PIN: ")
    if m == PIN:
        print("You have entered the correct PIN.")
        break
    else:
         print(f"You have entered the incorrect PIN {i + 1} Times.")
         if i+1 ==3:
             print("Now you are not allowwed to do any further entry.")"""
       
       
"""def electricity_bill(n):
    #100 units: ₹5 per unit
    #101 to 300 units: ₹8 per unit
    #Above 300 units: ₹10 per unit
    if n <= 100:
        a = n * 5
    elif 101 < n <= 300:
        a = n * 8
    else:
        a = n*10
    print(f"Your Total electricity bill: ₹{a}")

n = int(input("Enter units used: "))
electricity_bill(n)"""


