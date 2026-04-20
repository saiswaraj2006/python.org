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
#
# + operator is used for combining both strings

#print("cricket is played with "+"bat & ball")
#print("missile man of India"+"-sir APJ Abdul Kalam")
#we can add even numbers also 
#print("python"+"3.3")
#print("12"+"3456789")#it stores as a string value so that it could not perform addition instead of that it concatenates
#MULTIPLICATION (OR STRING REPETITION )
# If a string is multiplied by floating number it gives error 
#print("root"*4.0)
#TypeError: can't multiply sequence by non-int of type 'float'
#IF A STRING IS MULTIPLIED BY THE INTEGER THEN IT PRINTS 
#print("hello\t"* 4)
#output→hello   hello   hello   hello
#if a integer is stored as string then it concatenates or merges both 
#print("hello"+"4")#output→hello4
'''Tuples
A tuple is an ordered collection of items that is immutable, meaning once created, its elements cannot be changed, added, or removed.
Tuple is written by using ()
Duplicates are allowed means repeated values are allowed 
'''
#create a tuple and print the values
#roop=(21,81,91,0)
#print(roop.index(0))#it returns 3 because the line tracks the exact index value from tuple
#finding class type of the roop variable
#print(type(roop))#it prints <class 'tuple'>
#print(len(roop))#finding length of the tuple 
#tup=(21,41,21,42,5,5,3,5)
#counting the duplicate value in the tuple
#print(tup.count(5))
#print( roop)
#print(2*roop)#it prints 2 times each value in order 
#print(sorted(tup))#it prints in sorted means ascending ordered form if duplicates are there then it prints duplicates
#tuple can stores integers and strings
#tup2=(23,'hi','bye',71,'good morning')
#x,y,z,t,u=tup2#assigning values directly to variables like x,y,z,t,u then i calling y,u so it prints hi good morning
#print(y,u)
#tup3=('the balu ',)#the comma after the first element
#print(type(tup3))
#tup4=('the balu ')
#print(type(tup4))# No comma after the first element is not a tuple it shows it is a string
#tup5=(3,4,1,34,7,45,7,1,8)
#accessing the values in a tuple
#print("tup5[3:5]=",tup5[3:5])#it prints tuple values by using indexing
#print("tup5[1:8]=",tup5[1:8])
#print("tup5[0:9]=",tup5[0:9])

#deleting the created tuple
tup9=(4,'hook')
del(tup9)
#print(tup9)
#NameError: name 'tup9' is not defined. Did you mean: 'tuple'?
#because it is deleted
''' using the divmod() function to find the remainder and quotient after successful division
so divmod() functions returns two values like quotient and remainder'''
quotient, remainder=divmod(555,3)
print("quotient=",quotient)
print("remainder=",remainder)
rog=(12,45,67,23,89,5)
a=min(rog)
b=max(rog)
print("minimum value from the rog tuple=",a)
print("maximum value from the rog tuple=",b)
# example 2
a,b,c,d=(10,20,30,40)
print(a)
print(b)
print(c)
print(d)
#write a python program to multiply all the numbers in the tuple
yup=(2,3,4,5)
a,b,c,d=(2,3,4,5)#here i use the tuple assignment
print(a*b*c*d)
upp=((1,2),(3,4),(5,6))
#sorting the tuple by using'sorting'
oppo=(13,98,2,78)
print(sorted(oppo))#it returns sorted tuple in ordered way
#sai_marks=[19,20,18]
#print(tuple(sai_marks),type(sai_marks))
#print(type(sai_marks))
#checking wheather the value is there are not
#if 1 in sai_marks:
 #   print("True")
#else:
#    print("False")
#example write a code to find the sum of all numbers in a tuple
hup=(736,87,526,0,1,76)
#create a variable and a assign a built-in sum()function
#total_sum=sum(hup)
#print(total_sum)
tub=('blue',67,9,21,'black')
#for printing strings,integers separately i need to go for the line of code which separates by instance in a given tuple
numbers=tuple(x for x in tub if isinstance(x,(int,float)) )
#print("numbers=",numbers)
#total=sum(numbers)
#print('total=',total, type(numbers))
#question -1
#check whether an element 25 in the tuple (10,20,25,30)
#que_1=(10,20,25,30)
#if 25 in que_1:
    #print("is exist")
#else:
    #print("doesn't exist")
    #question-2
#write a program to find the length of a tuple 
#length=len(que_1)
#print("length=",length)
    #question-3
#given a tuple (1,2,3,4,5), create a new tuple with  each element squared
que_3=(1,2,3,4,5)
squared=tuple((i**2) for i in que_3)
#print(squared)
    #question-4
#Convert a tuple (10, 20, 30) into a list, modify it by adding 40, and convert it back to a tuple.
yup=(10,20,30)
y=list(yup)
print(y)
y.append(40)
print(y)
new_tuple=tuple(y)
print(new_tuple)
    #question-5
#Write a program to count how many times an element appears in a tuple.
oppo=(1,2,4,2,5,2,2)
print(oppo.count(2))
    #question-6
#Access the 3rd element of a tuple (10, 20, 30, 40, 50) and print it.
up=(10, 20, 30, 40, 50)
u=up[3]
print(u)
    #question-7
#Concatenate two tuples (1, 2, 3) and (4, 5, 6) and print the result.
nut=(1,2,3)
mut=(4,5,6)
but=nut+mut
print(but)
    #question-8
#Given a tuple of numbers, remove duplicates and return a new tuple.
oppo=(1,2,4,2,5,2,2)
duplicates=tuple(x for x in set(oppo) if oppo.count(x)>1)
print(duplicates)
def remove_duplicates(oppo):
    result = ()#creating a null tuple
    for x in oppo:
        if x not in result:
            result=result+(x,)
    return result
oppo=(1,2,4,2,5,2,2)
print(remove_duplicates(oppo))
    #question-9
#Given a nested tuple like (1, (2, 3), (4, 5)), flatten it into a single tuple (1, 2, 3, 4, 5).
rup=(1,(2,3),(4,5))
result=()
for x in rup:
    if isinstance(x,tuple):
        result=result+x
    else:
        result=result+(x,)
print(result)
    #question-10
#Write a program to sort a tuple without using sorted() (hint: convert to list).
cup=(8,3,4,2,9,8,0,0)
print(sorted(cup))
    #question-11
#Store student records as tuples (name, marks) and find the student with the highest marks.
student_record=(("nandhini",20),("varsha",19),("vaishnavi",18))
top_student=max(student_record,key=lambda x: x[1])
print(top_student)
'''on the above line top_student works by using max() it selects
the each element in student_record and selects the maximum value on a condition
key=lamda x: x[1]
take each tuple x
return x[1]→the marks by using indexing 
means x="nandhini" and x[1]=20
so, it returns x[1]
'''
    #question-12
#Given a tuple of daily temperatures, calculate the average temperature.
daily_temperature=(34,33,35,28)
a,b,c,d=daily_temperature#by using assignments if there is a less data
print((a+b+c+d)/4)
#if there was long data then im using the sum(),len()
daily_temperature=(34,33,35,28)
average_temperature=sum(daily_temperature)/len(daily_temperature)
print(average_temperature)
# this is the best because while the large data is there then this method is best
#convert the floating point number to the corresponding integer
#a=float(input("Enter the floating point number"))
print(("The integer variant of")+str(a)+("=")+str(int(a)))

'''Here i used concatenation operator so, it only concatenates the string values not integers
that's why i used str(a) instead of 'a' because 'a' stores the float value so i use that str(a)'''



#LISTS-NEW TOPIC
#List is a versatile data type which is available in the python and the elements is separated by usoing commas
#List allows different types of Datatypes to store in it it also allows indexing,updating,repetition,concatenation, and some operations 
first_lst=[1,'sun','Monday','3+5j',5.90,True]
print(first_lst)
print(type(first_lst))#it returns <class 'list'>
#List is mutable which means the value of its element can be changed
#ACCESSING VALUES IN LIST
#same has strings the list also perform the slicing,and concatenations
#lst=[start:stop:step]
#↡↡↡
#Above lst shows about slicing example
lst1=[1,2,3,4,5,6,7,8,9,10]
print("num List is:",lst1)
print("First element in the List is ",lst1[0])
print("Last element of the List is ",lst1[-1])#here by using slicing i calling last element in the particular list this is useful when large data is given then we want last element then this slicing is useful
print("lst1=[::2]", lst1[::2])#this returns every other element from the list
print("lst1=[2::2]", lst1[2::2])#get every other element but starting with index 2
print("reverse of List=", lst1[::-1])#it gets the output in the reverse order
lst2=[1,2,3,4,5,6,7,8,9,10]
print(lst2)
#performing inserting,append(),deletion 
 #on the list which is already created
    #example
lst2[9]=99#inserting the 99 value at the 9th index instead of 10
print(lst2)
lst2[1]=22
print(lst2)
lst2.append(299)#by using append( ) we can add any element at the last of the list
print(lst2)
del lst2[10]
print(lst2)#by using indexing we can delete a particular value of a given list 
#deleting all elements in a list
del lst2[::]
print(lst2)#it deletes all elements in the list and prints empty list because we using indexing
#Note:but it doesn't delete total list it only deletes the elements in the list
#when you want to delete the total list then directly use the del 
del lst2
#print(lst2)#NameError: name 'lst2' is not defined. Did you mean: 'lst1'?
#Write a program to insert a list in another list using the slice operation 
lst3=[9,4,2,1]
lst4=[]
lst4=lst3[::]
print("lst4=",lst4)#here i use null list to insertion by using slicing
#Taking a list with elements then slicing it into the another list 
lst5=[23,24,25]
lst5[2]=lst3
print("lst5 after insertion is=",lst5)#OUTPUT=lst5 after insertion is= [23, 24, [9, 4, 2, 1]]
#another way by using direct way without creating a list inserting directly in the step lest see.
lst5[1]=[0,1,22]
print("lst5 After insertion =",lst5)#OUTPUT=lst5 After insertion = [23, [0, 1, 22], [9, 4, 2, 1]]

#NESTED LISTS
#'NESTED LIST' means a list within another list 
#for example 
lst5=[23, [0, 1, 22], [9, 4, 2, 1]]
#here at the index 1,2 there are another list elements in int 
lst5[0]='fool'
print(lst5)
i=0
while i<(len(lst5)):
    print("lst5[",i,"]=",lst5[i])
    i+=1
#lst5[ 0 ]= fool
#lst5[ 1 ]= [0, 1, 22]
#lst5[ 2 ]= [9, 4, 2, 1]
lst5=[23,[0,1,22],[9,4,2,1]]
lst5.insert(0,22)#syntax is (index,object)
print(lst5)
lst5.pop(0)#it deletes the element from the list at specific index 
print(lst5)
lst5.insert(0,'sun') 
print(lst5)
lst3.sort()
print(lst3)#it sorts in low to high order
lst3.reverse()#the reverse() method can reverse the all elements 
print(lst3)
lst3.extend(lst5)#it adds the another list at the end of the list
print(lst3)
print(lst3.count(9))#it counts the 9 how many times it will repeat
print(lst3.index(4))#it prints the index value where the object exist
    #example-1
'''A small library wants to manage its collection of books using a python
program. The library stores book titles in a list. Your task is to write
a program that performs the following operations 
LIST METHODS
1. Add new books to the collection
2. Remove a book if it is borrowed 
3. Sort the books alphabetically 
4. Reverse the order
5. Count how many times a particular book appears
6. Find the position of a book in the list
7. Copy the collection into another list
8. Clear the collection at the end of the day
'''
#1
library_books=['Harry Potter', 'The Hobbit','1984','Harry Potter']
library_books.insert(1,'Dune')
library_books.insert(2,'Pride and Prejudice')
print(library_books)
#2
#removing book '1984'
library_books.remove('1984')
print("The '1984' book was borrowed so the remaining books was:",library_books)
#3
library_books.sort()
print(library_books)
#4
library_books.reverse()
print(library_books)
#5
j=library_books.count('Harry Potter')
print(j)#IT PRINTS COUNT=2
#6
library_books.index('Harry Potter')
#7
copy_library_books=library_books.copy()
print(copy_library_books)
#8
copy_library_books.clear()
print(copy_library_books)
library_books.pop(2)
print(library_books)#it deletes an element from list at certain index place
a=len(library_books)
print(a)
#program to make a list of cubes

b=[]#creating an empty list
for i in range(13):
    b.append(i**3)#it prints 0 to 13 cubes 
print(b)
#Looping in the lists
#example
#for i in list:
    #print(i)
#program to print the sum of elements and the mean also
#first creating a list 
klst=[4,3,2,1,6,3]
s=0
for i in klst:
    s=s+i
print("sum of the given list is:",s)
mean=float(s/float(len(klst)))
print("mean of the given list:",mean)

#example 2
'''
- Print all elements of the list one by one.
- Find the sum of all elements in the list.
- Find the largest and smallest numbers in the list.
- Count how many even and odd numbers are present in the list.
- Reverse the list without using built-in functions like reverse() or slicing.



'''
#creating the list to perform all operations by using loops concepts in the list
hook=[3,9,1,4,6,7]
for i in hook:
    print( i)#for printing all elements in the list
sum_hook=0
for i in hook:
    sum_hook=sum_hook+i
print("sum is:",sum_hook)  #to return the sum of elements in the given list

largest=hook[0]
for num in hook:
    if num>largest:
        largest=num
print("largest is:",largest)
smaller=hook[0]
for nums in hook:
    if nums<smaller:
        smaller=nums
print("smallest number :",smaller)
count=0
for nume in hook:
    if nume%2==0:#this condition checks if the number is even or not
        count+=1#if even then count is +1
print("even number count is:",count)
counts=0
for numo in hook:
    if numo%2!=0:
        counts+=1
print("odd number count is:",counts)
#converting any string,set,tuple or dictionary into list
dug=list("king emperor")#here the space also count
print(dug)
#LIST CLONING
#list cloning means creating a separate copy of the list this process is called as the list cloning
vig1=['l',9,0,4,'gun','rose']
vig2=vig1
print(vig2) 
vig3=vig2[2:-1]
print('vig3:',vig3)#list vig3 is clone by using vig2
#clone the all student marks from taking input from the user
s_marks=[]
#for i in range(5):

    #s_mark=input("enter the student marks {i+1} :")
    #s_marks.append(s_mark)
#print("s_marks:",s_marks)
s_names=[]
#for i in range(5):
    #names=input("Enter the student names{i+1}:")
    #s_names.append(names)
#print("s_names:",s_names)
s_report=list(zip(s_names,s_marks))
#above line is used to merge two lists using the zip()


print("s_report:",s_report)#output→s_report: [('sowmya', '12'), ('riya', '15'), ('somanth', '13'), ('hales', '20'), ('bejoes', '20')]
#program to iilustrate the use of the enumerate() to print an individual item and its index in the list
fool=[3,53,21,9,6]
for index,i in enumerate(fool):
    print(i,"index value is=",index)
    '''
3 index value is= 0
53 index value is= 1
21 index value is= 2
9 index value is= 3
6 index value is= 4
    '''
for index,i in enumerate(s_report):
    print(i,"is at index:",index)
    '''
('shiva', '14') is at index: 0
('ragu', '12') is at index: 1
('vasim', '15') is at index: 2
('vaishnavi', '20') is at index: 3
('helini', '20') is at index: 4
    '''
moo=[2,45,1,45,2]
for i in range(len(moo)):
    print("index:",i)
'''output is:
index: 0
index: 1
index: 2
index: 3
index: 4
'''
#filter() function constructs a list those elements of the list for which a function
#returns True.The syntax of the filter() function is= filter(function, sequence)
#   PROBLEM SOLVING 
#write a program that creates a list of numbers from 1-20 that are either divisible
#by 2 or divisible by 4 without using the filter function
div_2_4=[]
for i in range(2,22):
    if(i%2==0 or i%4==0):#it checks that is divisible by 2 or 4 then adds to the empty list 
        div_2_4.append(i)

print(div_2_4)
#write a program using filter function to a list of squares of numbers from 1-10.then 
#use the for...in construct to sum the elements in the list generated
#def square(x):
    #return(x**2)
#squares=[]
#squares=list(square(i) for i in filter(square, range(1,11)))
#print("list of the 1-10 squares:",squares)
#s=0
#for i in squares:
    #s=s+i
#print('sum:',s)
#write a program that defines a list of 5 states that are a member of india 
#check whether the state belongs to that list or not
India_states5=['Arunachal pradesh','Andhra pradesh','Telangana','Gujarat','GOA']
#is_state=input("Enter the name of the state:")
#if is_state in India_states5:
   # print(is_state,"is already in india")
#else:
   
   # print("Enter correct name")
    #SET() CONCEPT
#set is created by placing all elements in the curly braces{},separated by the comma or by using builtin function set()
#example of creating the set 
set1={3,1.1,'set created',90}
#print(set1)
#or
s=set(['sort','removes_duplicates',22,43])
#print(s)
#set has a property of removing duplicates directly from the set
#example
dog=set(['bone',"bone",66,43,11,11,5.6])#check the set has initialized by some duplicate values when i call the set it automatically removes
#print(dog)
#here the output={'bone', 66, 5.6, 11, 43}because the 'bone' repeated two times so it prints one time means removes the duplicate values and the 11 also 
#CONVERSIONS
list45=[4,6,45]
#print(set(list45))#list is converted to set.output=
tup0=(4,32,4,23)
#print(set(tup0))
#print(tup0)#it returns tuple values output=(4, 32, 4, 23)
#print(set(tup0))#converts the tuples to the set values. output={32, 4, 23}
#str="fjeiwnsfhimdve"
#print(set(str))#converting the string into the set

#print(set("a man has hunger issues".split()))#forms a set of words
#set operations 
'''s.update()
s.add()
s.discard(),s.pop(), s.clear(), len(), s.union(), s.intersection, s.difference , s.difference_update(), s.symmetric_difference()
s.copy(),s.isdisjoint(), all(s),max(),min(),sorted(),enumerate(s) etc
'''
# Original set
original_set = {1, 2, 3, 4}

# Copying the set
copied_set = original_set.copy()

#print("Original Set:", original_set)
#print("Copied Set:", copied_set)
soup={3,5,2,1}
sop={5,2,6}
#sop.update(soup)
#print(sop)
#sop.add(77)
#print(sop)
#sop.clear()
#print(sop)#it gives output has=set() means that empty values in the set
#sop.add(55)#here im adding a element to empty set()
#print(sop)
#so the set has contains only one element so im updating the set by adding some values
add_sop=set([3,4,2,99,46])
sop.update(add_sop)
#print(sop)
#so the set 'sop' contains {2, 99, 3, 4, 55, 46}
#finding the length of my set() by using len()
l=len(sop)
#print(l)#6
#checking is a element is present in the set or not
#print(3 in sop)#it returns 'TRUE' because the element is present in the sop()
#print(3 not in sop)#it returns 'FALSE' because the element is present in the sop() hence im checking not in set
#now im creating two sets to perform symmetrical operations
mat23={45,2,1,89,44,17,3,5}
mat45={64,90,1,2,3,5,4,99}

#print("the intersection of mat23&mat45:",mat23&mat45)
#print("the union of mat23 and mat45:",mat23|mat45)
#mat23.intersection_update(mat45)
#print(mat23)#without using '&'
set8={1,2,3}
#set8.issubset(mat45)
#print(set8<=mat45) #here it returns 'TRUE' because the all elements in the set8() are in the mat45()
#using enumeration function
dug={45,2,0,4,2,3}
#for i in enumerate(dug):
    #print(i)
alphabets={'a','b','c','d','e','f','g'}
#for i in enumerate(alphabets):
    #print(i,end='')#it returns (0, 'd')(1, 'a')(2, 'c')(3, 'e')(4, 'f')(5, 'g')(6, 'b')
#end='', which means no newline and no space will be added after each tuple.
#so to create new line 
print()
#for finding maximum and minimum in the given set
#max()
#sets={3,4,21,9,3,22,99,2}
#print(max(sets)) 
#or
#mm=max(sets)
#print('maximum:',mm)
#min()
#print(min(sets))
#or
#mi=min(sets)
#print('minimum:',mi)
#to print it in the sorted set form
#sorted_set=sorted(sets)

#print('sorted:',sorted_set)
#finding if the two sets have a null intersection or not
ss=set([23,54,1])
sp=set([44,2,68])
#print(ss.isdisjoint(sp))
#it returns True,because there is no intersection
#if it returns False then there is a intersection between the two sets
#example
sr=set([43,1,55])
#print(ss.isdisjoint(sr))
#it prints False because the 1 is in the another set
#print(ss.intersection(sr))#it returns the intersecting value={1}
#finding the sum of the set values
set4=set([22,1,4,343,342,1,25])
#it should not take the duplicate values 
#print(sum(set4))#737
#write a program that generates a set  of prime numbers and another set of odd numbers. Demonstrate the result of union, intersection,
#difference, and symmetric difference operations on these sets
odds=set([x*2+1 for x in range(1,10)])
#print('odd numbers:',odds)
primes=set()
for nu in range(2,20):
    for i in range(2,nu):
        if nu%i==0:
            break
    else:
        primes.add(nu)
#print("prime num:",primes)
#print("union:",odds.union(primes))
#print("intersection is:",odds.intersection(primes))
#print("symmetric difference:",odds.symmetric_difference(primes))
#print("difference:",odds.difference(primes))
'''
write a program that creates two sets .one of even numbers in range 1-10 and other has all composite numbers in range 1-20
demonstrate the use all(),is.superset(), len(),and sum() functions on the sets
'''
evens=set([x for x in range(1,20) if x%2==0])#here checks the condition and if it is true then prints x value
eve=set([x*2 for x in range(1,10)])#the x is multiplied by the 2 with all numbers 1-10
#print(eve)
#print(evens)
#for printing the composite numbers in range 1-20
composites = set()

for i in range(2, 21):  # start from 2, since 1 is not composite
    j = 2
    while j <= i // 2:  # check divisors up to half of i
        if i % j == 0:
            composites.add(i)
            break       # stop checking once composite is confirmed
        j += 1

#print("Composite numbers from 1 to 20:", composites)
#print("ALL:",all(evens))
#print("superset:",evens.issuperset(eve))
#print("superset:",evens.issuperset(composites))#it returns False
#print("Length of evens:",len(evens))
#print("sum of all numbers in th evens set:",sum(evens))
#write a program that creates the two sets  squares and cubes
squares=set([x**2 for x in range(1,10)])
#print('squares:',squares)
cubes=set([x**3 for x in range(1,10)])
#print("cubes:",cubes)
#adding the element
squares.add(11*2)
#print("squares_after_adding:",squares)#it adds the value o 11*2=22 in the squares
squares_pop=squares.pop()
#print("squares after pop:=",squares_pop)#it returns the 64
#if i use pop() operation  then the set is empty then it gives key error
set_empty={}
#print(set_empty.pop()) #it raises error 
#remove(), update(), clear()
squares.remove(36)
#print("after remove:",squares)
squares.update(cubes)
#print(squares)#it updates all cubes set values in  the squares
#so it gives the output has
#{64, 1, 512, 4, 8, 9, 16, 81, 22, 343, 216, 25, 729, 27, 49, 125}
#in the above if any duplicates are there it should be deleted and returns the set
#clear()
cubes.clear()
#print(cubes)#it empty the whole set i gives empty set has the output
#if i use discard() function then
squares.discard(1)
#print(squares)#then it tries to remove the element if is present in the set
#so here my output is the={64, 512, 4, 8, 9, 16, 81, 22, 343, 216, 25, 729, 27, 49, 125}
#write a program that has a list of countries . creates a set of the countries and prints the names of the countries in the sorted form
countries=(['China','Russia','Australia','India','Afghanistan','Cuba','Europe','South korea'])
#print("countries_after_sorted:",sorted(set(countries)))
#countries_after_sorted: ['Afghanistan', 'Australia', 'China', 'Cuba', 'Europe', 'India', 'Russia', 'South korea']
#dictionaries
#dictionary is a data structure in which we store values as a point of key and value.Each key is separated from its value by colon
# (:),and consecutive items are separated by commas.The entire items in a dictionary are enclosed in curly brackets({}). The 
# syntax for defining a dictionary is
#dictionary_name={key_1: value_1, key_2: value_2, key_3: value_3}
dict={'roll_no':'22','Admno':'24CAM1022','Hno':'1-67'}
#print(dict)
#program to create a 10 key values pairs where key is a number in hte range 1-10 and the value is twice the number
squares={x: x**2 for x in range(1,10)}
#print(squares)
#output={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#program to access values stored in a dictionary
dic={'roll_no':'22','marks':'45','School_name':'SMHS','Name':'swaraj'}
#print("dic[name]=",dic['Name'])
#print("dic[School_name]:",dic['School_name'])
#print("dic[marks]:",dic['marks'])
#print("dic[roll_no]:",dic['roll_no'])
#program to add a new line
dics={'Roll no':'34','School name':'high school'}
#print("dics[Roll no]:",dics['Roll no'])
#print("dics[School name]:",dics['School name'])
dics['marks']=100#new entry
#print(dics)
#now im creating the new dictionary and modifying the entry
new_dic={'Roll_No':22,'Stuyding':'AI-ML','Hobby':'editing,gaming,drawing,script writing,writing'}
print(new_dic)
print("ROLL_NO:",new_dic['Roll_No'])
print("STUDYING:",new_dic['Stuyding'])
print("HOBBY:",new_dic['Hobby'])
new_dic['Game']={'Chess,FF,Hill Climb Racing,Sudoku,etc'}
print("GAME:",new_dic['Game'])
print("AFTER ADDING THE NEW DATA:",new_dic)
#now for erasing all data i use the clear() function
#otherwise for deleting the certain data i use the del(dict_name) function to delete the certain one
del new_dic['Game']
print(new_dic)#{'Roll_No': 22, 'Stuyding': 'AI-ML', 'Hobby': 'editing,gaming,drawing,script writing,writing'}
#for clearing the all data from the existing dictionary we use clear() function
print("after clearing:",new_dic.clear())
#it gives none because the  dictionary has no data if i call the dictionary then
print(new_dic)#output→{}
#for deleting the data i use clear(),but for deleting the whole dictionary i use the del() function
del new_dic

#print(new_dic)

#then it returns Traceback (most recent call last):
#File "c:\Users\saisw\OneDrive\Desktop\python_practice\UNIT_1.py", line 878, in <module>
#print(new_dic)
#^^^^^^^
#NameError: name 'new_dic' is not defined
#here  dictionaries are case-sensitive 
#a program to randomly pop() or the element from  a dictionary
sov={'Roll No':690000,'Name':'Bhuvi','Rank':'1st'}
print(sov.pop('Roll No'))#it returns Roll No
print('sov=',sov)
#today im concentrating on the  dictionaries Built-in Functions and methods 
#to find the length of the dictionary 
print(len(sov))#it returns the value 2
#because the above block of the code pop the 'Roll No' so it has only two elements it returns 2
print(sov)
print(repr(sov))#Return the canonical string representation of the object.
#or
print("string representation:",str(sov))
#creating another dictionary to perform the copy ,clear
frog_lifespan={"Common Pond Frog":{"Wild":"5-8 years","Captivity":"10+ years"},
               "American Bullfrog":{"Wild":"7-10 years", "Captivity":"15+ years"},
               "Tree Frogs":{"Wild":"2-5 years", "Captivity": "8-10 years"},
               "Posiion Dart Frogs":{"Wild":"5-7 years", "Captivity":"10-12 years"},
               "Goliath Frog":{"Wild": "10-12 years","Captivity":"15+ years"},
               "Wood Frog":{"Wild": "3-6 years","Captivity":"8-10 years"}
               }
print(frog_lifespan.keys())
#it prints key values in the above dictionary
#ex=dict(''keys'':''values'')so it prints the key values
#dict_keys(['Common Pond Frog', 'American Bullfrog', 'Tree Frogs', 'Posiion Dart Frogs', 'Goliath Frog', 'Wood Frog'])
print("frog_lifespan.values=",frog_lifespan.values())
print(frog_lifespan['American Bullfrog']['Wild'])
#7-10 years
print(frog_lifespan.items())
frog_lifespan.setdefault('Golden Frog',{'Wild':'4-6 years','Captivity':'8 years'})
print("\n",frog_lifespan['Golden Frog'])
#it sets default value for a key that is  not present in the dictionary
