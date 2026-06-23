#performing the arithmetic operations by using numpy
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
#addition 
print(a+b)
#[5 7 9]
#subtraction
print(a-b)
#[-3 -3 -3]
print(b-a)
#[3 3 3]
#multiplication
print(a*b)
#[ 4 10 18]

#Division(/)
print(a/b)
#[0.25 0.4  0.5 ]
print(b/a)
#[4.  2.5 2. ]
#for integer division(//)
print(a//b)
#[0 0 0]→it prints only integer values
print(b//a)
#[4 2 2]
#Modulus-remainder
print(a%b)
#[1 2 3]

#Exponent->Power
print(a**b)
#[  1  32 729]
print(a**2)