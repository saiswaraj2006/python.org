#Dunder
#dunder stands for double underscore
'''__init__
used to construct or crete a new object
'''
str1="hello"#every thing created is an object like str1
str2="world"
new_str=str1+str2
print(new_str)
#it runs because both objects are two types
#now +is assigning both 
def func():
    pass
print(type(func))
#<class 'function'>

#Rather than using the + operator now im using the '__' double underscore method
new=str1.__add__(str2)
print(new)#helloworld
#normally 
n=len(str1)
print(n)
#but __len__ function is there which is used 
nn=str1.__len__()
print(nn)
#now the output of both is same 5
