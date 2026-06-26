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