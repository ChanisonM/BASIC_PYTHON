base = eval(input("base : "))
print(f'base >> {base}')

power = int(input("exponent : "))
print(f'power >> {power}')

if power >= 0 :
    result = 1 
    for i in range(0 , power) :
        result *= base

    print(f'{base}^{power} = {result:,}')
else :
    print("Plase input exponent int")