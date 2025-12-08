quantity = int(input("จำนวนที่ซื้อ : "))
price = eval(input("ราคาสินค้า : "))
total = price * quantity 
print(f"จำนวนที่ซื้อ {quantity} , ราคาต่อหน่วย {price}")
print(f'รวมเป็นเงิน : {total:,} บาท')
