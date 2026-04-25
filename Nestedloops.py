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
    




