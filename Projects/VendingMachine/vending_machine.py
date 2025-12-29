# vending_machine + log
import datetime

def save_history(data_string):
    file = None
    try:
        # เปิดไฟล์ history.txt แบบ 'a' (append) เพื่อเขียนต่อท้าย
        file = open("vending_history.txt" , 'a',encoding="utf-8")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f'[{timestamp}] {data_string}\n') 
    except Exception as e:
        print(f'❌ Save file not success {e}')
    finally :
        # ไม่ว่าจะเกิดอะไรขึ้น ต้องปิดไฟล์เพื่อคืนทรัพยากรให้ระบบ
        if file :
            file.close()
            print("💾 System : Save history and Close file complete")

def vending_machine(money, *drinks, **options):
    menu = {"Coke": 20, "Water": 10, "Green Tea": 25}
    total_cost = 0
    selected_items = []

    # คำนวณราคาสินค้า
    for item in drinks:
        if item in menu:
            total_cost += menu[item]
            selected_items.append(item)

    if not selected_items:
        return "ไม่มีการสั่งซื้อ"

    # สรุปผลการทำงาน
    items_str = ", ".join(selected_items)
    if money >= total_cost:
        result_msg = f"ซื้อ {items_str} สำเร็จ (จ่าย: {money}, รวม: {total_cost}, ทอน: {money-total_cost})"
        print(f"✅ {result_msg}")
        # --- เรียกใช้ฟังก์ชันบันทึกไฟล์ ---
        save_history(result_msg)
    else:
        result_msg = f"ซื้อ {items_str} ไม่สำเร็จ (เงินไม่พอ: มี {money} แต่ต้องจ่าย {total_cost})"
        print(f"❌ {result_msg}")
        save_history(result_msg)

# --- ส่วนรับเงิน (Input) ---
while True:
    try:
        val = input("\nหยอดเหรียญ (หรือพิมพ์ 'exit'): ")
        if val.lower() == 'exit': break
        
        amount = float(val)
        # ลองสั่ง Coke และ Green Tea พร้อมระบุความหวาน
        vending_machine(amount, "Coke", "Green Tea", sugar="50%")
        
    except ValueError:
        print("⚠️ กรุณาใส่ตัวเลขครับ")

print("จบการทำงาน")
