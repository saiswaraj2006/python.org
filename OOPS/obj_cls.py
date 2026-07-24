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
