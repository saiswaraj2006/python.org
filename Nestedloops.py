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



