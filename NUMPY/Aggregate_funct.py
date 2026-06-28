#aggregate functions
#they are used to perform a specific operation by using inbuilt function
import numpy as np
arr=np.array([1,2,3,4,5])
print(np.sum(arr))#returns the sum of all elements in the array
print(np.mean(arr.astype(float)))#returns the mean of all elements in the array
print(np.median(arr))#returns the median of all elements in the array
print(np.std(arr))#returns the standard deviation of all elements in the array
print(np.var(arr))#returns the variance of all elements in the array

print(np.min(arr))#1
print(np.max(arr))#5

matrix=np.array([[1,2,3],
                 [4,5,6]])
print(np.sum(matrix,axis=0))#returns the sum of all elements in the array along the specified axis
#like 1+4=5, 2+5=7, 3+6=9
print(np.sum(matrix,axis=1))#returns the sum of all elements in the array
#like 1+2+3=6, 4+5+6=15

#cumulative sum and product
arr=np.array([1,2,3])
print(np.cumsum(arr))
#it returns the cumulative sum of the elements in the array
#like 1, 1+2=3, 1+2+3=6
print(np.cumprod(arr))
#it returns the cumulative product of the elements in the array
#like 1, 1*2=2, 1*2*3=6
new_arr=np.array([[1,2,4,5],
                  [2,3,4,5]])
print(np.shape(new_arr))
#(2, 4)
print(np.cumsum(new_arr))
#1,1+2=3,3+4=7,7+5=12,12+2=14,14+3=17 etc..
#output=[ 1  3  7 12 14 17 21 26]
print(np.cumprod(new_arr))