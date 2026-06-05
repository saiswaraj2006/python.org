def celsius_to_fahrenheit(c):
    return(c*9/5)+32
if __name__=="__main__":

#above condition runs only during the testing of this file only
    assert celsius_to_fahrenheit(0)==32
    print("Test is passed")
#here 'assert' is a keyword in python used to test the condition 
#if condition is true nothing happens and program moves to next line
#if condition is false python stops the execution and raises error like 'AssertionError'

