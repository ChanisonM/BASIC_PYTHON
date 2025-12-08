balance = 1000

print(f'total : {balance} balance')

withdraw =  int(input('withdraw : '))
balance -= withdraw
print(f'deposit : {withdraw} , total : {balance}')


deposit = int(input('deposit : '))
balance += deposit
print(f'deposit : {deposit} , total : {balance}')