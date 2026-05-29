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
df = pd.DataFrame({"Name": ["Soumya", "Priya"], "Event": ["Marriage", "Marriage"]})
print(df)
#it returns 
'''  Name     Event
0  Soumya  Marriage
1   Priya  Marriage
'''
from PIL import Image
img = Image.open("photo1.jpeg")
img = img.resize((200, 200))
img.save("small_photo.jpeg")

#runs tasks automatically
import schedule
import time
count=0
def remainder():
    global count#i declared count as global 
    
    print("please wake up!")
    count+=1
    if count>=2:
#the code exits the loop after 2 prints
        exit()
schedule.every(5).seconds.do(remainder)

while True:
    schedule.run_pending()
    time.sleep(1)
#without using the schedule module


import time
count=0
while count<2:
    print("Please Wake Up!")
    count+=1
    time.sleep(5)

    
