number = int(input("Input Number : "))
print(f'Number : {number}')

x = number // 1000
print(x)

r = number % 1000
x = r //100
print(x)

r = r % 100
x = r // 10
print(x)

x = r % 10 
print(x)
