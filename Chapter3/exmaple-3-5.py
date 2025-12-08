quantity = int(input('จำนวนสินค้าที่ซื้อ : '))
print(f'quantity >>   {quantity} ชิ้น' )

price = int(input("ราคาสินค้าต่อหน่วย : "))
print(f'price >>   {price} บาท')

total = quantity * price 
print(f'รวมทั้งหมด : {total:,} บาท')

discount = total * (100 - 10) / 100
print(f'ลด 10% เหลือ : {discount:,} บาท' )

pay = eval(input(f'รวม {discount:,} จำนวนเงินที่จ่าย : ' ))
print(f'pay >> {pay:,}')

change = pay - discount
print(f'จำนวนเงินทอน {change:,} บาท')