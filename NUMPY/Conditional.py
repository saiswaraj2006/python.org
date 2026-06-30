#conditional operations
#here i can perform  conditional based operations on the array
import numpy as np
arr=np.array([-2,-3,-1,1,2,3,4,5])
result=np.where(arr>0,"Positive","Negative")
print(result)
#positive if the condition is true and negative if the condition is false
#output
'''['Negative' 'Negative' 'Negative' 'Positive' 'Positive' 'Positive' 'Positive' 'Positive']'''
result=np.where(arr>0,"High","Low")
print(result)

#Argwhere
#basically for row and column arrays like 2D
a=np.array([10,20,30,40])
print(np.argwhere(a>20))
'''
output:
[[2]
 [3]]
'''
#at index 2,3 i have the greater than 20 
#now i wanna check is my array has greater than or equal to the 20 
print(np.argwhere(a>=20))
'''
[[1]
 [2]
 [3]]
'''
mask=np.logical_and(a>10,a<30)
print(mask)
'''
[False  True False False]'''
#above the logical and checks both condition if both are true then it is true
#else false
#At Index 1 both conditions are satisfy so it returns True

#now i check for 2D array
two_D_array=np.array([[1,2,33],
                      [23,45,50],
                      [12,32,61]])
print(np.argwhere(two_D_array>=15))
'''
[[0 2]-->>index[0,2]means at 0rth row and 2nd col means->33
 [1 0]-->>1st row and 0rth col-->>23
 [1 1]
 [1 2]
 [2 1]
 [2 2]]
'''
#it returns the indexes where it satisfies the condition
copy=np.logical_and(two_D_array>=35,two_D_array<100)
print(copy)
'''
[[False False False]
 [False  True  True]
 [False False  True]]'''
c=np.logical_or.reduce([two_D_array<12,two_D_array>12,two_D_array<32,two_D_array>32])
print(two_D_array[c])
#output=[ 1  2 33 23 45 50 12 32 61]
#Because i need the all values other than 12 and 32
#np.take()->fetch values at the indices
rows=np.take(two_D_array,[0,2],axis=0)
print("Rows 0 and 2:\n",rows)
'''
Rows 0 and 2:
 [[ 1  2 33]
 [12 32 61]]
'''
arr=np.array([1,2,3,5,0])

#nonzero
print(np.nonzero(arr))
#(array([0, 1, 2, 3]),)it prints the indices of the non zero values
