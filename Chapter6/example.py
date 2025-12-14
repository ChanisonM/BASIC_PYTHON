# โจทย์ข้อ 1: นับถอยหลัง (Countdown)
# time = 10
# while time > 0 :
#     time -= 1
#     print(f'Time : {time}')
# print("Lift off!")
# -------------------------------------------------

# โจทย์ข้อ 2: ผลรวมของจำนวนเต็มบวก
# sum = 0
# count = 0
# while True :
#     count += 1
#     x = int(input(f'{count} : Sumary >> '))
#     if x == 0 :
#         break
#     sum += x
# print(f'Total sumary {sum}')
# -------------------------------------------------

# โจทย์ข้อ 3: ตรวจสอบรหัสผ่าน
# SECRET_PASSWORD = 12345
# user_input = 0
# while user_input != SECRET_PASSWORD :
#     user_input = int(input("Input your password : "))
#     if user_input != SECRET_PASSWORD :
#         print("รหัสผ่านไม่ถูกต้อง โปรดลองอีกครั้ง")
# print("รหัสผ่านถูกต้อง")
# -------------------------------------------------

# ข้อที่ 4: แสดงผลตัวเลขคู่ (Printing Even Numbers)
# x = 2 
# while x <= 20 :
#     print(x)
#     x += 2
# -------------------------------------------------

# 5.
# balance = 1_000
# goal = 1_500
# rate = 0.10
# years = 0

# print(f"Year 0: Starting balance {balance:,.2f} bath")
# while balance < goal :
#     balance = balance * (1 + rate)
#     years += 1
#     print(f'Year : {years} >> {balance :,.2f} bath')

# print(f'Finish : Excess amount {goal:,.2f} bath (current) {balance:,.2f} bath use time {years} Years')

# -------------------------------------------------
# 6.Plus of 3
# x = 3 
# while x <= 50 :
#     print(x)
#     x += 3 
# -------------------------------------------------

# # ข้อที่ 7: การหาค่าเฉลี่ย (Finding the Average)
# total_sum = 0
# valid_count = 0

# while True :
#     x = int(input(f"Input your Number {valid_count + 1} >> "))
#     if x < 0 :
#         break
#     total_sum += x
#     valid_count +=1

# print(f'Sumary : {total_sum}')
# if valid_count > 0 :
#     final_average = total_sum / valid_count
#     print(f'ค่าเฉลี่ย (Average) : {final_average :.2f}')   
# else :
#     print("ไม่มีตัวเลขที่ใช้คำนวณ (ป้อนเลขติดลบตั้งแต่แรก)")
# -------------------------------------------------
    
# โจทย์ข้อที่ 8: การจัดการเมนู
choice = 0
while choice != 4 :
    print("\n--- เมนูหลัก ---")
    print("1. ดูสถานะ")
    print("2. ตั้งค่า")
    print("3. ช่วยเหลือ")
    print("4. ออกจากโปรแกรม")

    choice = int(input("รับอินพุตจากผู้ใช้ (1 - 4) >> "))
    if choice == 1 :
        print(">> คุณเลือก: ดูสถานะ")
    elif choice == 2 :
         print(">> คุณเลือก: ตั้งค่า")
    elif choice == 3 :
         print(">> คุณเลือก: ช่วยเหลือ")
    elif choice == 4 :
        print("✅ ขอบคุณที่ใช้โปรแกรม กำลังออกจากระบบ...")
    else :
        print("⚠️ ตัวเลือกไม่ถูกต้อง โปรดเลือกตัวเลขระหว่าง 1 ถึง 4")

# -------------------------------------------------

# ข้อที่ 9: พลังของ 2 (Powers of 2)
# x = 1
# while x <= 1_000 :
#     print(x)
#     x *= 2
    
# if x > 1_000 :
#     print(x)
    

# ข้อที่ 10: จำนวนหลักของตัวเลข (Counting Digits)
# number = int(input("Number >> "))
# digit_count = 0

# while number > 0 :
#     number = number // 10
#     digit_count += 1
#     print(number)

# print(digit_count)

# -------------------------------------------------
# โจทย์ที่ 11: พิมพ์ชื่อสัตว์
# animals = ["cat", "dog", "fish", "bird"]
# for animal in animals :
#     print(animal)

# -------------------------------------------------
# โจทย์ที่ 12: ผลรวมตัวเลข 1 ถึง 100
# total = 0
# for i in range(1,101) :
#     total += i
# print(total)
# -------------------------------------------------

# โจทย์ที่ 13: นับถอยหลังเป็นเลขคู่
# for i in range(20 , 1 , -2) :
#     print(i)


# text = "Python"
#   for index , value in enumerate(text) :
#     index คือ ลำดับที่ของสมาชิก (0, 1, 2, ...)
#     value คือ ค่าของสมาชิกตัวนั้น
#     แสดงลำดับ (Index) ของอักขระนั้น โดยใช้ฟังก์ชัน enumerate()
#   print(f'{index} : {value}')
# -------------------------------------------------

# โจทย์ที่ 15: ตรวจสอบความถี่ในลิสต์
data = [1, 2, 1, 3, 4, 1, 5]
count_ones = 0
for i in data :
    if i == 1 :
        count_ones += i
print(count_ones)
