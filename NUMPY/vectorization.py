import numpy as np
#vectorization:
#np.vectorize()->Convert a regular function to be applied on an array.
def square(x):
    return x*x
vfunc=np.vectorize(square)
arr=np.array([1,3,4,5])
print(vfunc(arr))

def add(a,b):
    return a+b
fun=np.vectorize(add)
c=np.array([[21,32,43],[32,41,55]])
print(fun(c[0],c[1]))
#[53 73 98]

#np.inf and -np.inf->positive and negative infinities 
#np.isnan
#np.isinf
#np.isfinite
#These are the functions used to detect any null values,
#infinite value or finite values

#For checking the is array has  a number or not
#using np.isnan()
my_arr=np.array([2.1,3,np.nan,np.inf, 0,45])

print(np.isnan(my_arr))
#[False False  True False False False]

#np.isinf(x)->checks for infinity(+inf or -inf)
my_arr=np.array([2.1,3,np.nan,np.inf,-np.inf,0,45])
print("Nan check:",np.isnan(my_arr))
print("inf check:",np.isinf(my_arr))
print("Finite check:",np.isfinite(my_arr))
'''
Nan check: [False False  True False False False False]
inf check: [False False False  True  True False False]
Finite check: [ True  True False False False  True  True]
'''

#Flitter out nan and inf
cleaned_arr=my_arr[np.isfinite(my_arr)]
print("clean array:",cleaned_arr)
'''
clean array: [ 2.1  3.   0.  45. ]
'''
new_array=np.nan_to_num(my_arr)
print("my_arr",my_arr)
print(new_array)
#here when i use nan_to_num method then the 'not a number' function is changed to the any 0 value
#and the +inf->changed to very large number
#-inf->changed to very large negative number
'''
[ 2.10000000e+000  3.00000000e+000  0.00000000e+000  1.79769313e+308
 -1.79769313e+308  0.00000000e+000  4.50000000e+001]
'''
print("Before changed",np.isfinite(my_arr))
print("After changed:",np.isfinite(new_array))
'''
Before changed [ True  True False False False  True  True]
After changed: [ True  True  True  True  True  True  True]
'''
#so,here After changed there are all finite values in array
print(np.isnan(my_arr))
print(np.isnan(new_array))