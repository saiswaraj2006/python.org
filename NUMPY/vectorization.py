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

