# VendingMachine + log + MemberShip

import json , os , datetime


def load_member():
    # ตรวจสอบว่ามีไฟล์อยู่ไหม ถ้าไม่มีให้สร้าง Dictionary ว่าง
    if not os.path.exists("members.json") :
        return {}

    with open("members.json" , "r" ,encoding="utf-8") as f:
        return json.load(f)

def save_members(data) :
    with open("members.json" , "w" , encoding="utf-8") as f :
        json.dump(data , f , indent=4 , ensure_ascii=False)

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


def vending_machine(money , *drinks , **options):
    menu = {"Coke": 20, "Water": 10, "Green Tea": 25}
    total_cost = 0
    selected_items = [item for item in drinks if item in menu]

    for item in selected_items :
        total_cost += menu[item]

    if not selected_items or money < total_cost :
        # print("❌ การสั่งซื้อล้มเหลว (สินค้าไม่มีหรือเงินไม่พอ)")
        result_msg = f"ซื้อ {selected_items} ไม่สำเร็จ (เงินไม่พอ: มี {money} แต่ต้องจ่าย {total_cost})"
        save_history(result_msg)
        return

    # --- ส่วนของระบบสมาชิก (ดึงจาก **kwargs) ---
    member_id = options.get('member_id')
    members_db = load_member()
    
    # result_msg = f"✅ ซื้อสำเร็จ: {', '.join(selected_items)} | ยอดรวม {total_cost} บาท"
    result_msg = f"ซื้อ {', '.join(selected_items)} สำเร็จ (จ่าย: {money}, รวม: {total_cost}, ทอน: {money-total_cost})"
    save_history(result_msg)

    if member_id :
        # ถ้าเป็นสมาชิก: คำนวณแต้ม (10 บาท = 1 แต้ม)
        new_points = total_cost // 10

        if member_id in members_db :
            members_db[member_id] += new_points
        else :
            members_db[member_id] = new_points # สมัครสมาชิกใหม่ทันที
            print(f"🎊 ยินดีต้อนรับสมาชิกใหม่คุณ {member_id}!")

        print(f"⭐ คุณได้รับ {new_points} แต้ม | แต้มสะสมทั้งหมด: {members_db[member_id]} แต้ม")
        save_members(members_db)
        
    else :
        print("💡 เคล็ดลับ: ใส่เบอร์โทรศัพท์เพื่อสะสมแต้มได้นะ!")
    
# --- 3. ส่วนรับค่าจากหน้าจอ (Main) ---
while True:
    try:
        print("\n=== ตู้ขายน้ำอัจฉริยะ ===")
        val = input("หยอดเหรียญ (หรือ 'exit'): ")
        if val.lower() == 'exit': break
        
        money = float(val)
        phone = input("กรอกเบอร์สมาชิก (ไม่ใส่กด Enter): ")
        
        # เรียกใช้งาน (ถ้า phone ว่าง member_id จะเป็น None)
        vending_machine(money, "Coke", "Green Tea", member_id=phone if phone else None)
        
    except ValueError:
        print("⚠️ กรุณากรอกตัวเลขให้ถูกต้อง")

print("ขอบคุณที่ใช้บริการครับ")
