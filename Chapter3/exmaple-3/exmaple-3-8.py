withdraw = int(input('จำนวนเงินที่จะกดตู้ ATM : '))
print(f'withdraw >> {withdraw}')

b1000 = withdraw // 1000
remain = withdraw % 1000

b500 = remain // 500
remain = withdraw % 500

b100 = remain // 100
remain = withdraw % 100

b50 = remain // 50
remain = withdraw % 50

b20 = remain // 20
remain = withdraw % 20

b10 = remain // 10
remain = withdraw % 10

print(f'1000 = {b1000}' ,
      f'500 = {b500}' ,
      f'100 = {b100}' ,
      f'50 = {b50}' ,
      f'20 = {b20}' ,
      f'10 = {b10}' ,
        sep='\n')