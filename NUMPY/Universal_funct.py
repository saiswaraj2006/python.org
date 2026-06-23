#Ufuncs
import numpy as np
#square root->np.sqrt()
a=np.array([1,4,9,16])
print(np.sqrt)
#<ufunc 'sqrt'>
print(np.sqrt(a))
#[1. 2. 3. 4.]

#Exponential->np.exp->e^x ->x is any integer
print(np.exp(a))
#[2.71828183e+00 5.45981500e+01 8.10308393e+03 8.88611052e+06]
print(np.exp([4]))
#[54.59815003]
print(a)
#sine function ->np.sin
angles=np.array([0, np.pi/2, np.pi] )
print(np.sin(angles))
#[0.0000000e+00 1.0000000e+00 1.2246468e-16]
#here sin(pi/2)=1
#it prints the angles of sine

#cos function
print(np.cos([0]))
#[1.]
b=np.pi
print(np.cos(b))
#-1.0

#Indexing and slicing
I=np.array([1,2,3,4,5,6,7,8,9,10])
print(I[0])#1
print(I[-1])#10 (negative indexing which starts with right to left with -1)
print(I[9])#10(forward indexing which starts with left side of an array with 0)
#slicing
#slicing means which we can access a piece of a list
#in slicing here there are 3 terms->[start:stop:step]
print(I[1:9:2])#two is the step means steps into 2nd value
#[2 4 6 8]

#if i want to access last three digits
#then im using slicing
print(I[-1:-4:-1])
#[10  9  8]
print(I[7:10:1])
#[ 8  9 10]
print(I[ : :2])
#[1 3 5 7 9]
#Multidimensional slicing
matrix=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(matrix)
#now i want to print only two rows with all columns then im using multidimensional slicing
#matrix[start:stop(rows),start:stop(cols)]
print(matrix[0:2, :])
'''output
[[1 2 3]
 [4 5 6]]'''
print(matrix[0:2,0:2])
'''this can access only two rows and two cols of first two rows and cols
[[1 2]
 [4 5]]'''

#i need [[5 6]
         #[8 9]]
print(matrix[1:, 1: ])
#i need [[]]