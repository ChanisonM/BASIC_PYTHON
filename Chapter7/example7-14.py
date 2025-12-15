import random 

nums = []
for i in range(0 , 11):
    n = random.randint(1 , 100)
    print(f'index : {i} value : {n}')
    nums.append(n)

print(f"จำนวนทั้งหมดในลิสต์ {nums}" )
print(f'Sumary : {sum(nums)}')
print(f'Maxinum : {max(nums)}')
print(f'Minium : {min(nums)}')