# Random Password A-Z , a-z , 0-9
# step 1
import random 
A_Z = range(ord('A') , ord('Z') + 1)
a_z = range(ord('a') , ord('z') + 1)

uppercase_letters = ''
for i in A_Z :
    uppercase_letters += chr(i)
    # print(uppercase_letters)

lowercase_letters = ''
for i in a_z :
    lowercase_letters += chr(i)
    # print(lowercase_letters)

digits = ''
for d in range(0 ,10):
    digits += str(d)
    # print(digits)

password_chars = uppercase_letters + lowercase_letters + digits
pswd = ''
for c in range(6) :
    pswd += random.choice(password_chars)    
    print(pswd)

print(f'Password is {pswd}')