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





