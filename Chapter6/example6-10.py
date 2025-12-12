start = 1 
end = 9000
pn = ''

for n in range(start , end + 1) :
    sum = 0
    stop = n // 2
    
    for d in range(1 , stop + 1) :
        if n % d == 0 :
            sum += d
    
    if sum == n :
        pn += str(n) + ' '

print(f' {start} - {end}')
print(f'Perfect Number is {pn}')