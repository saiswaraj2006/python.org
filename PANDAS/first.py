import pandas as pd
s=pd.Series([12,3,4,54,2,1])
print(s)

'''
0    12
1     3
2     4
3    54
4     2
5     1
dtype: int64
'''
#if i add a string into the s then the entire series converted into object 
#that means all the integers converted into the strings
print(s.values)#[12  3  4 54  2  1]
print(s[2])#4
#indexing by using function is ->iloc
print(s.iloc[2])#4

#if i need many number of indexes
print("---------")
print(s.iloc[[2,3,4]])
print("---------")
'''
---------
2     4
3    54
4     2
dtype: int64
---------
'''
s.name="Numbers"
print(s.name)
print(s[0:5:2])
'''
Numbers
0    12
2     4
4     2
Name: Numbers, dtype: int64
'''
index=["apple","banana","lemon","kiwi","papaya"]
s.name="Fruits"
print(s)
emp_salaries={
    'Ramesh' :4500, 
    'Priya' : 52500, 
    'Arjun' : 60000, 
    'Sneha' : 48000, 
    'Kiran' : 55000, 
    'Meena' : 47500, 
    'Vivek' : 50000, 
    'Anjali': 58000, 
    'Rohit' : 62000, 
    'Kavya' : 46500 
}

s2=pd.Series(emp_salaries,name="salaries")
print(s2)