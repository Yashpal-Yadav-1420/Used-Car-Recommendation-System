# class is use to store data for an object.
# from cake example :- object is a output(cake) and the information about that object is stored in a class. 

# Humne ek class banali student naam se ab hum bata rahe hai ki isme kya kya information store honi chahiye student ke liye

"""
class Student:
    name = "Karan"  """
# Yeh humne class bana li, lekin hum classes ko directly use nahi kar sakte, class ki object banani padthi hai
# Eg:- ek factory ke andar ek blueprint bana diya ki acr ke andar yrh yeh feature hone chahiye, phir gadi bhi toh banani padegi us blueprint ko use karke, vo jo gadi banti hai usse hum object kehte hain.

#creating object(instance)
"""s1 = Student()
print(s1) 
print(s1.name) # output :- karan"""

"""class Cars:
    color = "blue"
    brand = "BMW"
v1 = Cars()   # Yeh parenthesis constructor ko call karne ke liye lagaye jate hain.
print(v1.color,v1.brand)"""

# Constructor(__init__function):- Yeh function object creation ke time pe invoke hota hai
# All classes have a function called__init__(),which is always executed when the object is being initiated. means :- jaise hi aap class ka use karke ek object banaoge tab automatically init function call hojayega.chahe aap init function likho ya mat likho, init function hamesha execute hoga ther is always a constructor there for us.
# Constructor hamesha ek parameter leta hain,self.
"""self :- jo nayi object create ho rahi hain isiko hum self keh rahe hain.
yeh jo object hain jiske creation par constructor call hota hain iska yeh reference hain, matlab yeh isi ki taraf pointout kar raha hai """
"""Hum bina print statement ke bhi object print kar sakte hain.because yeh jo counstructor hai vo aapne aap call or invoke ho jata hai """
"""Yeh jo student object hai or jo self parameter hain vo dono same hi hai(dono ka out same hi aayega print karne par)"""
"""Constroctor har ek object se sath ek bar call hota hai"""
"""COnstructor ke andar jab ek nai object banti hai toh ham additiona information bhi ham pass kar sakte hain taki vo additional information hamari object ke saath jake store ho jaye or kal ko hum isi information ko access kar sakte hain or kisi bhi kam ke liye iste mal kar sakte hain. """
"""class Student:
#Constructors are divided into two :
    college_name = "IITJ"

     #default constructors
    def __init__(self):
            pass
     # parametarized constructors
    def __init__(self, fullname,  branch):
        self.branch = branch
        self.name = fullname
        print("adding another name to database..") # line no. 28

s1 = Student("Karan", "B.Tech")
print(s1.name, s1.branch, s1.college_name)"""

"""Attributes :- koi bhi variable eg:- name, marks yeh attributes hain meri class ke liye. """
"""Object memory me space occupy karti hain. """ 
# Jab bhi same name ke class and object attribute hote hain tab object attribute print hota hain, because object attribute > class attribute in priority  . 
# Class can store two things 1) data(attributes) :- attributes ka matlab hai kya kya properties hain aapke pass
# 2) methods :- functions written inside the class.

"""class Student:
    college_name = "IITJ"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Karan", 85)
s1.welcome()
print(s1.get_marks())"""

class Student:
     def __init__(self, name, marks):
          self.name = name
          self.marks = marks

     def avg(self):
         sum
         """ x =  self.marks/3
          print(x)"""
     
s1 = Student("Karan", [90, 30, 25])
print(s1.name, s1.marks)
s1.avg()
"""s2 = Student("Nitin", [90, 30, 25])
print(s2.name, s2.marks)
s3 = Student("Yashpal", [90, 30, 25])
print(s3.name, s3.marks)"""
          