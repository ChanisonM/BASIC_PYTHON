import math 
num = eval(input('กำหนดค้าที่ต้องการหาเลขที่ใกบ้เคียง : '))
integer = math.trunc(num) # ตัดทศนิยมเอาแต่จำนวนเต็ม
fraction = math.modf(num)[0] # ตัดจำนวนเต็มเอาแต่ทศนิยม

if fraction > 0.5 :
    integer += 1
elif fraction < 0.5 :
    integer += -1

print(f'จำนวนเต็มใกล้เคียง คือ : {integer}')
print(f'ประมาณค่าใกล้เคียง round() : ' , round(num))
