def read_int(msg) :
    i = input(msg)
    return int(i)

def read_num(msg) :
    i = input(msg)
    return eval(i)

quantity = read_int('จำนวนสินค้าที่ต้องการ : ')

sum = read_int('จำนวนที่ 1 : ') + read_num('จำนวนที่ 2 : ')

print(sum)

if read_num('ราคาสินค้า') <= 0 :
    print('ราคาสินค้าต้องมากกว่า 0 ')

