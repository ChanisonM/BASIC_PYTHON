# Random Password A-Z , a-z , 0-9
# step 2

import random
pswd = ''
for c in range(6) :
    g = random.randint(1,3) 
    print(g)
    if g == 1 :
        start , end = 'A' , 'Z'
    elif g == 2 :
        start  , end = 'a' , 'z'
    elif g == 3 :
        start ,  end = '0' , '9'

    x = random.randint(ord(start) , ord(end)) # ord() แปลงจากตัวอักขร เป็น รหัส ASCII (หรือ Unicode)
    pswd += chr(x) # chr() แปลงจาก รหัส ASCII (หรือ Unicode) เป็นตัวอักขร

print(f'password is {pswd}')