import math

pi = math.pi
print(f'{pi:.2f}')

number_1 = 12345
print(f'{number_1:,}')

number_2 = 123
print(f'{number_2:0>6}')

number_3 = 12
print(f'{number_3:0<9}')

dt = f'{9:0>2}'
mt = f'{2:0>2}'
print(f'date : {dt}/{mt}/{2025}')