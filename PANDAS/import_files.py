import pandas as pd
#means in importing the csv_files and dealing with that data
#by using 
#pd.read_csv("file path/file name")
#data=pd.read_csv()
#creating a data
Employees=pd.DataFrame({
    'EmployeeID':[101,102,103,104,105,106,107,108,109,110],
    'Name': [
        "Aarav",
        "Priya",
        "Rohan",
        "Meera",
        "Vikram",
        "Sneha",
        "Arjun",
        "Kavya",
        "Rahul",
        "Ananya"
    ],
    "Gender":["Male","Female","Male","Female","Male","Female","Male","Female","Male","Female"],
    "Age": [26, 31, 28, 36, 29, 40, 33, 27, 32, 25],
    "Department": [
        "HR",'IT','Finance','Marketing','IT','HR','Finance','Marketing','IT','HR'],
    "salary":[45000,65000,55000,70000,62000,75000,68000,52000,66000,48000],
    "PerformanceRating":[4.5, 4.8, 4.2, 4.9, 4.4, 4.9,3.5,4.2,3.5,4.0]


})
print(Employees)
Employees.to_csv("Employees.csv",index=False)#index=false used because
#prevents pandas from writing row numbers to the file.
print("file saved successfully!")
#now i saved that above data into "Employees.csv" 
data=pd.read_csv("Employees.csv")
print("read successfull")
print(data.head())
#the head()  is used to read my first 5 rows of my data
print(data.tail())
#the tail() is used to read my last 5 rows 
print(data.shape)
#(10, 7)
#which means 10-rows and 7-col
print(data.size)
#70
#size->means no of elements in the data
print(data.iloc[::2])
print(data.info())