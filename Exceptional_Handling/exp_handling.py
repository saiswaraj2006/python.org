try:
    num=int(input("Enter a number:"))
    result=10/num
    print("Results:",result)
except ZeroDivisionError:#if zerodivisionerror is come then it prints the 
    #down print statement
    print("Error: Cannot divide by zero.")
except ValueError:
    #if i entered the char,float,str different dataset from int it prints the down print statement
    print("Error: Invalid input, please enter a number.")
finally:
    print("Execution finished")
    #the above finally block is always prints at end
'''
Enter a number:0
Error: Cannot divide by zero.
Execution finished
'''
#another example
'''
Enter a number:3.5
Error: Invalid input, please enter a number.
Execution finished
'''

#Raising the exceptions 
def check_name(name):
    if not isinstance(name,str):
        raise ValueError("Name must be in string format!")
    return name
print(check_name(name="shiva"))

#print(check_name(name=12))

def checking_name(name):
    if not name.isalpha():
        raise ValueError("Name must contain only alphabets.")
    return name
#print(checking_name("shiva123"))#it returns ValueError
print(checking_name("ganga"))