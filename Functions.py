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



