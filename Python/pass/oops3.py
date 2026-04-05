"""class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_values(self):
        return 10* self._value
    
    @ten_values.setter
    def ten_values(self, new_value):
        self._value = new_value/10
        

#x = int(input("Enter your number: "))
obj = MyClass(20)
obj.ten_values = 67
print(obj.ten_values)
obj.show()"""
#Question 
"""class Library:
    def __init__(self, no_of_booksborrowed, no_of_booksreturned, books, shelf):
      self.no_of_booksborrowed = no_of_booksborrowed
      self.books = books
      self.no_of_booksreturned = no_of_booksreturned
      self.shelf = shelf
    def book(self):
       if (self.no_of_booksborrowed == self.no_of_booksreturned):
          print("Thanks for returning all the borrowed books")
       else:
          print("Please return all the borrowed books")
       for self.books in self.shelf:
        print("All the correct books have been returned")
        break
no_of_booksborrowed = int(input("Enter the number of books: "))
no_of_booksreturned = int(input("Enter the number of books: "))
books = input("Enter elements separated by space: ").split()
shelf = input("Enter elements separated by space: ").split()
a = Library(no_of_booksborrowed, no_of_booksreturned,books,shelf )
a.book()"""

#Solution
class Library:
    def __init__(self):
        self.noofbooks = 0
        self.books = []
    def addBook(self, book):
        self.books.append(book)
        self.noBooks = (self.books)
    def showInfo(self):
        print(f"The library has{self.noBooks} books.The books are ")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("Harry Potter 1")
l1.addBook("Harry Potter 2")
l1.addBook("Harry Potter 3")
l1.showInfo()
