#importing the numpy library
import numpy as np
#alias-np

np.array([1,2,3])
#for checking the array dimension 
arr=np.array([1,2,3])
print(arr.ndim)
#1
#so firstly above array has one dimension because it has only one row
#if i has row and column then it is 2 
#example
a=np.array([[1,2,3],[4,2,3]])
print(a.ndim)
#it prints '2'
aa=np.array([[[]]])

print(aa.ndim)
#3
print(aa.shape)
#instead of using for loop 
#i use the np.arange(,,)
range=np.arange(1,10,2)
print(range)
#[1 3 5 7 9]
arr=np.linspace(0,1,5)
print(arr)

#here it evenly space  like 0,0.25,0.5,0.75 like that
b=np.linspace(0,4,7)
print(b)
'''[0.         0.66666667 1.33333333 2.         2.66666667 3.33333333
 4.        ]'''
#here from 0-4 it evenly space upto 7 values

#np.logspace
#it is basically used to logarithmic scale array

#a=np.logspace(start,end-powers,3-no of values we need)
d=np.logspace(1,3,4) #np.logspace(10^1-10^3,4-values)
print(d)
#[  10.           46.41588834  215.443469   1000.        ]
#np.zeros()-array full of zeros
arr=np.zeros(4)
print(arr)
#[0. 0. 0. 0.]
#that is only one dimensional 
#now im creating the 2 dimensional array
h=np.zeros([2,3])#two rows and three columns
print(h)
#for 3-D
hh=np.zeros([2,3,4])#2-blocks,3-rows,4-cols
print(hh)
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
print(arr)
#i also declare the data type also
a=np.ones([2,3],dtype=int)
print(a)
'''
[[1 1 1]
 [1 1 1]]'''
b=np.ones([2,3],dtype=float)
print(b)
'''
[[1. 1. 1.]
 [1. 1. 1.]]'''
