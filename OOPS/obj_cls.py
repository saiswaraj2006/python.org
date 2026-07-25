class Student:
    name="sai"
s1=Student()
print(s1)
#<__main__.Student object at 0x00000230984F6E40>
print(s1.name)#sai
s2=Student()
print(s2.name)#sai
#because i declared name="sai"
#in that particular class 

#CONSTRUCTOR
class Bottle:

    def __init__(self,fullname):
        self.color=fullname
b1=Bottle("Blue")
print(b1.color)
#blue
#self refers to first object name 
#Constructors are Three types
#1. Default Constructor
class Demo:
    def __init__(self):
        print("Default Constructor.")
obj=Demo()

#Parameterized Constructor
#Where parameters(Arguments) accepts the arguments to initialize object attributes
class Class_Room:
    def __init__(self,std_name,age):
        self.std_name=std_name
        self.age=age
obj=Class_Room("Varun",55)
print(obj.std_name,obj.age) 

#Copy Constructor:
#CREATES  a new object by copying data from another object
#here python doesn't have copy constructor but im using it manually
class Car:
    def __init__(self,Brand=None,color=None,obj=None):
        if obj is not None:#copy constructor
            self.Brand=obj.Brand
            self.color=obj.color
        else:
            self.Brand=Brand
            self.color=color

        
C1=Car("Mercedes","Royal Blue")
C2=Car(obj=C1)#copy constructor
#because im copying the C1 to C2 
print(C2.Brand,C2.color)
#Mercedes Royal Blue
#class attribute
#this is used when same attributes for many number of objects then it is used

#instance attribute
#this instance is different for every object when created

class Student:
    clg_name="XYZ Institute"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
s1=Student(name="Roshan",roll_no=22)
s2=Student(name="Pallavi",roll_no=54)
print(s1.name,"from",s1.clg_name,"and his roll_no is",s1.roll_no)
print(s2.name,s2.roll_no)
'''
Roshan from XYZ Institute and his roll_no is 22
Pallavi 54
'''
#but above i include a str line which is "and his roll_no is"
#but i want to include in my attributes for boys 
#and another with "her" for girls
class Student:
    clg_name="XYZ Institute"
    he="and his roll_no is"
    she="and her roll_no is"
    fr="from"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
      
s1=Student(name="Priya",roll_no=28)
s2=Student(name="Mani",roll_no=34)
s3=Student(name="Varshini",roll_no=30)
print(s1.name,s1.fr,s1.clg_name,s1.she,s1.roll_no)
print(s2.name,s2.fr,s2.clg_name,s2.he,s2.roll_no)
print(s3.name,s3.fr,s3.clg_name,s3.she,s3.roll_no)