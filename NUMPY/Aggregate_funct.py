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
#[   1    2    8   40   80  240  960 4800]

#now after learning dealing with nan(not a number )
#now the aggregate functions that ignore NaN
#np.nanmean()
#np.nanmax()
#np.nanmin()
#np.nansum()
arr=np.array([1,np.nan,3,5])
print(np.nanmean(arr))
#3.0 even though it has nan it ignores and do the function 
a=np.array([34,12,np.nan,0,73,4,34])
print("max=",np.nanmax(a))
#max= 73.0
print("min_value:",np.nanmin(a))
#min_value: 0.0

arr=np.array([1,np.nan,np.inf,4,3])
filtered_arr=np.isfinite(arr)
print(arr[filtered_arr])
#[1. 4. 3.]

arr=np.array([np.nan,np.inf,2,45,100,36])
print(np.nansum(arr))