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
secure_token on:2026-06-09 15:35:52.016518+00:00
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