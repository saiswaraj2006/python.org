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

#Flitter out nan and inf
cleaned_arr=my_arr[np.isfinite(my_arr)]
print("clean array:",cleaned_arr)