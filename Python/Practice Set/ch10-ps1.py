# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class programmer:
    Company = 'Microsoft'
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary 
        self.language = language
        print("I am creating an object")
p = programmer("Yashpal Yadav", 1200000, "Python")
print(p.name, p.salary, p.language, p.Company)   
        