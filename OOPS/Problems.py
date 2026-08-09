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
'''
Ravi is Passed,and congras!
Reshma is Fail,Best of Luck'''

#problem
'''
Create a Rectangle class with attributes for length and width. Add methods to:
Calculate the area
Calculate the perimeter
Compare two rectangles to see which one has a larger area'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def compare_area(self, other_rectangle):
        if self.area() > other_rectangle.area():
            print("This rectangle has a larger area.")
        elif self.area() < other_rectangle.area():
            print("The other rectangle has a larger area.")
        else:
            print("Both rectangles have the same area.")



rect1 = Rectangle(10, 5)
rect2 = Rectangle(8, 7)
print("Rectangle 1 Area:", rect1.area())
print("Rectangle 1 Perimeter:", rect1.perimeter())
print("Rectangle 2 Area:", rect2.area())
print("Rectangle 2 Perimeter:", rect2.perimeter())

# Compare areas
rect1.compare_area(rect2)
'''
Rectangle 1 Area: 50
Rectangle 1 Perimeter: 30
Rectangle 2 Area: 56
Rectangle 2 Perimeter: 30
The other rectangle has a larger area'''

#problem
'''
Create a Dog class with attributes for name and age. Add methods to:

Make the dog bark
Check if the dog is a puppy (age < 2)

'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

    def is_puppy(self):
        if self.age < 2:
            print(f"{self.name} is a puppy.")
        else:
            print(f"{self.name} is not a puppy.")

    def display(self):
        print(f"Dog Name: {self.name}, Age: {self.age}")


# Example usage
dog1 = Dog("Pup", 1)
dog2 = Dog("Max", 4)

dog1.display()
dog1.bark()
dog1.is_puppy()

dog2.display()
dog2.bark()
dog2.is_puppy()
#output:
'''
Dog Name: Pup, Age: 1
Pup says: Woof! Woof!
Pup is a puppy.
Dog Name: Max, Age: 4
Max says: Woof! Woof!
Max is not a puppy'''

#Question 2: Online Shopping Cart
'''
Model a shopping cart system with Product, CartItem, and ShoppingCart classes.
Implement adding items, removing items, and calculating total price.
'''
class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price
class CartItem:
    def __init__(self,product,quantity):
        self.product=product
        self.quantity=quantity
    def get_total(self):
        return self.product.price * self.quantity
class ShoppingCart:
    def __init__(self):
        self.items=[]
    def add_items(self,product,quantity):
        self.items.append(CartItem(product,quantity))
        print(f"Added {quantity} x {product.name} to cart.")
    def remove_item(self, product):
        self.items=[item for item in self.items if item.product!=product]
        print(f"Removed {product.name} from cart.")
    def calculate_total(self):
        total=sum(item.get_total() for item in self.items)
        print(f"Total price: ${total}")
        return total
p1=Product("Laptop", 50000)
p2=Product("Headphones", 2000)
cart=ShoppingCart()
cart.add_items(p1, 1)
cart.add_items(p2, 2)
cart.calculate_total()
cart.remove_item(p2)
cart.calculate_total()

#i'm creating the Hotel Booking system
#my implementation is with room,customer name,hotel,booking and checking functionality
class Room:
    
    def __init__(self,room_no,price):
        self.room_no=room_no
        self.is_booked=False
        self.price=price
    
    def book(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False
    def checkout(self):
        if self.is_booked:
            self.is_booked=False
            return True
        return False
class Customer:
    def __init__(self, name):
        self.name = name
        self.booked_rooms = []
    def book_room(self, room):
        if room.book():
            self.booked_rooms.append(room)
            print(f"{self.name} booked Room {room.room_no} for ₹{room.price}")
        else:
            print(f"Room {room.room_no} is already booked.")
    def checkout_room(self,room):
        if room in self.booked_rooms and room.checkout():
            self.booked_rooms.remove(room)
            print(f"{self.name} checked out from Room {room.room_no}")
        else:
            print(f"{self.name} cannot checkout Room {room.room_no}")
    
class Hotel:
    def __init__(self,name):
        self.name=name
        self.rooms=[]
    def add_room(self,room):
        self.rooms.append(room)
    def list_available_rooms(self):
        print("Availability Rooms:")
        for room in self.rooms:
            if not room.is_booked:
                print(f"Room {room.room_no} - ${room.price}")
hotel=Hotel("Dhaba Hotel")
room1=Room(101,2000)
room2=Room(102,2100)
hotel.add_room(room1)
hotel.add_room(room2)
cust1=Customer("Dhruv")
cust1.book_room(room1)
cust1.book_room(room2)
cust1.checkout_room(room1)
hotel.list_available_rooms()
#question
#-----------------------------------#
'''
Design a system to manage students and courses in a school. You need three classes:
Student → stores student details (name, roll number, enrolled courses).
Course → stores course details (course name, course code, enrolled students).
School → manages students and courses.
requirements
A student can enroll in multiple courses.

A course can have multiple students.

The school should be able to list all students in a course and all courses a student is enrolled in.
'''
class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        self.courses=[]
    def enroll(self,course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)
            print(f"{self.name} enrolled in {course.course_name}")
        else:
            print(f"{self.name} is already enrolled in {course.course_name}")
    def list_courses(self):
        print(f"{self.name}'s courses:")
        for course in self.courses:
            print(f"- {course.course_name}")       
class Course:
    def __init__(self,course_name,course_code):
        self.course_name=course_name
        self.course_code=course_code
        self.students=[]
    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)
    def list_students(self):
        print(f"students in {self.course_name}")
        for student in self.students:
            print(f"- {student.name}")
class School:
    def __init__(self,name):
        self.name=name
        self.students=[]
        self.courses=[]
    def add_student(self, student):
        self.students.append(student)
    def add_course(self,course):
        self.courses.append(course)
#Example usage
school=School("NATIONAL HIGH SCHOOL")
s1=Student("Dhanush",101)
s2=Student("Shreyansh",102)
c1=Course("Mathematics","MATH101")
c2=Course("Science","SCI102")
school.add_student(s1)
school.add_student(s2)
school.add_course(c1)
school.add_course(c2)
s1.enroll(c1)
s2.enroll(c2)
s2.enroll(c1)
s1.list_courses()
c1.list_students()
#today about learning the abstraction example
#abstraction is about to hiding the important details while implementation and exposing
#only the essential features
from abc import ABC, abstractmethod
# Abstract base class
class Shape(ABC):
    @abstractmethod #defining the method
    def area(self):#in my above class the subclassses are area and perimeter
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class implementing abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Usage
rect = Rectangle(10, 5)
print("Area:", rect.area())          # Area: 50
print("Perimeter:", rect.perimeter()) # Perimeter: 30
#here im hiding the internal formula used in area and perimeter finding
#the actual calculation is hidden the subclass
'''
output:
Area: 50
Perimeter: 30
'''
print()
#i already done the bank balanced system
''' question
Design a system to manage bank accounts. You need three classes: 
Account → stores account number, balance, and methods for deposit/withdraw.
Customer → represents a customer with a name and multiple accounts.
Bank → manages customers and allows transfers between accounts.

Requirements:

A customer can open multiple accounts.

Deposits and withdrawals should update the balance correctly.

Transfers should only work if the sender has enough funds.

The bank should be able to list all customers and their accounts.
'''

class Account:
    def __init__(self,acc_no,balance=0):
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return f"{amount}$ is credited new balance is:{self.balance}$"
    def withdraw(self,amount):
        
        if amount<=self.balance:
            self.balance-=amount
            return f"{amount}$ is debited from your {self.acc_no} and new balance is:{self.balance}$"
            
        else:
            return "insufficient amount to withdraw!"
            
    def get_balance(self):
        return self.balance
    
class Customer:
    def __init__(self,name):
        self.name=name
        self.accounts=[]
    def open_acc(self,account):
        self.accounts.append(account)
        print(f"{self.name} opened account {account.acc_no}")
    def list_accounts(self):
        print(f"{self.name}'s Account:")
        for acc in self.accounts:
            print(f"Account {acc.acc_no}, Balance:{acc.balance}$")

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

   
    def transfer(self, from_account, to_account, amount):
        result = from_account.withdraw(amount)
        print(result)
        if "debited" in result:
            print(to_account.deposit(amount))
            print(f"Transferred {amount}$ from {from_account.acc_no} to {to_account.acc_no}")

    def list_customers(self):
        print(f"Customers of {self.name}:")
        for cust in self.customers:
            print(f"-{cust.name}")


# Example usage
bank = Bank("State Bank of India")

cust1 = Customer("Sai")
cust2 = Customer("Roy")

acc1 = Account(101, 5000)
acc2 = Account(102, 2000)

cust1.open_acc(acc1)
cust2.open_acc(acc2)

bank.add_customer(cust1)
bank.add_customer(cust2)

msg1=acc1.deposit(2000)
print(msg1)
msg2=acc1.withdraw(3000)
print(msg2)
print(bank.transfer(acc1, acc2, 1000))

cust1.list_accounts()
cust2.list_accounts()






