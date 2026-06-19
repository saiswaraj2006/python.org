#importing the numpy library
import numpy as np
#alias-np

np.array([1,2,3])
#for checking the array dimension 
arr=np.array([1,2,3])
#print(arr.ndim)
#1
#so firstly above array has one dimension because it has only one row
#if i has row and column then it is 2 
#example
a=np.array([[1,2,3],[4,2,3]])
#print(a.ndim)
#it prints '2'
aa=np.array([[[]]])

#print(aa.ndim)
#3
#print(aa.shape)
#instead of using for loop 
#i use the np.arange(,,)
range=np.arange(1,10,2)
#print(range)
#[1 3 5 7 9]
arr=np.linspace(0,1,5)
#print(arr)

#here it evenly space  like 0,0.25,0.5,0.75 like that
b=np.linspace(0,4,7)
#print(b)
'''[0.         0.66666667 1.33333333 2.         2.66666667 3.33333333
 4.        ]'''
#here from 0-4 it evenly space upto 7 values

#np.logspace
#it is basically used to logarithmic scale array

#a=np.logspace(start,end-powers,3-no of values we need)
d=np.logspace(1,3,4) #np.logspace(10^1-10^3,4-values)
#print(d)
#[  10.           46.41588834  215.443469   1000.        ]
#np.zeros()-array full of zeros
arr=np.zeros(4)
#print(arr)
#[0. 0. 0. 0.]
#that is only one dimensional 
#now im creating the 2 dimensional array
h=np.zeros([2,3])#two rows and three columns
#print(h)
#for 3-D
hh=np.zeros([2,3,4])#2-blocks,3-rows,4-cols
#print(hh)
'''
output:
[[[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]'''
#np.ones()
#it used to prints all the values as one
arr=np.ones([4,2])
#print(arr)
#i also declare the data type also
a=np.ones([2,3],dtype=int)
#print(a)
'''
[[1 1 1]
 [1 1 1]]'''
b=np.ones([2,3],dtype=float)
#print(b)
'''
[[1. 1. 1.]
 [1. 1. 1.]]'''

#empty() 
#creates an array without initializing values
a=np.empty((3,3))
print("\nEmpty Array: \n",a)#it prints empty uninitialized values
'''
Empty Array: 
 [[6.95319127e-310 6.95329883e-310 6.95319127e-310]
 [2.02369289e-320 0.00000000e+000 0.00000000e+000]
 [0.00000000e+000 0.00000000e+000 0.00000000e+000]]
'''
#full()
#the specific values which i initialize
arr_full=np.full((3,3),7)
print("\n Full Array(7): \n",arr_full)
'''
Full Array(7): 
 [[7 7 7]
 [7 7 7]
 [7 7 7]]
'''
arr_full=np.full((2,2),0)
print("\nFull Array (0's):\n",arr_full)
#output 
'''
Full Array (0's):
 [[0 0]
 [0 0]]
'''
#for identity matrix
#i use eye()
I=np.eye(4)#for 4*4 matrix
print("Identity Matrix\n",I)
'''
Identity Matrix
 [[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]'''
I=np.eye(1)
print("Identity Matrix\n",I)
'''
Identity Matrix
 [[1.]]'''
#actually there is no need of identity matrix of one 
#Diagonal matrix with custom values
D=np.diag([10,20,30])
print("Diagonal Matrix\n",D)
'''
Diagonal Matrix
 [[10  0  0]
 [ 0 20  0]
 [ 0  0 30]]
 '''
