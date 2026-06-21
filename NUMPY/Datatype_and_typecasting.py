#NUMPY DATA TYPE
#the data types which is in numpy
import numpy as np
arr=np.array([1,2,3,4,3.1])
print(arr)
#my array is:
#[1.  2.  3.  4.  3.1]
#for checking which type
print(type(arr))
#so it is 
#<class 'numpy.ndarray'>
lst=["str",3,4.2,"doom"]
arr=np.array(lst)
print(arr)
#i passed the list into my array then all the elements in the list becomes strings
#['str' '3' '4.2' 'doom']
print(type(lst))
#<class 'list'>
#in the numpy Data types  
'''it basically stores as 1. int32 which is low valued integers like 3,2,5.etc
and  2.'int64' =large integers like 1000,2078 etc..
3.float32 smaller float values of 32 bits like 1.0,2.12 etc..
4.float64  and this float64 is default like 1.0000 
5.bool for boolean (True/False)
6.complex number like 1+2j,3-4j
7.str for Unicode string like "hello","apple" etc.'''

#so now im creating an array which containing only integers
arr=np.array([1,2,3,4,52])
print(arr)
#now it prints in integers 
#[ 1  2  3  4 52]
#if i add one float then my array changed like float 
arr=np.array([1,2.9,3,4,52])
print(arr)#output in floats
#[ 1.   2.9  3.   4.  52. ]
#now if i add one string then my array totally converted into string
arr=np.array([1,2,3,4,52,"str"])
print(arr)
#output=['1' '2' '3' '4' '52' 'str']
print(arr.dtype)
#<U21
arr=np.array([1,2.9,3,4,52],dtype=np.int64)
print(arr)
#[ 1  2  3  4 52]
#it converted my float value to the integer of 64 bit
arr=np.array([1,2.9,3,4,52],dtype=np.float64)
print(arr)
arr_ss=np.array([3.9854663,4.2763283,36.732983],dtype=np.float16)
print(arr_ss)
#it converted my float values to float16
#[ 3.986  4.277 36.72 ]
arr_ss=np.array([3.9854663,4.2763283,36.732983],dtype=np.float64)
print(arr_ss)
#[ 3.9854663  4.2763283 36.732983 ]
print(arr_ss.dtype)
#float64

#TYPE CASTING
print("------------------")
#converting one datatype to another type that is type casting
#using astype()
arr=np.array([1,2,3])
print(arr.dtype)
#int64
#for converting the int64 to float64
new_arr=arr.astype(np.float64)
print(new_arr)
print(new_arr.dtype)
#output=
'''
[1. 2. 3.]
float64'''
arr_new2=new_arr.astype(np.int64)
print(arr_new2.dtype)
#int64

#ERRORS IN TYPE CASTING
#arr=np.array(["1","2","hello"])
#arr2=arr.astype(np.int64)
#print(arr2)
#valueError
#whenever we want to convert the multiple datatypes then it rises error

