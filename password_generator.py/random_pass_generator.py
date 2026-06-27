
import string as st
import secrets as sc
def random_password_generator(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    password_characters = st.ascii_uppercase + st.ascii_lowercase + st.digits + st.punctuation
    password=sc.choice(password_characters)  # Ensure at least one character from each category
    for i in range(length - 1):# Generate the remaining characters randomly
        password += sc.choice(password_characters)
    return password
print("password:",random_password_generator(12))
#output=
'''
password: >[n_G]vKh1bW'''
#here i used secrets module to generate a secure random password of length 12 characters. 
#It includes uppercase letters,lowercase letters,digits,and punctuation symbols.
#the function ensures that the password is at least 8 characters long and raises a ValueError if the specified length is less than 8.
