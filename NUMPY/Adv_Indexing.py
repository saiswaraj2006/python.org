#Index Arrays also known as Advanced Indexing
#in order to access index values from the array we can create an array/list of indices to access specific elements of another array.
#np.take->built in function to perform indexing and slicing 

import numpy as np
arr=np.array([10,20,30,40,50])
ind=[0,2]
print(np.take(arr,ind))#[10 30]
ind2=[0,1,4]
print(np.take(arr,indices=1))#20
print(np.take(arr,ind2))#[10 20 50]
