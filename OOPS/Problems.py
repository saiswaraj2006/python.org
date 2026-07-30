'''Library Management  
Model Book, Member, and Library classes. Implement borrowing and returning functionality.'''

#i need to implement classes like Model Book, Member, and Library
#with methods
class Book:
    def __init__(self,title,author,book_no):
        self.title = title
        self.author = author
        self.book_no=book_no
        self.is_borrowed=False
    def borrow(self):
        
        if not self.is_borrowed:
            self.is_borrowed=True
            return True
        return False #when book is already borrowed
        
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            return True
        print("book is returned")
    

book1=Book("Happiness","Jhon Smith",3425)

class Member:
    def __init__(self,name,member_id):
        self.name=name
        self.member_id=member_id
        self.borrowed_books=[]
    def borrow_book(self,book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available")
    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()#calls book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
    def remaining_book(self,book):
        if book in self.borrowed_books:
            return False
        else:
            print(self.remaining_book(book))
class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
    def add_books(self,book):
        self.books.append(book)
    def add_member(self,member):
        self.members.append(member)
    def borrow_book(self,member,book):
        member.borrow_book(book)
    def return_book(self,member,book):
        member.return_book(book)
    def remaining_book(self,book):
        self.remaining_book(book)
Lib=Library()
book2=Book("python Basics","Jane Doe",1234)
Lib.add_books(book1)
Lib.add_books(book2)

#Add members
m1=Member("SUV",1)
m2=Member("Dinesh",2)
Lib.add_member(m1)
Lib.add_member(m2)
#now borrowing the book
Lib.borrow_book(m1,book1)
Lib.borrow_book(m2,book1)
#SUV borrowed Happiness
#Happiness is not available
#now m1 is returning book 
Lib.return_book(m1,book1)
Lib.borrow_book(m2,book1)
'''
SUV returned Happiness
Dinesh borrowed Happiness'''

#Create a student class with attributes for name and marks .Add methods to:
#display student details
#calculate whether the student has passed(marks>=40)
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def student_details(self):
        if self.marks>=40:
            print(f"{self.name} is Passed,and congras!")
        else:
            print(f"{self.name} is Fail,Best of Luck")
        return self.name,self.marks
s1=Student("Ravi",40)
s2=Student("Reshma",39)
s1.student_details()
s2.student_details()
        
    
