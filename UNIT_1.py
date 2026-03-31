#python is a case sensitive language
#variables is used to store some information and this information can be changed 
variable_name='hump'
variable_num=35
variable_float=4.3
print(variable_name , variable_float , variable_num) 
#here identifiers are used to identify the variables names easily 
#SOME RULES TO FOLLOW
# 1. The first character of an identifier is must be a letter or underscore(_)
# 2. The identifiers can be written by using the digits,alphabets, and underscore
# 3. Identifiers are case sensitive
# 4. The symbols like @,$,and % are not allowed
_ball=21#the variable name should start with the (_) or letter no problem
#$all=21 this terminates"invalid syntax error"
student1='rani'
student2='raju'
student3='balu'
print(student1)
print(student2)
print(student3)
print(_ball)
x=10
y=20
str1="good"
print(str1)
print(x*y)#using the operation
#INPUT OPERATION
#to take input from user,Python makes use of the input() function.
name=input("whats your name?")# it takes input from user in string format
age=input("enter your age:")
print(name+",you are"+ age +"years old")# it displays user name +you are +age+ years old message on output screen after taking both input values
#PYTHON HAS RESERVED WORDS CERTAIN WORDS HAS PRE-DEFINED MEANING
# such has 
'''
and
assert
break
class
continue
try
def
del
elif
else
except
exec
finally
for
from
global
if
import
in
is
lambda
not
or
pass
print
raise
return
try
while
with
yield
'''
import keyword# it imports all reserved words such as elif, else, if, break, try etc...
age=int(input("what's your age?"))
if age<18:#condition check 
    print("YOU ARE MINOR")
elif age>=18:#if not if then it terminates to elif and checks the condition
    print("YOU ARE MAJOR")
else:#if not both then prints else block
    print("invalid age please reenter your age")
#INDENTATION 
# white space at the beginning of the line is called indentation
# the indentation describes the logical line for example while taking if conditions at the end we write ':' that symbol
#it provides a whitespace at beginning of the new line or use a single TAB for each indentation
age=80
if age>=50:  #indentation for the logical condition if that not places then the beginning whitespace of the print statement wont occur then it terminates"indentation error"
    print("you are vey old in age")
else:
    print("you are young")
#OPERATORS 
str1="GOOD"
str2="MORNING!"
c=str1+str2#'+' operator uses to concatenates
print(c)
str1+=str2# it same as str1=str1+str2
print(str1)
#using operators like +,-,*,/,%,//,**.
x=32
y=3
print(x+y)#addition operation
print(x-y)#subtraction operation
print(x*y)#multiplication
print(x/y)#Division
print(x%y)#modulus it returns remainder
print(x//y)#Floor Division it returns quotient
print(x**y)#Exponent operation it raises (32^3)performs exponential calculation
k=43
j=45
k+=j# same has k=k+j and stores k has k+j
print(k)
j-=k#in above k value is changes to 88 then it performs operation, it is also same as j=j-k then returns j
print(j)
#comparison operators
#such as <,>,!=,>=,<=
h=90
g=90
l=1
print(h>l)#returns True if the value of left operand is grater than right operand 
print(h<l)#returns True if the value of left operand is lesser than right operand
print(h!=g)#returns True if the two values not equal
print(h>=g)#returns True if the value of the left operand is greater than or equal to the value of right operand
print(h<=g)#returns True if the value of the right side  operand is either greater than or equal to the value on its left side

no1=22
no2=2
no1/=no2
print(no1)


