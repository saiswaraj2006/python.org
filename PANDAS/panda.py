import pandas as pd
data={
    'Name':["Arun","Charan","Swathi","Hasan","Shreya"],
    'Age':[22,21,20,19,20],
    'Course':["AI","DS","DS","CS","AI"],
    'Fee':[150000,120000,120000,135000,150000],
    'Gpa_Marks':[10,9.9,9.9,8,7.5]
}
df=pd.DataFrame(data)
print(df)
#now i want to add another column
df["Discount_Fee"]=df["Fee"]*0.9
#means i want to declare 10% of discount
print(df)
''' 
    Name  Age Course     Fee  Gpa_Marks  Discount_Fee
0    Arun   22     AI  150000       10.0      135000.0
1  Charan   21     DS  120000        9.9      108000.0
2  Swathi   20     DS  120000        9.9      108000.0
3   Hasan   19     CS  135000        8.0      121500.0
4  Shreya   20     AI  150000        7.5      135000.0
'''
#adding another col
df["City"]=["HYD","WGL","DELHI","KZP","HYD"]
print(df)
#now i want to delete the col 
print(df.drop("Age",axis=1,inplace=True))
print(df)
#or
#del df["Age"]
#print(df)
new_row=pd.DataFrame([{"Name":"Roshan",
                       "Course":"AI",
                       "Fee":150000,
                       "Gpa_Marks":8.7
                       }])
df=pd.concat([df, new_row],ignore_index=True)
#print(df)
#now i need the students who got 8.5 above
#print(df['Gpa_Marks']>=8.5)
'''
0     True
1     True
2     True
3    False
4    False
5     True
Name: Gpa_Marks, dtype: bool
'''
#print(df.iloc[::2])
'''
     Name Course     Fee  Gpa_Marks  Discount_Fee   City
0    Arun     AI  150000       10.0      135000.0    HYD
2  Swathi     DS  120000        9.9      108000.0  DELHI
4  Shreya     AI  150000        7.5      135000.0    HYD
'''
df["Name"]=df["Name"].replace("Arun","Ajay")
#print(df)#now here it will be changed in the original data
#Duplicates:
#checking all duplicates values
print(df)
#dd=df.drop_duplicates()->for remove duplicates
#print(dd)

#invalid values
#lambda-> function
df["Discount_Fee"]=df["Discount_Fee"].apply(lambda x: x*0.9 if x>=120000 else x)
print(df)
'''
     Name Course     Fee  Gpa_Marks  Discount_Fee   City
0    Ajay     AI  150000       10.0      121500.0    HYD--- these three cols has been given again 10% of discount when the condition is true
1  Charan     DS  120000        9.9      108000.0    WGL
2  Swathi     DS  120000        9.9      108000.0  DELHI
3   Hasan     CS  135000        8.0      109350.0    KZP---
4  Shreya     AI  150000        7.5      121500.0    HYD---
5  Roshan     AI  150000        8.7           NaN    NaN
'''
print(df)#when i print the real table the above 10% discount col is updated successfully

#apply and lambda
#first adding the age column
df["Age"]=[19,20,21,20,19,20]
print(df)
df["Age"]=df["Age"].apply(lambda x:x-1)
print(df)

#JOINS
#Merges

import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 18, 47],
    'Salary': [50000, 60000, 30000, 80000]
}
df = pd.DataFrame(data)

# Example 1: Apply lambda to a column
# Increase salary by 10%
df['Updated_Salary'] = df['Salary'].apply(lambda x: x * 1.10)

# Example 2: Apply lambda across rows
# Categorize age groups
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Adult')

# Example 3: Apply lambda with multiple columns using axis=1
# Create a custom description
df['Description'] = df.apply(lambda row: f"{row['Name']} is {row['Age']} years old and earns {row['Salary']}", axis=1)

print(df)
'''
      Name  ...                              Description
0    Alice  ...    Alice is 25 years old and earns 50000
1      Bob  ...      Bob is 32 years old and earns 60000
2  Charlie  ...  Charlie is 18 years old and earns 30000
3    David  ...    David is 47 years old and earns 80000

[4 rows x 6 columns]'''

d=pd.DataFrame([{
    "Name":[20,4,18,4,8,25],
    "Group":['Major','Minor','Major','Minor','Minor','Major']
}])
f=pd.DataFrame([{
    'Class':['B.tech','pri_School','B.tech','Pri_School','Pri_School','M.tech']

}])
print(f)
#now im merging both data sets into one
print(pd.concat([d,f]))


