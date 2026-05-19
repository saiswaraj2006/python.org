'''A function in Python is a block of organized, reusable code that is used to perform a specific task.
 It helps in breaking programs into smaller modules, improves readability,
 and allows code to be reused without rewriting it.'''

'''
 Starting by writing def to define a function.
 Giving  the function a name
 Choosing a meaningful name ,that describes what the function does.
 Adding parentheses ()
 Inside the parentheses, specify parameters (inputs) if needed.
 If no inputs are required, leave them empty.
 End the line with a colon :
 
 
 Adding the code to performs the task.
 using Indentation 
 Using return 
 If the function should give back a result, use return.
 If not, the function just performs its task.'''

#example
def add_numbers(a, b):   
    result = a + b       
    return result        


#Calling the function:
print(add_numbers(5, 3))
#for subtraction
def sub(x,y):#x,y is arguments
    return x-y
print(sub(5,2))
#TYPES OF ARGUMENTS
'''
1. Positional Arguments
2.Keyword Arguments
3.Default Arguments
4.Variables-length Arguments
'''
print()
#positional arguments 
#values are passed in the same  order as parameters are defined.
def student(name,age):
    print(f"hello {name},your are {age} years old!")
student("sourabh",20)
def ss(name,occupation):
    print(f"Hi {name} is you're {occupation} in the office?")
ss("Prabhakar","Sales Manager")#here name="Prabhakar",occupation="Sales Manager"

#Keyword Arguments
#directly specifying the keyword to the specific argument 
#like 
ss(name="Prabha",occupation="Sales Manager")
#above line im directly adding the keywords to the arguments
#output=Hi Prabha is you're Sales Manager in the office?

#3.Default Arguments
#here the parameters have the default value if i cannot specify value
def about(name,age=19):
    print(f"hi {name} i think  your are {age} years old.")
about("Soumya")#here the value is not specified but it uses the current default value as age
#4. Variable-Length Arguments
#this is used when user don't know how many values will be passed
#in this argument we have two types
#a.args(Non-keyword arguments)
#it collects the extra positional argument into a tuple
def add_numbers(*args):
    print(sum(args))
add_numbers(1,2,3,55)#it gives output has -61
#b.**kwargs(keyword arguments)
#it collects extra keyword arguments into a dictionary
def details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
details(name="siksha",age=20,city="Bombay")
#output is-
'''
name: siksha
age: 20
city: Bombay
'''
#it gives output has func(a=1,b=2) etc

#Lambda Function or Anonymous Function
#A Lambda function is an anonymous function (no name) created using the lambda keyword
#syntax:
#lambda arguments: expression
add=lambda x:x**2
print(add(x=9))#output=81

multiplying=lambda z,x:z*x
print(multiplying(3,898))
#in above code i used multiple Arguments 
#the output=2694

notice=lambda: print("Tomorrow is holiday on the occasion of Diwali! \n so school is opened on 19-05-2026")
notice()
#solving the real time problems 
#1-question 
'''
1. you have a list of students with their attendance percentage :
attendance=[("Ravi",85),("Ananya",72),("Kiran",60),("Meena",95)]
Use filter() with lambda to find students who have less than 75% attendance (and need to be warned)'''
#so using lambda and filter functions trace out the below 75% attendance student(and need to be warned)
attendance=[("Ravi",85),("Ananya",72),("Kiran",60),("Meena",95)]
less_75=list(filter(lambda student: student[1]<75, attendance))
print(less_75)
for name, marks in less_75:
    print(f"Warning:{name} your attendance is {marks}% so, please improve.")
#the output is
'''
[('Ananya', 72), ('Kiran', 60)]
Warning:Ananya your attendance is 72% so, please improve
Warning:Kiran your attendance is 60% so, please improve
'''
#and i need to greet the above 75% students so again using the filter function
above_75=list(filter(lambda  student: student[1]>=75, attendance))
print(above_75)
for name,marks in above_75:
    print(f"Great job {name} your attendance is {marks}% keep it up well done")
#output=[('Ravi', 85), ('Meena', 95)]
#Great job Ravi your attendance is 85% keep it up well done
#Great job Meena your attendance is 95% keep it up well done
#write a function that displays a string repeatedly.
def func():
    for i in range(5):
        
        print(i,"hello world")#here i=0 then print "hello world" and function call itself recursively
func()
#here how to calculate the sport analytics (strike rate)
def strike_rate_calculator(runs,balls_faced):
    return(runs/balls_faced)*100
print(int(strike_rate_calculator(50,33)))
#output=151
#write a function to check even or odd number
def tester():
   # num=int(input("enter the random number:"))
    if num%2==0:
        return "Even"
    else:
        return "Odd"
#print(tester())#it prints the whatever function returned in the console
#output:
'''
enter the random number:567839
Odd'''
#squaring a number
def square(num):
    return num*num
print(square(34))
#output=1156
#cubing a number
def cubing(num):
    return num**3
print(cubing(6))
#output=216
#finding the maximum of the given numbers by using the function
def find_max(a,b,c):
    if (a>b)and(a>c):
        return a
    elif (b>a)and(b>c):
        return b
    else:
        return c
print(find_max(45,22,29))
#output=45
#write a program to check whether it is a palindrome or not
#palindrome is a string which is same meaning when the string is reversed also.
def palindrome_check(text):
    return text==text[::-1]
print(palindrome_check("madam"))
#output=True

#sum of the digits
def sum_of_digits(n):
    total=0
    while n>0:
        r=n%10
        total+=r
        n//=10#it removes the last digit
    return total
print(sum_of_digits(1213))
#output=7
#for counting the vowels in the given string
def counting_vowels(text):
    count=0
    vowels="aeiouAEIOU"
    for i in text:
        if i in vowels:
            count+=1
    return count
print(counting_vowels("HE IS A GOOD BOY"))
#for counting the consonants in the given string
def counting_consonants(text):
    count=0
    vowels="aeiouAEIOU"
    for j in text:
        if j.isalpha() and j not in vowels:
            count+=1
    return count
print(counting_consonants("HE IS A GOOD BOY"))






