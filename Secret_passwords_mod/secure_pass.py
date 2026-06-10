import secrets
import datetime
secure_token=secrets.token_urlsafe(30)
current_datetime=datetime.datetime.now(datetime.timezone.utc)
print(f"secure_token on:{current_datetime}")
print(f"reset link token:{secure_token}")
#it generates a secure, random web token for a url reset link
#reset link token:HUBFFCp3v5puEhxLOK1x8ZqM8dorcXB_6wAsF8Q3
#output=
'''
secure_token on:2026-06-09 15:42:52.016518+00:00
reset link token:As8DmCZtIcdCgtc5503pAFQjA0riyNVBUTbGGaYn
'''
#every time the user try to run it gets random web reset url link
expiry_time=current_datetime+datetime.timedelta(minutes=2)
print(f"Token Expires:{expiry_time.strftime('%D-%m-%y %H:%M:%S')}")
'''it prints the expiry time after 2 minutes 
format of time and date=first 'date-month-year' ,then time in hours:minutes:seconds
Here timedelta() is used for add or subtract time from a date or time object  
it represents the time duration 
'''
#output=
'''
secure_token on:2026-06-09 15:46:58.436812+00:00
reset link token:XI9CeuIWQYspZhZkct4K_G7gmzKg68Viln2bO0Zk
Token Expires:06/09/26-06-26 15:48:58
'''
from collections import deque
#deque=Double-Ended-Queue
#A CONTAINER like list optimized for fast appends and pops from both ends.
q=deque([1,2,3])
q.append(4)
#it adds to right side of the list
q.popleft()#it deletes the left side one which means 1
print(q)#it prints the remaining list
#output=deque([2, 3, 4])
#stack implementation
#stack uses LIFO principle
s=deque()
s.append('A')
s.append('B')
s.pop()#it deletes the last one means stack LIFO principle
print(s)#it prints remaining stack 
#output=deque(['A])
#FOR ROTATING THE POSITIVE VALUES USES .rotate()
from collections import deque
e=deque([1,2,3,4])
e.rotate(2)
print(e)
#means it shifts all positive values to 2 step right side
#so the output is 
#deque([3, 4, 1, 2])
#if im use same with negative values then it rotate to left side
#Example
from collections import deque
de=deque([-1,-2,-3,-4])
de.rotate(2)
print(de)
#here this values are Negative so, it shifts the 2 positions to left side
#so the output =
#deque([-3, -4, -1, -2])
#or
re=deque([1,2,3,4])
re.rotate(-2)
print(re)