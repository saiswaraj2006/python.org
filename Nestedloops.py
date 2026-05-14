'''nested loop→A loop within the loop here, The inner loop runs completely for each iteration of the outer loop.
for printing the basic pattern like
* 
 *
  *
  '''
  #first i need to check the rows and coloums of the pattern and checking the spaces also
  #     j=1 j=2 j=3
'''i=1*
     i=2    *
     i=3        *
     so here if i=1 ,j=1 then we have a *
     same has 2 and 3 so i take the condition as if i==j then print *
     '''
for i in range(3):
    for j in range(3):
        if i==j:
            print("*",end='')
        else:
            print(' ',end='')
    print()#it prints the new line after the successful runs of the one iteration 
    '''
            *
        *
    *
for printing the reverse pattern here i check when the '*' is the 
   j=1 j=2 j=3
i=1        *
i=2    *
i=3*        
so when i=1 and j=3 then '*'
and when i=2 and j=2 
and at last i=3 and j=1
'''
print()
n=3
for i in range(n):
    for j in range(n):
        if i+j==n-1:#we need to start print from reverse so where the row index+ column index =n-1(3-1)
            print('*',end='')
        else:
            print(' ',end='')
    print()
#for printing the below pattern
'''
 *****
 *   *
 *   *
 *   *
 *****
 '''
#so to print the above pattern we need to print the without gapped rows which are 1,5
#and then printing the columns and gaps
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:#it prints weather any one of those condition is true i refers to rows and j returns to the columns
            print('*',end='')
        else:
            print(' ',end='')
    print()
#or in other way
print()#to give space
n=5
print('*'*n)
for i in range(n-2):#is number of middle rows 
    print('*'+' '*(n-2)+'*')#here in the middle (n-2) rows are printing with spaces
print('*'*n)
#SCHOOL TIMETABLE
#Each school day has multiple periods
days=['Monday','Tuesday','Wednesday']
periods=['Mathematics','Physics','Chemistry']
for day in days:
    for period in periods:
        print(f"{day}: {period}")
'''
output=Monday: Physics
Monday: Chemistry
Tuesday: Mathematics
Tuesday: Physics
Tuesday: Chemistry
Wednesday: Mathematics
Wednesday: Physics
Wednesday: Chemistry
'''
#for example if i have a holiday at the Wednesday then
print()
for day in days:
    if day=='Wednesday':
        print(f"{day}: Holiday")
        continue
    for period in periods:
        print(f"{day}: {period}")
'''
Monday: Mathematics
Monday: Physics
Monday: Chemistry
Tuesday: Mathematics
Tuesday: Physics
Tuesday: Chemistry
Wednesday: Holiday→→(here it prints  holiday so school is leave)
'''
size = 8

for r in range(size):
    for c in range(size):
        if (r+c) % 2 == 0:
            print("⬛", end=" ")
        else:
            print("⬜", end=" ")
    print()
print()

rows = 7
cols = 20

# Define coordinates for each letter
S_coords = {(0,1),(0,2),(0,3),(1,1),(2,1),(3,1),(3,2),(3,3),(4,3),(5,3),(6,1),(6,2),(6,3)}
A_coords = {(0,6),(0,7),(0,8),(1,6),(1,8),(2,6),(2,7),(2,8),(3,6),(3,8),(4,6),(4,8),(5,6),(5,8),(6,6),(6,8)}
I_coords = {(0,11),(0,12),(0,13),(1,12),(2,12),(3,12),(4,12),(5,12),(6,11),(6,12),(6,13)}

for r in range(rows):
    for c in range(cols):
        if (r,c) in S_coords or (r,c) in A_coords or (r,c) in I_coords:
            print("⬜", end=" ")
        else:
            print("⬛", end=" ")
    print()
'''i just created 'sai' by using the coordinates,the output is crazy
⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬜ ⬛ ⬛ ⬛ ⬛ ⬜ ⬛ ⬜ ⬛ ⬛ ⬛ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬜ ⬛ ⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬜ ⬛ ⬜ ⬛ ⬛ ⬛ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬛ ⬛ ⬜ ⬛ ⬜ ⬛ ⬛ ⬛ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬛ ⬛ ⬜ ⬛ ⬜ ⬛ ⬛ ⬛ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬜ ⬛ ⬜ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
'''
#it prints white block in the mentioned coordinates other wise black so 
#then after successful iteration till last coordinate it gives the above output

#For printing the months in a year i also use the nested loop
months=['January','February','March','April','May','June','July','August','September','October','November','December']
#numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
#for no,month in zip(numbers,months):
    #if month=='April'and no==4:
        #print(f"{no}: {month}: (current month)")
    #else:
        #print(f"{no}: {month}")
    #so above firstly used normal outer loop and inner loop i get stuck then i use for pairs zip() function
    # then i get the answer perfectly
'''for printing below pattern
******
*    *
*    *
*    *
******
''' 
#for normal outlined box
#To print the horizontal * 
n=6
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
#now i need to print '$' symbol inside the box but in the diagonal top-left to down-right
#so here i observe that the if both diagonals 0,0 and 1,1, and 2,2 and 3,3 and 4,4 is equal then it has '$' symbol
#but here im taking n=5
#then 
n=5
for i in range(n):
    for j in range(n):
        if i==j:
            print('$',end='') #for diagonal condition when i==j then prints the '$'
        elif i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    '''
$****
*$  *
* $ *
*  $*
****$
    '''
#now i need two diagonals one is left to right and one is reverse
print()
n=5
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:#here i use both diagonal and reverse diagonal 
            print('$',end='')
        elif i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
print()
    #to print the following pattern
'''
    0
    12
    345
    6789
    '''
count=0
for t in range(1,5):
    print()
    for u in range(1,t+1):
        print(n,end=' ')
        count=count+1
#to print the below pattern
'''
     1
    12
   123
  1234
 12345
'''
print()
n=5
for i in range(1,n+1):
    for k in range(n,i,-1):
        #to print in reverse order using slicing
        print(" ",end='')
    for j in range(1,i+1):
        print(j,end='')
    print()
#here i used reverse printing condition when there is pattern starts in reverse so i use another 
#loop to iterate from n to 0
#then the loop starts with n
#stops at index o 
#steps -1
#means starts with nth and ends with starting position
#write a program to implement the following sequence of numbers.
'''
1. 1,8,27,64,.....
2. -5,-2,0,3,6,9,12,....
3. -2,-4,-6,-8,-12.....
4. 1,4,7,10,.....
'''
print()
for i in range(1,6):
    print(i**3,end=',' if i<5 else ",...")#if i add the comma in the end block then it prints , at the end also so i use condition
    #if i<5 then prints the ,....
    
print()
#for 2. sequence

for l in range(-5,16,3):
    if l==-2:
        print(l,end=",")
        
    elif l>0:
        print(l-1,end="," if l-1<12 else",....")
    else:
        print(l,end="," )

#output=-5,-2,0,3,6,9,12,....
#for 3rd sequence 
#-2,-4,-6,-10,-12,...
#here it is starts with the -2 and ends upto -12
print()
for i in range(-2,-13,-2):
    print(i,end="," if i>-12 else",...")
#for printing the 1,4,7,10
#here it starts with the 1 and ends upto the value 10 and so on ,...

#so by using the for loop start,stop,step condition i able to print the sequence
print()#for new line because it will print from the end of the above output
for i in range(1,11,3):
    print(i,end=',' if i<9 else",....")
#some crazy work
print()
a=30
if a==30:
    a=60
if a==60:
    a=90
c=0
c=+a
print(a+78)
c=a+78
g='g'+str(c)+"ood"#here if i want to add the c value then it is integer so i used str(c) this converts the c value to string so then concatenates with g
print(g)
print("\n g is:",g)
#so tomorrow i can prepare for the new concept is file handling 
#File is a collection of data stored on a secondary storage device like hard disk.
#we have ASCII files and Binary files and opening and closing file
#For opening file 
#we use
#fileobj=open(file_name[, access_mode])
file=open("File.txt","rb")
print(file)
#<_io.BufferedReader name='File.txt'>
#we have accessing the modes
#r=This is the default mode of opening file which opens the file for reading only
#rb= This mode opens a file for reading only in binary format.The file pointer  is placed at the beginning of the file
#r+=This mode opens a file for  both reading and writing .This file pointer at the beginning of the file
#rb+=This mode opens the file for both reding and writing in binary format.The file is placed at the beginning of the file
#w=this mode is used only for writing 
#wb=opens a file in binary format for writing only.In this mode two things can happens when file is does not exist,a new file 
#is created for writing .if the file is already existed and has some data stored in it,the contents are over written
file=open("File.txt")
print("the file name is:",file.name)
print("File is closed:",file.closed)
print("File has been opened in:",file.mode,"mode")#it returns the mode has 'r' which means read mode

f=open("File.txt","r")
file=open("File.txt","w")
'''
THE close() METHOD
'''
#using close method by
#fileobj.close()
'''
'ab' is used to appending the binary file .The pointer is at end of the file exists.If the file does not exist it creates a new file
for writing 

'a+' is  used to open a file for both reading and the appending . The file pointer is placed at the end of the file if the file exists.
If the file does not exist then it creates a new file

'ab+' is used to open a file in binary format for both reading and appending. The file pointer is placed at the end of the file if hte file exists.
If it does not exist, a new file is created for reding and writing.'''
#example
f=open("File.txt","a+")
f.write("Adding python 'File Handling' concept in the nested loops.py file \n")
f.close()
print("successfully added the content")

with open("File.txt", "a") as f:
    f.write("Adding python 'File Handling' concept in the nested loops.py file \n")

print("Successfully added the content")

with open("File.txt","+r") as f:
    print("open file is \n",f.read())

with open("File.txt","+r") as f:
    for line in f:
        print("line is\n",line.strip())#this line.strip () is removes the spaces at beginning and ending of the line

with open("File.txt","w") as f:
    f.write("third line is added by using 'w' mode\n")#this overwrites the entire file and removes the existing files
#for splitting the words in the certain text file
#using the .split() method for splitting 
with open("File.txt","r") as f:
    line=f.readline()
    wp=line.split()
    print("wp:",wp)
#wp: ['third', 'line', 'is', 'added', 'by', 'using', "'w'", 'mode']
#now im adding the another line in the existing file
with open("File.txt","+a") as f:
    f.write("this text file is created by the owner for studying purpose\n")
    print("successfully added the content in the text file")

#again splitting and updated text file 
with open("File.txt","r") as f:
    content=f.read()#used to read entire file as the one string
    
    words=content.split()
    print("words_after_splitting:",words)
#output=words_after_splitting: ['third', 'line', 'is', 'added', 'by', 'using', "'w'", 'mode', 'this', 'text', 'file', 'is', 'created', 'by', 'the', 'owner', 'for', 'studying', 'purpose']
#for printing each line separately
with open("File.txt","r") as f:
    content=f.readlines()
    for line in content:
        word=line.split()
        print("words:",word)
#output=words: ['this', 'text', 'file', 'is', 'created', 'by', 'the', 'owner', 'for', 'studying', 'purpose']
#program to display all content in the file 
#for that we use read() method
file=open("File.txt","r")
for line in file:
    print(line)
file.close()
''' output is:
third line is added by using 'w' mode

this text file is created by the owner for studying purpose
'''
#fileno()=used to return the file number of the file(which is an integer descriptor)
#flush()=This method is used to flushes the write buffer of the stream
#isatty()=Returns True if the file stream is interactive and False otherwise
#readline(n)=Reads and returns one line from the file .if n is specified then almost n bytes are read
#truncate()=Resizes the file to n bytes
# rstrip()=Strips off whitespaces including newline characters from the right side of the string  
file=open("File.txt","w")
print(file.fileno()) 
#3
feee=open("File.txt","w")
print(feee.flush())
#for knowing if my program is interactively running on the terminal or not
#if it runs then it returns 'True' and otherwise 'False'
file=open("File.txt","w")
print(file.isatty())#it returns 'False' because file is the regular file in the disk not in the terminal
#Reading a file in chunks of 27 characters per line
#for calculating the vowels and consonants in the particular file by every character 
#filename=input("Enter the file name:")
#with open(filename) as file:
    #text=file.read()
    #count_vowels=0
    #count_consonants=0
    #for i in text:
        #if i in "aeiou" or i in "AEIOU":
            #count_vowels+=1
        #else:
            #count_consonants+=1
#print("Number of vowels:",count_vowels)
#print("Number of the consonants:",count_consonants)
#for printing the length of the file
#print("Length of the file is=",len(text))
#i use another method for length of the file 
#by adding the "count_vowels"+"count_consonants"=length of the file
#print("length of the file:",count_vowels+count_consonants)
'''
output=Enter the file name:Nestedloops.py
Number of vowels: 3085
Number of the consonants: 11240
Length of the file is= 14325
length of the file: 14325
'''
#for calculating the percentage of vowels presented in the file and also calculating the consonants presented in the file
#print("Percentage of the vowels in the file:",((count_vowels*100)/len(text)))
#the output is=Percentage of the vowels in the file: 21.535776614310645
#now for consonants in the same file
#print("Percentage of the consonants in the file:",((count_consonants*100)/len(text)))
#output=Percentage of the consonants in the file: 78.46422338568935
#so here my "Nestedloops.py" file has very high amount of consonants
#*NOTE=for calculating each character in the provided file
#Write a program that counts the number of tabs ,spaces, and newline characters in a file
#filename=input("Enter the name of the file:")
#with open(filename) as file:
    #text=file.read()
    #count_tabs=0
    #count_spaces=0
    #count_new_line=0
    #for char in text:
        #if char=='\t':
            #count_tabs+=1
        #if char==' ':
            #count_spaces+=1
        #if char=='\n':
            #count_new_line+=1
#print("TABS=",count_tabs)
#print("Spaces:",count_spaces)
#print("NEW LINE:",count_new_line)
'''
Enter the name of the file:UNIT_1.py
TABS= 0
Spaces: 4930
NEW LINE: 1090
'''
#WRITE A PROGRAM TO READ A FILE LINE BY LINE .EACH LINE READ FROM THE FILE IS COPIED TO ANOTHER FILE WITH LINE NUMBERS SPECIFIED AT 
#THE BEGINNING OF THE LINE
file1=open("File.txt","r")
file2=open("new.txt","w")
num=1
for line in file1:
    file2.write(str(num)+" : "+line)
    num=num+1
file1.close()
file2.close()
#write a program that copies first 10 bytes of a binary file into another
with open("File.txt","rb") as file1:#using rb for reading only in the binary file format and pointer 

    with open("new.txt","wb") as file2:
        buff=file1.read(10)
        file2.write(buff)
print("file is copied")
print(buff)

with open("File.txt","rb") as f1, open("new.txt","rb") as f2:
    original = f1.read(10)
    copied = f2.read()

    print("Original File (first 10 bytes):", original)
    print("Copied File (new.txt):", copied)
#output=Original File (first 10 bytes): b''
#Copied File (new.txt): b''
#so here my file is empty so the buffered pointer is empty to copy 10 bytes 
#now im adding the data in the file
with open("File.txt","wb") as f:
    f.write(b"abcdefghijklmnopqrstuvwxyz")
print("successfully completed")
#now my file has some data then i can copy upto 10 bytes and print
with open("File.txt","rb") as f1:
    with open("new.txt","wb") as f2:
        buffff=f1.read(10)
        f2.write(buffff)
print(buffff)#b'abcdefghij'
with open("File.txt","rb") as f1, open("new.txt","rb") as f2:
    print("Original File (first 20 bytes):", f1.read())
    print("Copied File (new.txt):", f2.read())
#the output=Original File (first 20 bytes): b'abcdefghijklmnopqrstuvwxyz'
#Copied File (new.txt): b'abcdefghij'
#i have a text file named as ''war.txt''
#now to delete this file firstly im adding the content in the file
with open("war.txt","w+") as file:
    file.write("text is ssss but this file is created to add some text and then delete the file")
#now for delete the whole file from my system im using os.remove() method
#importing the os
#import os
#os.remove("war.txt")
#print("successfully deleted the file")
#print(war.txt) output=NameError: name 'war' is not defined because the file is removed from my os 

#RENAME the file
#firstly adding the text in the my new file
#with open("cap.txt","w+") as file:
#    file.write("the name of file is cap.txt ")
#print("written successfully")
#RENAMING THE "cap.txt" file to "cap2.txt"
#import os
#os.rename("cap.txt","cap5.txt")
#print("\n Your File is renamed as 'cap5.txt'")
#directory methods
'''
the directory is a collection of files where each file may be of a different format, python has various modules that help programmers to work
with directories .These methods allow users to create ,remove, and change directories'''

#using os.mkdir("new_dir_name")
#import os

# Get current working directory
#print(os.getcwd())
#list the files in the directory
#print(os.listdir("C:/Users/saisw/OneDrive/Desktop/python_practice"))
#it returns in list format like
#['.git', 'Nestedloops.py', 'cap4.txt', ]

#creating new directory
#os.mkdir("pythonnexttopics")
#it creates a new directory 
import pathlib
#for using in cleaner path using 
#A path is a class from python's  pathlib module
#from pathlib import Path
#path("C:/Users/saisw/OneDrive/Desktop/python_practice>").mkdir(pythonnexttopics==True,exist_ok=True)
#it returns "FileExistError"
#already exists:"pythonnexttopics"
#creating and writing files 
#using open() or Path.write_text()
from pathlib import Path
file=Path("c:/Users/saisw/OneDrive/Desktop/python_practice/pythonnexttopics/summary.txt")
file.write_text("My new directory was created to perform all types of operations here")
print(file.read_text())
#it prints 
#My new directory was created to perform all types of operations here
#APPENDING DATA
with open(file,"a") as f:
    f.write("\n Adding the notes by using the appending 'a' .")
    #it adds the text in the above file
    
import os
print(os.path.getsize(file))#it returns the no of bytes of data the file is used

#to check the file absolute path using Path.resolve()
from pathlib import Path
p=Path("Users/saisw/OneDrive/Desktop/python_practice/cap1.txt")
print(p.resolve())
#for checking is the path is exist im using .exists()
print("path is exist:",p.exists())

#using teh os.stat(file) for retrieving a full set of metadata about the file (size,timestamps, permissions , etc)
#stat.st_size=gives the file size in bytes
import os
import time

file = "cap1.txt"
stats = os.stat(file)

print("Size:", stats.st_size, "bytes")
print("Created:", time.ctime(stats.st_ctime))
print("Modified:", time.ctime(stats.st_mtime))
print("Last accessed:", time.ctime(stats.st_atime))
#Size: 0 bytes
#Created: Fri May  8 23:17:57 2026
#Modified: Fri May  8 23:17:57 2026
#Last accessed: Fri May  8 23:17:57 2026
'''write a program that generates a quiz and uses two files-- Questions.txt and Answers.txt. The program opens Questions.txt and reads a questions and displays the 
questions with options on the screen . The program then opens the Answer.txt file and displays the correct answers
'''
#first im creating both files of the both .txt files
with open("Questions.txt","w+") as file1:
    file1.write("Q1.print(type({}))" )
    file1.write("\n A.<class'list'> \n B.<class'dict'>\n C.<class'set'>\n D.Error")
    file1.write("\n Q2.Which of the following is used to create a tuple in python?")
    file1.write("\n A.[] \n B.{} \n C.() \n D.<> ")
    
print("successfully file1 is created")
print()
with open("Answers.txt","w+") as file2:
    file2.write("Answers")
    file2.write("\n1-B) print(type({}))'")
    file2.write("\n2-C) ()")
print("successfully file is created")
#after creating now im opening first "Questions.txt" then "Answers.txt" file
file1=open("Questions.txt","+r")
file2=open("Answers.txt","+r")
q=file1.read()
qlines=q.split('\n')
for lines in qlines:
    print(lines)
qq=file2.read()
qlines=qq.split('\n')

for lines in qlines:
    print(lines)
#my output is
'''
successfully file1 is created

successfully file is created
Q1.print(type({}))
 A.<class'list'> 
 B.<class'dict'>
 C.<class'set'>
 D.Error
 Q2.Which of the following is used to create a tuple in python?
 A.[] 
 B.{} 
 C.() 
 D.<> 
Answers
1-B) print(type({}))'
2-C) ()
'''
print()

#to copy a file using shutil module
#by using the shutil.move() function,we can move a file
#first importing the shutil
import shutil
#shutil.move("cap5.txt","cap55.txt")
#after execution it rename as cap55.txt
import os
import datetime

#  to Get file stats
stats = os.stat("basics.txt")

# Convert timestamps to readable format
created = datetime.datetime.fromtimestamp(stats.st_ctime)
modified = datetime.datetime.fromtimestamp(stats.st_mtime)
accessed = datetime.datetime.fromtimestamp(stats.st_atime)

print("Created:", created)
print("Modified:", modified)
print("Accessed:", accessed)
#it returns file created , modified, accessed time and the date 
#seek() concept

#the file.seek(,) is a method is used to move the file pointer 
#in this method it has offset-used for how many bytes to move
#whence=the reference point from which the offset is applied
#the whence has 0 means from the beginning of the file
#1 means from the current file position 
#2 means from the end of the file
#file.seek(20,1) means 20 for moving 20 bytes
#1 is to relative to the current position
with open("alphabets.txt","w") as file:
    file.write("abcdefghijklmnopqrstuvwxyz")


with open("alphabets.txt","rb") as file:
    before_seek=file.read(5)#before seek method
    print(before_seek)
    file.seek(5)                # move pointer to the 6th byte (index 5)
    data = file.read(5)         # read 5 bytes from there
    print(data)




