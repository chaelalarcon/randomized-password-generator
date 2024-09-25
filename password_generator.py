import random
import string

def password_gen (length = 12):
    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation
    for i in range (length): 
        password += random.choice (chars)
    return password

print ('Your password is: ', password_gen ()) 