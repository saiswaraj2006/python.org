#ITERATING 
import numpy as np
arr=np.array([[1,2],[5,6]])
print(arr.ndim)#2
for i in np.nditer(arr):
    print(i,end=" ")
#1 2 5 6
#it iterates through the array and prints the elements
#now i need the index+value then
#use ndenumerate()->both value+index
print()
for ind, x in np.ndenumerate(arr):
    print(ind, x)
#output
'''
(0, 0) 1#at index 0,0 i have the value is 1
(0, 1) 2
(1, 0) 5
(1, 1) 6'''
#view and copy
#view->it does not create a new array, it just creates a view of the original array
#copy->it creates a new array and copies the data from the original array
arr1=np.array([1,2,3,4,5])
view=arr1[1:3]
print(view[0])#2
print(arr1[1])#2
view[0]=10
print(view[0])#10
print(arr1)
#[ 1 10  3  4  5]->so i see the change in the original array as well because view is just a view of the original array
#copy
copy=arr1.copy()
copy[0]=100
print(copy[0])#100
print(arr1[0])#1 because copy is a new array and it does not affect the original array

