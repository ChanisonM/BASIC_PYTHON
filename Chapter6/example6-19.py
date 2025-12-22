from Chapter8.Error import Error

year = 12

salary = int(input("Salary >> "))

if salary < 0 :
    raise Error("Data not correct!!")

incom =  year * salary
print(f'incom / year : {incom : ,.2f} bath')
spend = (40 / 100) * incom
print(f'spend : {spend : ,.2f} bath')

if spend > 60_000 :
    discount = 60_000

incom -= spend
print(f'incom -= spend : {incom : ,.2f}')

discount = 30_000
incom -= discount
print(f'incom -= discount : {incom : ,.2f}')

rate = 0
if incom <= 150_000 :
    rate = 0
elif incom <= 300_000 :
    rate = 5
elif incom <= 500_000 :
    rate = 10
elif incom <= 1_000_000 :
    rate = 20
elif incom <= 2_000_000 :
    rate = 25
elif incom <= 5_000_000 :
    rate = 30
elif incom > 5_000_000 :
    rate = 35

incom -= 150_000

tax = incom * (rate / 100)
print(f'tax payment : {tax : ,.2f} bath')
