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
#print(student1)
#print(student2)
#print(student3)
#print(_ball)
x=10
y=20
str1="good"
#print(str1)
#print(x*y)#using the operation
#INPUT OPERATION
#to take input from user,Python makes use of the input() function.
#name=input("whats your name?")# it takes input from user in string format
#age=input("enter your age:")
#print(name+",you are"+ age +"years old")# it displays user name +you are +age+ years old message on output screen after taking both input values
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
#import keyword# it imports all reserved words such as elif, else, if, break, try etc...
#age=int(input("what's your age?"))
#if age<18:#condition check 
 #   print("YOU ARE MINOR")
#elif age>=18:#if not if then it terminates to elif and checks the condition
 #   print("YOU ARE MAJOR")
#else:#if not both then prints else block
 #   print("invalid age please reenter your age")


#INDENTATION 
# white space at the beginning of the line is called indentation
# the indentation describes the logical line for example while taking if conditions at the end we write ':' that symbol
#it provides a whitespace at beginning of the new line or use a single TAB for each indentation
#age=80
#if age>=50:  #indentation for the logical condition if that not places then the beginning whitespace of the print statement wont occur then it terminates"indentation error"
 #   print("you are vey old in age")
#else:
 #   print("you are young")
#OPERATORS
 
#str1="GOOD"
#str2="MORNING!"
#c=str1+str2#'+' operator uses to concatenates
#print(c)
#str1+=str2# it same as str1=str1+str2
#print(str1)
#using operators like +,-,*,/,%,//,**.
#x=32
#y=3
#print(x+y)#addition operation
#print(x-y)#subtraction operation
#print(x*y)#multiplication
#print(x/y)#Division
#print(x%y)#modulus it returns remainder
#print(x//y)#Floor Division it returns quotient
#print(x**y)#Exponent operation it raises (32^3)performs exponential calculation
#k=43
#j=45
#k+=j# same has k=k+j and stores k has k+j
#print(k)
#j-=k#in above k value is changes to 88 then it performs operation, it is also same as j=j-k then returns j
#print(j)
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
print(no1)#output is 11.0 because the logic is same has no1=no1/no2
#BITWISE OPERATOR

#Bitwise OR(|)
#Bitwise AND(&)
#Bitwise NOT(~)
#Bitwise XOR(^)
#Bitwise operations are the operations which performs on the bit level 
print(6&3)#which means 0110&0011 then first operand ANDed with corresponding right operand
# which is output→0010=2 so it returns 2
print(6|3)#using Bitwise OR OPERATOR so the bit in the first operator is ORed with the corresponding right operand
#output→ 7 
#because 6 is 0110 and 3 is 0011 then when both operands are 0 result will be 0 otherwise 1
#0110
#0011
#____
#0111→(7) so it returns 7
print(~3)# it is the BITWISE NOT operator (-6+1=7)it inverts bit
#which if it is 0 it prints 1
# ______________ 
#|A   | !A      |      
#|0   |  1      | 
#|1   |  0      |—–—→TRUTH TABLE
#|____|_________|
#example ~001001 is 110110
#BITWISE XOR
print(6^3)#it compares each bit of the first operand with the corresponding bit of its second operand. if one of the bits is 1,the corresponding bit in the result is 1 and 0 

#shift operator 
#left shift <<
# Example 1: Simple left shift
x = 5          # binary: 0101
print(x << 1)  # Output: 10 (binary: 1010)

# Example 2: Shift by 2 positions
x = 5          # binary: 0101
print(x << 2)  # Output: 20 (binary: 10100)
#RIGHT SHIFT OPERATOR
x=5
print(x>>1) # binary:0101
#output:2 (binary:0100)
#the left most bit is 0 for positive numbers then shifted right from left most bit or simple as like the division by 2
print(x>>2)
#here x=0101 
#shifting by 1 we get→0010
#again shifting by 1 by using above answer then we shifted 2 times so 2 right side shifting is over
#0010→0001 so the output is 1
# Example 3: shift by 3 positions 
print(x>>3)
#output is 0 because right shift by one by using 2 shift answer
#then 0001→0000===0 so the output is the 0
#OPERATIONS ON STRINGS 
'''CONCATENATION
MULTIPLICATION (OR STRING REPETITION )
indexing 
slicing
length etc
'''


