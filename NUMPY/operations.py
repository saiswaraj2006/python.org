#transpose of a matrix
import numpy as np
arr=np.array([[1,2],[3,4]])
#print(arr.T)#transpose of the matrix
#output
'''
[[1 3]
 [2 4]]'''
#or
#print(arr.transpose())
#output
'''[[1 3]
 [2 4]]'''
#print(np.shape(arr))#shape of the array
#output
#(2, 2)
#print(arr.swapaxes(0,1))#swaps the axes of the array
#likewise, we can use swapaxes to swap the axes of a 3D array

#output
'''
[[1 3]
 [2 4]]'''
#print(arr.flatten())#flattens the array into 1D array
#output
#[1 2 3 4]
#print(arr.ravel())#returns a flattened array, but it is a view of the original array
#output
#[1 2 3 4]
#print(arr.reshape(4,1))#reshapes the array into 4 rows and 1 column
#output
'''
[[1]
 [2]
 [3]
 [4]]'''    
arr=np.array([[[1,2],[3,4]]])
#print(np.shape(arr))#shape of the array
#output
#(1, 2, 2)
#now i can swap the axes of the array
swap=np.swapaxes(arr, 0, 1)
#print(swap)
#swaps the axes of the array
#it swaps the first axis with the second axis
#output
'''[[[1 2]]

 [[3 4]]]'''
#print(np.shape(swap))#shape of the array
#output
#(2, 1, 2)
#now i can swap the axes of the array from 1,2 to 2,1

#CONCATENATION
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[56,89],[12,34]])

#basic i have two stacks one is vertical stack and the other is horizontal stack
#vertical stack->it stacks the arrays vertically
#using vstack() function
print(np.vstack((a,b)))
#output
'''
[[ 1  2]
 [ 3  4]
 [56 89]
 [12 34]]
'''
#next is horizontal stack->using hstack() function
print(np.hstack((a,b)))
'''
[[ 1  2 56 89]
 [ 3  4 12 34]]'''
#instead of vstack and hstack we can also use concatenate() function to concatenate the arrays
#using concatenate() function
print(np.concatenate((a,b),axis=0))
#here axis=0 means rows and axis=1 means columns
print(np.concatenate((a,b),axis=1))
#it prints in horizontal stack
#instead of concatenate we can also use stack() function to stack the arrays
print(np.stack((a,b),axis=0))#axis=0 means row wise
print(np.stack((a,b),axis=1))#axis=1 means column wise

#splitting the array into multiple arrays

import numpy as np
arr=np.array([1,2,3,4,5,6])
print(np.split(arr,3))#splits the array into 3 parts
#output 
'''[array([1, 2]), array([3, 4]), array([5, 6])]'''
print(np.split(arr,2))
#output
'''[array([1, 2, 3]), array([4, 5, 6])]'''
print(np.split(arr,6))
#output
'''[array([1]), array([2]), array([3]), array([4]), array([5]), array([6])]'''
#here it splits the array into equal parts, if the array cannot be split into equal parts then it will raise an error
print(np.hsplit(arr,3))
#it splits the array into 3 parts horizontally
#output

'''[array([1, 2]), array([3, 4]), array([5, 6])]'''
print()
print(np.vsplit(arr.reshape(2,3),2))#here i changed the shape of the array to 2,3 because 
#vsplit() function can only split the array vertically if the array has 2 or more rows
#output 

'''[array([[1, 2, 3]]), array([[4, 5, 6]])]'''

#REPEATING THE ARRAY
import numpy as np
arr=np.array([[1,2],[3,4]])
print(np.repeat(arr,3))
print(np.shape(arr))#2
print(np.repeat(arr,3,axis=0))#repeats the array 3 times along the rows
#output
'''
[[1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]'''
print(np.repeat(arr,3,axis=1))
#output
''' [[1 1 1 2 2 2]
 [3 3 3 4 4 4]]'''  
#tilling the array->it repeats the array along the specified axis
print(np.tile(arr,3))
#output
'''[[1 2 1 2 1 2]
 [3 4 3 4 3 4]]'''


