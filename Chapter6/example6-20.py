from Error import Error

price = int(input("Car pice >> "))
if price < 0 :
    raise Error("Car pice not correct !!")

rate = eval(input("feet per year >> "))
if rate < 0 :
    raise Error("Feet not correct !!")

r = rate / 100
r /= 12

down = eval(input("Car down (%) >> "))
if down <= 0 or down > 100 :
    raise Error("Down pice not correct !!")
d  = (down / 100) * price
finance = price - d

months = int(input("months >> "))
if months < 0 :
    raise Error('Number of installments not correct !!')

interest = finance * months * r
total = finance + interest
installment = total / months
print(f'installments (months) {installment :,.2f} bath')