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
