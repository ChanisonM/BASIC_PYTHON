for i in range(1,11):
    fact = 1
    for n in range(i , 1 , -1) :
        fact *= n
    print(f'{i}! = {fact:,}')
