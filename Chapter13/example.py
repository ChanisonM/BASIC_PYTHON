# ระดับที่ 1 , 2: พื้นฐานการเขียนไฟล์ (Basic Writing)
# โจทย์: จงเขียนโปรแกรมเพื่อรับชื่อเล่นของตัวคุณจากคีย์บอร์ด (input) จากนั้นให้นำชื่อนั้นไปบันทึกลงในไฟล์ชื่อ my_name.txt
# file_name = 'myname.txt'
# try : 
#     # Write File
#     with open(file_name , mode='w' , encoding='utf-8') as f :
#         data = input("Input Your Name : ")
#         f.write(data)

#     # Read file
#     with open(file_name , mode='r', encoding='utf-8') as r :
#         print(r.read().strip())

# except IOError as err :
#     print(err)



# ระดับที่ 3: การเพิ่มข้อมูลต่อท้าย (Appending Multiple Lines)
# โจทย์: เราจะสร้างระบบ "บันทึกรายการสินค้า" (Shopping List)
# file_name = "shopping_list.txt"
# try :
#     with open(file_name , mode='a' , encoding='utf-8') as data:
#         for i in range(1 , 4) :
#             items = input(f"No. {i} : List Name >> ")
#             data.write(f'No. {i} : {items}\n')
            
    
# except IOError as err :
#     print(err)



# ลองทดสอบและก้าวสู่ ระดับที่ 4 (ระดับสูงสุด!)
# โจทย์ระดับ 4: การประมวลผลข้อมูลคะแนน (Data Processing)
# รายชื่อคะแนนที่เราต้องการบันทึก
# write file
raw_scores = [85, 42, 76, 90, 55, 30, 88, 62]
file_name = 'scores.txt'
try:
    with open(file_name, mode='w', encoding='utf-8') as f:
        for s in raw_scores:
            # สำคัญ: ต้องแปลงเป็น string และใส่ \n เพื่อให้คะแนนอยู่คนละบรรทัด
            f.write(f"{s}\n")
    print(f"สร้างไฟล์ {file_name} สำเร็จแล้ว!")
except IOError as err:
    print(f"เกิดข้อผิดพลาด: {err}")

# read file 
file_name = "scores.txt"

total_score = 0
student_count = 0
passed_students = 0

try :
    with open(file_name , mode='r', encoding='utf-8') as data :
        for line in data :
            score = int(line.strip())
            total_score += score
            student_count += 1
            
            if score >= 50 :
                passed_students += 1

            if student_count > 0:
                average = total_score / student_count
            else:
                average = 0


        print(f'Sumary : {total_score}')
        print(f'Count : {student_count}')
        print(f'Pass Count {passed_students}')
        print(f'Average :  {average:.2f}')
       
except IOError as err :
    print(err)




