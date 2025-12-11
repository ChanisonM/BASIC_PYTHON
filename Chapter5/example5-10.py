nums = 5
max = 0
for i in range (1 , nums+1) :
    n = eval(input(f"Number {i} :: "))
    # print(n , ' ' , end=' ')
    if n > max :
        max = n

print(f'maximun >> {max}')
