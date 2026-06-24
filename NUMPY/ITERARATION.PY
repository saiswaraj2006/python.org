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