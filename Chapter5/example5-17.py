# กำหนดช่วงของแม่สูตรคูณ (ตัวตั้ง) ตั้งแต่ 1 ถึง 12
start_multiplier = 1 
end_multiplier = 12

# กำหนดช่วงของตัวคูณ ตั้งแต่ 1 ถึง 12
start_multiplicand = 1 
end_multiplicand = 12 

# ลูป for ตัวนอก: วนซ้ำเพื่อเลือก "แม่สูตรคูณ" (i)
for i in range(start_multiplier , end_multiplier + 1):
    print(f'--- แม่ {i} ---')

    # ลูป for ตัวใน: วนซ้ำเพื่อเลือก "ตัวคูณ" (j)
    for j in range(start_multiplicand , end_multiplicand + 1) :
        # คำนวณผลลัพธ์
        result = i * j
        # พิมพ์ประโยคสูตรคูณในรูปแบบที่อ่านง่าย
        print(f'{i:2} X {j:2} = {result:3}')
    # พิมพ์บรรทัดว่างเพื่อแยกแต่ละแม่สูตรคูณ
    print()
