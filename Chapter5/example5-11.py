amount = eval(input("Amount :: "))
# print(f'amount >> {amount}')

rate = eval(input('feet per year :: '))
# print(f'feet >> {rate}')

year = int(input("Invested period :: "))
# print(f'year >> {year}')

rate /= 100

for y in range(1 , year+1) :
    fv = amount * ((1 + rate) ** y)
    print(f'year {y} amount : {fv:,.2f} bath')