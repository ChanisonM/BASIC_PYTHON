n1 = int(input("Number 1 : "))
print(f'>> {n1}')
min = n1 

n2 = int(input("Number 2 : "))
print(f'>> {n2}')
if n2 < min :
    min = n2

n3 = int(input("Number 3 : "))
print(f'>> {n3}')
if n3 < min :
    min = n3

print(f"Mininum : {min}")