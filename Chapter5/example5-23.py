max_load = 500
sum_weight = 0
count = 0
while True :
    count += 1
    w = eval(input(f'น้ำหนักของผู้โดยสารคนที่ : {count} \n ใส่ 0 เพื่อยกเลิก : '))
    print(f'weight {count} >> {w}')
    if w == 0 :
        count -= 1 
        break
    # list_weight += str(w) + ' '

    if (sum_weight + w) > max_load :
        break
    sum_weight += w

print(f'จำนวนผู้โดยสารในลิฟต์ : {count} คน')
print(f'น้ำหนักรวมทั้งหมด {sum_weight} กิโลกรัม')