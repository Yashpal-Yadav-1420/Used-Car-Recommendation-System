"""class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # private 

    def reset_password(self):
        print(self.__acc_pass)    # by doing this you can access private
# For hiding in pyrhon just put 2 underscore in front of attributes and methods

acc1 = Account("12345", "abcde")
print(acc1.acc_no)
print(acc1.reset_password()) """

#class Person:
   # __name = "anonymous"        # Private attribute

    #def __hello(self):
        #print("Hello person!")  #Private methods
"""Que:-Humne aisa function banaya hi kya jo hum object ke sath use    hi nahi kar sakte?
    ans:- Kyuki is tarah ke functions hote hai genrally jinko internally koi dusra hi function ude karna chata hai"""

      #For ex :- 
       
    #def welcome(self):
       # self.__hello() # yeh aapna name pass karta hain 
        # yeh hello function ko call lagayega or aapna name pass karega
        #yeh welcome function hello ko call karega, yeh hello ko completely call kar sakta hai
 
#p1 = Person()
# Person welcome kar sakta hain lekin hello nahi kar sakta
#welcome hello kar sakta hain kyuki voh internally class ka method hain
#print(p1.welcome()) #p1 ab welcome ko call karega kyuki yehi cheez karna possible or welcome uske liye self.__hello ko call kar raha tha
"""kaise work kar rahi hai cheeze :- Agar humne kisi bhi cheez ko double underscore se private bana diya toh use class ke internal functions hi accss kar payenge bahar ka koi bhi use access nahi kar payega"""

# Inheritance 

"""class Car:
    color = "Light Green"
    @staticmethod
    def start():
        print("car started")
        # Hum chahe to inhe static bhi rakh sakte hain baki inke andar as such car object use nahi ho rahi hai isliye humne inhe static banaya hai
    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):    # Hum parenthesis ke andar uss class ka naam likhte hain jiski properties ko hum inherit karna chate  hain
    def __init__(self, brand):
        self.brand = brand"""

"""car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")
print(car1.name)
print(car1.color)
print(car1.start())"""

"""class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
car1 = Fortuner("Disel")
car1.start()
print(car1)"""

# Multiple Inheritance
"""class A:
    varA = "Welcome To class A"
class B:
    varB = "Welcome To class B"
class C(A, B):
    varC = "Welcome To class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)"""

# Super Method 
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car):
    def __init__(self, name):
       self.name = name

car1 = ToyotaCar("")