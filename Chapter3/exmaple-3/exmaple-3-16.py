import random

chars = '0123456789'
chars += 'abcdefghijklmnopqrstuvwxyz'
chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

a = random.choice(chars)
b = random.choice(chars)
c = random.choice(chars)
d = random.choice(chars)
e = random.choice(chars)

password = a + b + c + d + e 
print(f'Password : {password}')