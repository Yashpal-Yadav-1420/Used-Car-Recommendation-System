'''import sys 

class Node :
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action 


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0 '''

'''x = 10
y = x
x = 20 
print(y)
print(x)'''


'''value_1 = (bool(1) == True)
value_2 = (bool(0.1) == True)
value_3 = (bool(-1) == True)
value_4 = (bool("") == False)

print(value_1, value_2, value_3, value_4)'''

'''sum = 5 + True
print(sum)'''

'''str_1 = "DA_108_Python Programming"
print(str_1.split('_')[1])'''

'''x = 5/2
print(x)'''

'''x = len("")
print(x)'''

#Question 14
#Which of the following is the correct way to convert a float to an int in Python?



'''int_value = convert(5.6, 'int')
print(int_value)'''




'''int_value = 5.6 --int
print(int_value)'''



'''int_value = int(5.6)
print(int_value)'''



'''int_value = 5.6.toInt()
print(int_value)'''

#datetime = "2023-04-15 20:00:00"
#With the string datetime = "2023-04-15 20:00:00", which of the below assignment(s) retrieves the date "2023-04-15"?



#date = datetime[:10]
#print(date)




#date = datetime[0:10]
#print(date)



#date = datetime.split(' ')
#print(date)




#date = datetime.split(' ')[0]
#print(date)

#a = float(input("Enter a number: "))
#b = float(input("Enter a number: "))
#c = (a+b)
#print(c)

'''A = "string"
b = A*100
print(b n)'''

'''for i in range(3):
    for j in range(2):
        print(i + j, end=" ")'''

'''aList = [1, 2, 3, 4, 5, 6, 7]
pow2 =  [2 * x for x in aList]
print(pow2)'''

'''x = 5
y = 10
result = "x is greater" if x > y else "y is greater"
print(result)'''

'''length = 10
current_num = 0
next_num = 1
count = 0
if length <= 0:
	print ("Please provide a number greater than zero")
elif length == 1:
	print (current_num)
else:
	while count < length:
		print (current_num, end = ' ')
		sum = current_num + next_num
		current_num = next_num
		next_num = sum
		count = count + 1'''
'''for i in range(5):
    i = i**2
print(i)'''

'''for num in range(2,-5,-1):
    print(num, end=", ")'''

'''words = ["apple", "banana", "orange", "grape"]
i = 0
while i < len(words):
    print(words[i][0], end=" ")
    i += 1'''

#my_list = [1, 2, 3, 4, 5]
#print(my_list.pop(5))
#print(my_list.remove(-1)) 
#print(my_list.pop(-1))  
#print(my_list.delete(-1))  

'''for i in range(5):
    print(i, end=' ')
    i +=2
print(i)'''

'''list = [[3, 4, 5, 1], [12, 6, 1, 2]]
 
value = list[0][0]
for row in range(0, len(list)):
    for column in range(0, len(list[row])):
        if value < list[row][column]:
            value = list[row][column]
 
print(value)'''

#Which of the following will be a correct for statement to iterate over a range of numbers in decreasing order?

  

#for i in reversed(range(5)):
 # print(i)


#for i in range(5, 0, -1):
 #  print(i)


#for i in range(5, 0):
 #  print(i)

#for i in range(-5, 0):
   #print(i)

'''for num in range(2,-5,-1):
    print(num, end=", ")'''


'''length = 10
current_num = 0
next_num = 1
count = 0
if length <= 0:
	print ("Please provide a number greater than zero")
elif length == 1:
	print (current_num)
else:
	while count < length:
		print (current_num, end = ' ')
		sum = current_num + next_num
		current_num = next_num
		next_num = sum
		count = count + 1'''


"""number1=int(input("Enter number "))
number2=int(input("Enter number "))
result = number1+number2
print("frist number is: ", number1, "second number is: ", "result is: ", result)"""


'''List = ["String", 2, 2.6, 3+5j]
for i in List:
    print(i)
    print(type(i))'''


#x = int(input("Enter your number: "))
#print(count(x))

'''x = int(input("Enter your number: "))
if(x>=18):
    print("Your eligible to vote ")
else:
    print("You are not eligible to vote")'''

'''A = int(input("Enter a number: "))
B = int(input("Enter a number: "))
C = int(input("Enter a number: "))
if(A>B>C):
    print("A is the largest",A)
elif(A<B>C):
    print("B is the largest",B)
elif(A<B<C):
    print("C is the largest", C)
else:
    print("A, B and C are equal")'''


#print(0.1+0.2)
print(1+5.2)