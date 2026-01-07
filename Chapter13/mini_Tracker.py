file_name = "expenses.txt"

# count_item = 1

while True :
    print("\n--- Mini Expense Tracker ---")
    print("1. เพิ่มรายการค่าใช้จ่าย")
    print("2. ดูสรุปยอดรวม")
    print("3. ออกจากโปรแกรม")

    choice = input("เลือกเมนู (1/2/3): ")

    if choice == '1' :
       
        try :
            item = input("รายการ : ")
            try :
                price = float(input("ราคา : "))
            except ValueError:
                print("❌ พิมพ์ผิดแล้ว! กรุณากรอกเป็นตัวเลขเท่านั้น (เช่น 50 หรือ 25.5)")
                continue
            
            with open(file_name , mode='a' , encoding="utf-8") as f :
                f.write(f'{item},{price}\n')
            print("บันทึกสำเร็จ")
        except IOError as err:
            print(err)
    

    elif choice == '2' :
        total = 0 
        count = 0
        try :
            with open(file_name , mode='r', encoding='utf-8') as f :
                print("\n--- รายการทั้งหมด ---")
                for line in f :
                    name , price = line.strip().split(',')
                    print(f'- {name} : {price} บาท')
                    total += float(price)
                    count += 1
                print("-"*20)
                print(f'รวมทั้งสิ้น : {total} บาท รวมทั้งหมด {count} รายการ')

        except FileNotFoundError :
            print("ยังไม่มีข้อมูลบันทึกไว้")
        except Exception as e :
            print(f"เกิดข้อผิดพลาด: {e}")

    elif choice == '3' :
        print("ขอบคุณที่ใช้งานครับ!")
        break
    else :
        print("กรุณาเลือกเมนูให้ถูกต้อง")