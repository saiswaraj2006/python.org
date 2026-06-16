#A module in python is a file that contains python code-it can define functions, classes, and variables.
#or
#A Module is a .py file that groups related code together
#it has built-in Modules like math,os,random etc..
#example i performed "Invitation.py" file by importing it into "RE_Invitation.py"
'''
in this i declared a function that returns the invitation to my friend 
in "Invitation.py then imported that file to "RE_Invitation.py then printed
'''
#above one is the example of the modules
#here different types of modules in the python
'''
1. Built-in Modules
ex:math, os ,sys ,random, datetime.

2.User-Defined Modules
ex: like recently created "eventmanager" with packages like guestlist.py,invitation.py, remainder.py.

3.External Modules
ex:numpy, pandas , flask.
'''
#1.Built-in Modules
from math import pi
print(pi)
#output=3.141592653589793
from math import sqrt as square_root
print(square_root(576))
#output=24.0

from math import pow as power
print(power(5,2))#returns:25.0
print(power(23,3))#returns:12167.0

#3.external modules
import pandas as pd
#df = pd.DataFrame({"Name": ["Soumya", "Priya"], "Event": ["Marriage", "Marriage"]})
#print(df)
#it returns 
'''  Name     Event
0  Soumya  Marriage
1   Priya  Marriage
'''
#from PIL import Image
#img = Image.open("photo1.jpeg")
#img = img.resize((200, 200))
#img.save("small_photo.jpeg")

#runs tasks automatically
#import schedule
#import time
#count=0
#def remainder():
    #global count#i declared count as global 
    
    #print("please wake up!")
   # count+=1
  #  if count>=2:
#the code exits the loop after 2 prints
 #       exit()
#schedule.every(5).seconds.do(remainder)

#while True:
    #schedule.run_pending()
    #time.sleep(1)
#for fetching the data  from the websites 
#im importing requests
import requests
#from bs4 import BeautifulSoup
#response=requests.get("https://www.readthetale.com")
#print("status:",response.status_code)
#print("First 100 chars:",response.text[:100])
#soup=BeautifulSoup(response.text,"html.parser")
#print("page title:",soup.title.text)#it gets the title 
#print("page text:",soup.get_text()[:400])
#above line prints the first 400 chars

#Pandas
#import pandas as pd
#data={"NAME":["Sai","Shiva","Swaroop"],"EVENT":["Marriage","Birthday","House Warming Ceremony"]}
#df=pd.DataFrame(data)
#print(pd)
 #above line prints the pandas module obj
#print(df["NAME"])
#print(df["EVENT"])#it prints the  EVENT column 
#print(df.head(1))#prints the first row
#print("_______________")
#print(df.head(2))
#print("_______________")
#print(df.head(3))
#output=
'''
0        Sai
1      Shiva
2    Swaroop
Name: NAME, dtype: str
0                  Marriage
1                  Birthday
2    House Warming Ceremony
Name: EVENT, dtype: str
  NAME     EVENT
0  Sai  Marriage
_______________
    NAME     EVENT
0    Sai  Marriage
1  Shiva  Birthday
_______________
      NAME                   EVENT
0      Sai                Marriage
1    Shiva                Birthday
2  Swaroop  House Warming Ceremony
'''
#birthday_guest=df[df["EVENT"]=="Birthday"]
#print(birthday_guest)
#it filters and prints where the EVENT ="Birthday"

#output=  
# NAME     EVENT
#1  Shiva  Birthday

import pandas as pd
df=pd.DataFrame({"lang_Name":["Dutch","French",],"origin_place":["West_Germanic","France"]})
print(df)
print(df.columns)
print(df.shape)#it prints tuple of (rows,columns)
#output=(2,2)
new_df=df.assign(hook=["u","y"])
print(new_df)
#it prints new column
print(df.head(3))#it prints first 3 rows
print(df.tail(1))#it prints last row
#for sorting alphabetically
print("After sorting\n",df.sort_values("lang_Name"))
#above the output is same because it was already in alphabetical form
df["Name_length"]=df["lang_Name"].apply(len)
print(df)
#above line prints the length of the lang_name column
#if i need the length of the origin_place
#then
df["origin_place_length"]=df["origin_place"].apply(len)
print(df)

#DYNAMIC IMPORTS
#dynamic imports means we load the modules at the runtime, not at the top
#of the file
#we don't know which module will need until the program runs.
#Example problem 
#creating a string
module_name="math"#it is string 
math_module=__import__(module_name)
print(math_module.sqrt(16))
print(math_module.pow(16,2))#importing the math_module then runs

#using the importlib
import importlib
module_name="random"
random_module=importlib.import_module(module_name)
print(random_module.randint(1,10))
#randint(1,10) is the function starts from1 to 10 then it prints randomly one integer from that limit

#for exact date and time
import datetime
print(datetime.datetime.now())
#it prints the exact date and time with milliseconds 
from math import *
print(square_root(4))
print(factorial(7))
def fact_total():
    a=factorial(3)#3 factorial=6
    b=factorial(4)#4 factorial=24
    return a+b #it returns the total of a and b
print(fact_total())

#SET MATRIX ZERO PROBLEM
'''
Approach= first create a matrix, then track which rows and columns are zeroes in the matrix 
through loop once after finding all original 0's.
Loop through the matrix again to change those  entire rows and columns to 0.
'''
#def setZeroes(matrix):
#    #to get the size of the matrix
#    num_rows=len(matrix)
#    num_cols=len(matrix[0])
#    zero_rows=[]
#    zero_cols=[]
#    for r in range(num_rows):
#        for c in range(num_cols):
#            if matrix[r][c]==0:
#                zero_rows.append(r)
#                zero_cols.append(c)
#    #for turning rows and columns into zeroes
#    for r in range(num_rows):
#       for c in range(num_cols):
#            if r in zero_rows or c in zero_cols:
#                matrix[r][c]=0
#my_matrix=[[1,1,1],[1,0,1],[1,1,1]]
#setZeroes(my_matrix)
#print(my_matrix)
#output=[[1, 0, 1], [0, 0, 0], [1, 0, 1]]
#using built in function 
import keyword
#for checking the given string is a special keyword in python or not
#print(keyword.iskeyword("if"))#True
#print(keyword.iskeyword("is"))#True
#print(keyword.iskeyword("apple"))#False
#above one returns False because given string is not keyword in the python

#For counting how many times item appear in a list
#so importing the collections counter
from collections import Counter
#items=["apple","banana","apple","kiwi","kiwi","apple","grapes","mango","mango","papaya","orange","grapes","grapes"]
#for counting all the items automatically
#no_of_fruits=Counter(items)
#print(no_of_fruits)
'''output=Counter({'apple': 3, 'grapes': 3, 'kiwi': 2, 'mango': 2, 'banana': 1, 'papaya': 1, 'orange': 1})
'''
#for statistics solving the mean ,median ,mode for weighted graphs by using the 
#built in module name called statistics
import statistics
Std_Marks=[99,45,88,85,76,59,67]
#for calculating average of Std_Marks(mean)
#print(statistics.mean(Std_Marks))
#output=74.14285714285714
#for finding the most common grade(mode)
#print(statistics.mode(Std_Marks))
#output=99
#print(statistics.median(Std_Marks))
#output=76

#for finding the performance and machine of my laptop
import platform
#print(platform.system())
#Windows
#print(platform.processor())

from collections import defaultdict
#it tells python to automatically create an empty list[] for any new key

student_grades=defaultdict(list)
#now i can append grades immediately without checking if the name exists first
student_grades["Aravind"].append(94)
student_grades["Anuv"].append(95)
student_grades["chandu"].append(76)
print(f"{student_grades}:")
#output=defaultdict(<class 'list'>, {'Aravind': [94], 'Anuv': [95], 'chandu': [76]}):
#or
print(dict(student_grades))
#output={'Aravind': [94], 'Anuv': [95], 'chandu': [76]}


