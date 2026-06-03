import random
total_sum=0
print("rolling the cube 6 times.")

for i in range(1,7):
    roll=random.randint(1,6)
    total_sum+=roll
    #above im adding roll to total_sum each time the program runs upto 6 times
    print(f"Roll {i}: you got a {roll}")
print(f"Total sum of all 6 rolls:{total_sum} ")
#output=
'''
rolling the cube 6 times.
Roll 1: you got a 1
Roll 2: you got a 4
Roll 3: you got a 4
Roll 4: you got a 5
Roll 5: you got a 4
Roll 6: you got a 5
Total sum of all 6 rolls:23 
'''
print("end")
   