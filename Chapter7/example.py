# ข้อที่ 1: การเพิ่มข้อมูลท้าย List
# my_fruits = ["apple", "banana", "cherry"]
# my_fruits.append("orange")
# print(my_fruits)

# ข้อที่ 2: การแทรกข้อมูลในตำแหน่งที่กำหนด
# numbers = [10, 20, 40, 50]
# numbers.insert(2,30)
# print(numbers)

# ข้อที่ 3: การลบข้อมูลตามค่าที่ระบุ
# colors = ["red", "green", "blue", "green", "yellow"]
# print(colors)
# colors.remove("green")
# print(colors)

# ข้อที่ 4: การเรียงลำดับข้อมูลใน List
# data = [5, 1, 9, 3, 7]
# print(data)
# data.sort()
# print(data)

# ข้อที่ 5: การนับจำนวนสมาชิกที่ซ้ำกัน
# votes = ["A", "B", "A", "C", "B", "A", "B"]
# votes_a = votes.count("A")
# print(votes_a)

# ข้อที่ 6: การนับและแสดงผลเฉพาะสมาชิกที่ไม่ซ้ำกัน (Combining count() and Logic)
# items = ["book", "pen", "book", "pencil", "pen", "book"]
# unique_items = list(set(items))
# print(unique_items)
# for item in unique_items :
#     count = items.count(item)
#     print(f'{item} \t ปรากฏ {count} ครั้ง')


# ข้อที่ 7: การสร้าง List ใหม่จากการกรองและรวมข้อมูล (Filtering and Appending)
# temperatures = [35, 28, 41, 25, 30, 45, 22]
# hot_days = []
# for temp in temperatures :
#     if temp > 30 :
#         hot_days.append(temp)
# print(hot_days)

# ข้อที่ 8: การย้อนกลับการเรียงลำดับ (Reverse Sorting)
# score = [88, 95, 76, 99, 81]
# score.sort(reverse=True)
# print(score)




# size = 5
# for i in range(size) :
#     for j in range(size) :
#         print('*' , end=' ')
#     print()

# size = 5
# for i in range(size):
#     # 1. ลูปพิมพ์ช่องว่าง (รันให้เสร็จก่อน)
#     for j in range(size - i - 1):
#         print(' ', end="")
#     # 2. ลูปพิมพ์ดาว (อยู่ระดับเดียวกับลูป j แต่อยู่หลัง j)
#     for k in range(i + 1):
#         print('*', end=" ")
#     # 3. เมื่อจบทั้งช่องว่างและดาวในแถวนั้นแล้ว ค่อยขึ้นบรรทัดใหม่
#     print()

            # *
            # * *
            # * * *
            # * * * *
            # * * * * *

size = 5
for i in range(size):
    for j in range(size - i - 1):
        print(' ', end="")
    for k in range(i + 1):
        print('*', end=" ")
    print()

for i in range(size -1 , 0 , -1):
    for j in range(size - i):
        print(' ', end="")
    for k in range(i):
        print('*', end=" ")
    print()


            #     * 
            #    * * 
            #   * * *
            #  * * * *
            # * * * * *
            #  * * * *
            #   * * *
            #    * *
            #     *