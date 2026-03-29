print("<<Hello welcome to python by saiswaraj ")
print('''Hello welcome to python by saiswaraj''')
print('Hello welcome to python by saiswaraj')
print('hello welcome'"\n bye good bye")
#above line shows that ''& "" both are used for strings
# note=""&'' these kind of braces should not print in the output only the string can show or displayed on the console screen

a=3.7538284
b=9.e349309
print(a*b)#output=inf which means infinity denotes an arithmetic overflow has occurred
c=3.0e-400/4.3e200
print(c)#outpput=0.0 which means that arithmetic underflow in the result

e=1/3
print(e)#output=0.3333333333333333 which means that where 3 is repeated infinitely,  this is loss of precision problem


## Division with float conversion without using format()
print(float(16/(float(3))))
#output is the 5.333333333333333 which means that float(3)=3.0
# then 16 divided by 3.0
# we got 5.333333333333333
# the outer float converts the output into float but the result already in float so it prints directly5.333333333333333

'''this 'format()' function is used for the producing a numeric string of a floating point value rounded
to a specific number of decimal places'''
## Division with float conversion by using format()
print(format(float(16/(float(3))),'.2f'))
# which means same as the division with float but format() function  '.2f' makes two decimal rounded then prints th value
print(format(float(16/(float(3))), '.3f'))
#here in the above code the'.3f' rounded upto 3 decimal places 
#output=5.333

print(format(1283978,','))
# used to insert comma in the number so the output is 1,283,978

'''python can carry some operations on numbers.To perform a calculation, simply
   enter the numbers and type of the operation you needs to be perform'''
print(12+55-90*50)#output→-4433
print(750-735)#output→15
print(int(96/12))#output→8
''' Division by zero
if 12/0 it generates error 
Traceback(most recent call last):
it prints 'zero division error'''
'''print(15/0) →  print(15/0)
          ~~^~
ZeroDivisionError: division by zero'''

#DIVIDING TWO INTEGERS
#if you want quotient use(//) example
print(78//5)#15 is quotient 
# if you need remainder use(%) modulo symbol
print(78%5)# 3 is remainder

#EXPONENTIATION raising operators one number to the power of another
print(5** 5)
# here 3125 is the output means  step takes 5^5 =3125
# this raising of one number to the power of another is called exponentiation
print(5-+35)#-30
#in the above statement it seems like unusual but it actually works 
#because the (5-+35) is actually denotes unary +35 (5-(+35)) so the operation 5-35=-30 is the output
# \t which inserts tab in a string 
print("hello \t world")
# \n which is used to escape sequence for new line string 
print("hello \n world")

print("hello\fworld")
print("hello\aworld")# which gives beep sound 
# Printing "SAI" using hex escape sequences (ASCII)
print("\x53\x41\x49")
# printing "HELLO" using hex escape sequence 
print("\x48\x45\x4C\x4C\x4F")
# escape sequence \' prints single quote and \" prints double quotes
print('It\'s a sunny day')
print("He said, \"Hello Sai\"")
print("i\'am sai\tswaraj \n this is my best experience in \"2026\"")








