balance = 30_000
limited = 20_000
print(f'{balance} THB')

withdraw = int(input('Input withdraw : '))
print(f'withdraw >> {withdraw}')

if balance < withdraw :
    print("You can not over withdraw balance")
elif withdraw > limited :
    print(f'You can not over {limited} balance')
elif withdraw % 100 != 0 :
    print('100 only mods')
else :
    balance -= withdraw

print(f'Remaining balance >> {balance} THB')
