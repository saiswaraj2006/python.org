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
print(np.stack((a,b),axis=0))
print(np.stack((a,b),axis=1))