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
#print(s.values)#[12  3  4 54  2  1]
#print(s[2])#4
#indexing by using function is ->iloc
#print(s.iloc[2])#4

#if i need many number of indexes
#print("---------")
#print(s.iloc[[2,3,4]])
#print("---------")
'''
---------
2     4
3    54
4     2
dtype: int64
---------
'''
s.name="Numbers"
#print(s.name)
#print(s[0:5:2])
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
#print(s2)
'''
Name: Fruits, dtype: int64
Ramesh     4500
Priya     52500
Arjun     60000
Sneha     48000
Kiran     55000
Meena     47500
Vivek     50000
Anjali    58000
Rohit     62000
Kavya     46500
Name: salaries, dtype: int64
'''
 #CONDITIONAL SELECTION
#print(s2[s2>50000])
#it prints all greater than valued rows with name
'''
Priya     52500
Arjun     60000
Kiran     55000
Anjali    58000
Rohit     62000
Name: salaries, dtype: int64
'''
#print(s2[s2>=46500])
#it prints all greater than or equal to 46500
'''
Priya     52500
Arjun     60000
Sneha     48000
Kiran     55000
Meena     47500
Vivek     50000
Anjali    58000
Rohit     62000
Kavya     46500
Name: salaries, dtype: int64
'''
#logical operators
#using and operator which is &

#print(s2[~(s2>50000)])
'''
Ramesh     4500
Sneha     48000
Meena     47500
Vivek     50000
Kavya     46500
Name: salaries, dtype: int64'''

#print(s2[(s2>=50000) & (s2<60000)])
'''
Priya     52500
Kiran     55000
Vivek     50000
Anjali    58000
Name: salaries, dtype: int64'''
#or=!

#MODIFYING
s2["Ramesh"]=45000
print(s2)
#now 4500 to 45000 it will be changed

import numpy as np
ser=pd.Series(['a',np.nan,1,np.nan,2])
#print(ser.notnull().sum())
#3
#print(ser.notnull())
'''
0     True--->
1    False
2     True--->   which is 1+1+1=3
3    False
4     True--->
dtype: bool'''
#print(ser.isnull().sum())#2 
#here actually the sum() is not adding the null numbers
#in pandas it will give a boolean representation how many Trues it will be the answer 
#Example in the above
#print(ser.isnull())
'''
0    False
1     True --->1 ↘
2    False         ↠ which is 1+1=2
3     True ---> 1↗
4    False
dtype: bool'''

# Student marks dataset
data = {
    "students": ["Ravi", "Anita", "Sai", "Meena"],
    "Math": [85, 78, 92, 70],
    "Science": [88, 74, 90, 65],
    "English": [80, 82, 85, 75],
    "History": [70, 68, 75, 60]
}
df=pd.DataFrame(data)
#print(df)
'''
  students  Math  Science  English  History
0     Ravi    85       88       80       70
1    Anita    78       74       82       68
2      Sai    92       90       85       75
3    Meena    70       65       75       60
'''
#i just converted into dataframe
#print(df.head(2))
#if i want first two rows i use here head function
#but now this time i need the last two rows of the dataframe
#then im using tail() function
#print(df.tail(1))
'''
  students  Math  Science  English  History
3    Meena    70       65       75       60'''

#loc and iloc functions
#print(df.iloc[1:3])#im fetching the index 1 and 2 rows
#iloc[start:end]

#instead of having all the row i need separated with separate cols which
#i need i use function 'loc[start:end,["col_name","col2_name"]]-->format
#print(df.loc[0:3,["students","History"]])#but in indexes ending also included
'''
  students  History
0     Ravi       70
1    Anita       68
2      Sai       75
3    Meena       60
'''
#print(df.iloc[:3,::-4])#[no of rows and end value not included,start:end:step]

#if i need only particular column i can directly access it
#print(df["students"])
#if i need another col with all rows
#simply im adding the another col
#print(df[["students","Science"]])

#if i want to drop the data set at particular col or row
#row =0,col=1
print(df.drop("Math",axis=1))
'''
  students  Science  English  History
0     Ravi       88       80       70
1    Anita       74       82       68
2      Sai       90       85       75
3    Meena       65       75       60
'''
#here in above dataset the entire 'Math' col
#now i need to remove the 'sai' row in students
print(df.drop(2,axis=0,inplace=True))#inplace is used to modify the data set after changes
#print(df)
'''
  students  Math  Science  English  History
0     Ravi    85       88       80       70
1    Anita    78       74       82       68
3    Meena    70       65       75       60
'''
#here i already deleted the math col but it is there because i dont use inplace=True so it 
#returns new dataset
#print(df.shape)
new_data={
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Department": ["HR", "Finance", np.nan, "IT", "Marketing"],
    "Salary": [50000, np.nan, 60000, 55000, np.nan],
    "JoiningDate": ["2020-01-15", "2019-11-23", "2021-06-10", np.nan, "2022-03-05"]
}
df=pd.DataFrame(new_data)
#print(df)
'''
   EmployeeID     Name  ...   Salary  JoiningDate
0         101    Alice  ...  50000.0   2020-01-15
1         102      Bob  ...      NaN   2019-11-23
2         103  Charlie  ...  60000.0   2021-06-10
3         104    David  ...  55000.0          NaN
4         105      Eve  ...      NaN   2022-03-05

[5 rows x 5 columns]'''
#for checking other inf
#information about my datatype using info()
#print(df.info())
#output:
'''
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 5 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   EmployeeID   5 non-null      int64  
 1   Name         5 non-null      str    
 2   Department   4 non-null      str    
 3   Salary       3 non-null      float64
 4   JoiningDate  4 non-null      str    
dtypes: float64(1), int64(1), str(3)
memory usage: 417.0 bytes
None'''

#Broadcasting in Pandas
df["Salary"]=df["Salary"]+5000
#print(df["Salary"])
'''
0    55000.0
1        NaN
2    65000.0
3    60000.0
4        NaN
Name: Salary, dtype: float64
'''
#renaming concept
#renaming the column name 
#now inplace of EmployeeID i want to replace with the Emp_ID
df.rename(columns={"EmployeeID":"Emp_ID"},inplace=True)
#print(df)
#now my col name of EmployeeID is changed to the Emp_ID
df.rename(columns={"Department":"Dept"},inplace=True)
#print(df)
#print(df["Salary"].unique())
#[55000.    nan 65000. 60000.]
print(df["Dept"].value_counts())#this function returns the number of counts the particular col have
'''
Dept
HR           1
Finance      1
IT           1
Marketing    1
Name: count, dtype: int64'''
print(df)
#i want to create a new col
df["retired emp"]=df["Emp_ID"]
print(df)
#cleaning
print(df.isnull().sum())
