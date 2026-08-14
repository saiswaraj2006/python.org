'''try:
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
    print("Execution finished")'''
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
'''
Write a Python function divide_numbers(a, b) that:

Takes two inputs a and b.
Returns the result of a / b.
Raises a ValueError if either input is not a number.
Handles division by zero gracefully with a custom error message.
Always prints "Operation complete" at the end (using finally).'''
try:
    def divide_numbers(a,b):
        return a/b
    print(divide_numbers(a,10))
except ZeroDivisionError:
    print("Error:Zero Division Error ")
except ValueError:
    print("Error:Values must be numbers  ")
except NameError:
    print("Error: name is not defined")
finally:
    print("Operation completed!")

'''
Error: name is not defined
Operation completed!
'''
#using another way to implement
def divide_number(a,b):
    try:
        if not isinstance(a,(int,float)) or  not isinstance(b,(int,float)):
            #here im using the or and checking is that is num or what 
            raise ValueError("Inputs must be numbers.")
        result=a/b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError as e:
        return "Error:",e
    finally:
        print("Operation complete.")
print(divide_number(10,2))
#5.0
print(divide_number(10,0))
'''
Error: Cannot divide by zero.
Operation complete.
'''
print(divide_number("tt",2))
'''
Error: Inputs must be numbers.
Operation complete.
'''
#Question-2
'''
Write a Python function read_file(filename) that:

Opens a file in read mode.
Raises a FileNotFoundError if the file does not exist.
Prints the file content if it exists.
Handles any other unexpected errors gracefully.
Always prints "File operation complete" at the end (using finally).'''


'''from openpyxl import load_workbook
def file_excel(filename):
    try:
        #trying to open the workbook
        workbook=load_workbook(filename)
        sheet=workbook.active
        #printing the first 5 rows as a sample
        for row in sheet.iter_rows(min_row=1, max_row=5, values_only=True):
            print(row)

    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print("Unexpected error:",e)
    finally:
        print("Excel File operation complete.")
file_excel("C:/Users/saisw/OneDrive/Documents/Book1.xlsx")

'''
#it prints the first five lines
'''
Write a Python function validate_excel(filename) that:

Opens the given Excel file using openpyxl.
Reads the first column of the active sheet.
Raises a ValueError if any cell in the first column is empty.
Prints "Validation complete" at the end (using finally).
'''
from openpyxl import load_workbook
def validate_excel(filename):
    try:
        workbook=load_workbook(filename)
        sheet=workbook.active
        for col in sheet.iter_cols(min_col=1, max_col=2,values_only=True):
            print(col)
    except ValueError:
        print("Error: The First column is empty.")
    finally:
        print("Validation is complete")
validate_excel("Book1.xlsx")
#now for validate and sum of all ages if valid
#and returns "summation complete" at end
from openpyxl import load_workbook
def validate_and_sum(filename):
    try:
        workbook=load_workbook(filename)
        sheet=workbook.active
        for col in sheet.iter_cols(min_col=2,max_col=2,values_only=True):
            print(f"sum of all ages is :{sum(col)}")
    except ValueError:
        print("Error: The second col is empty.")
    finally:
        print("validation is completed")
validate_and_sum("Book1.xlsx")#sum of all ages is :277







