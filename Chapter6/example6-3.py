import random 

print(" ----- Sale of 7 day -----")
for d in range(1 , 8) :
    print(f' วันที่ {d} ' , end='')
    sales = random.randint(1, 20)
    print("*" * sales , end=" ")
    print(f'({sales})')