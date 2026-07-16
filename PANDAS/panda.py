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
print(df)
#now i need the students who got 8.5 above
print(df['Gpa_Marks']>=8.5)
'''
0     True
1     True
2     True
3    False
4    False
5     True
Name: Gpa_Marks, dtype: bool
'''
print(df.iloc[::2])
'''
     Name Course     Fee  Gpa_Marks  Discount_Fee   City
0    Arun     AI  150000       10.0      135000.0    HYD
2  Swathi     DS  120000        9.9      108000.0  DELHI
4  Shreya     AI  150000        7.5      135000.0    HYD
'''
df["Name"]=df["Name"].replace("Arun","Ajay")
print(df)