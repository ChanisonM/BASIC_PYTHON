# โจทย์ข้อ 1: นับถอยหลัง (Countdown)
# time = 10
# while time > 0 :
#     time -= 1
#     print(f'Time : {time}')
# print("Lift off!")

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


# โจทย์ข้อ 3: ตรวจสอบรหัสผ่าน
# SECRET_PASSWORD = 12345
# user_input = 0
# while user_input != SECRET_PASSWORD :
#     user_input = int(input("Input your password : "))
#     if user_input != SECRET_PASSWORD :
#         print("รหัสผ่านไม่ถูกต้อง โปรดลองอีกครั้ง")

# print("รหัสผ่านถูกต้อง")

# ข้อที่ 4: แสดงผลตัวเลขคู่ (Printing Even Numbers)
# x = 2 
# while x <= 20 :
#     print(x)
#     x += 2

balance = 1_000
goal = 1_500
rate = 0.10
years = 0

print(f"Year 0: Starting balance {balance:,.2f} bath")
while balance < goal :
    balance = balance * (1 + rate)
    years += 1
    print(f'Year : {years} >> {balance :,.2f} bath')

print(f'Finish : Excess amount {goal:,.2f} bath (current) {balance:,.2f} bath use time {years} Years')