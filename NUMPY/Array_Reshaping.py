import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr.size)#6
print(arr.shape)#(6,)
reshaped=arr.reshape(2,3)
print(reshaped)
#now the arr.reshape() function reshapes the array without changing the array elements
#it prints in 2-rows and 3-columns
'''output
[[1 2 3]
 [4 5 6]]'''
#now checking the shape of the array
print(reshaped.shape)#(2, 3)
#so here the array shape is changed without changing the elements


'''reshaped2=arr.reshape(3,3)
print(reshaped2)'''
#if i have run the above code it should give 'ValueError' so
#we want to change the shape but in order like what way it should be fit
'''reshaped3=arr.reshape(2,2)
print(reshaped3)'''
#above one also same if you want 2 rows and 2 cols then there is only four
#elements can fit but here the size is changing so it should be valueerror

#if i wanna change my shape by using reshape() then size should be same without changing 
'''RAVEL
ravel is a function that is particularly used to convert 
any array into a 1D array
'''
ravel=reshaped.ravel()
#now first the reshaped array is in 
print(reshaped.ndim)#2
#but  after ravel() function it should be in 1D
print(ravel)
#[1 2 3 4 5 6]
print(ravel.ndim)#1
print(ravel[0])#1
print(ravel[2])#3
print(reshaped)
#so 2D array was changed to 1D array

'''
FLATTEN()
this is also convert any array into the 1D array
but it returns a copy of the array

'''
flat=reshaped.flatten()
print(flat)
#[1 2 3 4 5 6]
flat[0]=200
print(flat)
#[200   2   3   4   5   6]
print(flat[2])#3
print(flat[0])#200
print(reshaped)
#it won't be changed because it returns the copy of that
#print(ravel)
#[1 2 3 4 5 6]
ravel[0]=50
print(ravel)
print(reshaped)
#output
'''
[50  2  3  4  5  6]

[[50  2  3]
 [ 4  5  6]]
'''
#here it changes the reshaped array also 
#if i want a safe copy then i use flatten()
