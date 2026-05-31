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
print(df.tail(1))