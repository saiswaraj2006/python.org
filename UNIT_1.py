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

