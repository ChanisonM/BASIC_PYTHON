from tkinter import *
from datetime import datetime

window = Tk()
window.title('Expense & Budget')
window.geometry('550x600') # ขยายขนาดเล็กน้อยให้พอดีกับฟอนต์ใหญ่
window.config(padx=20, pady=20)
window.option_add('*font', 'tahoma 12') # ปรับฟอนต์ลงมานิดเพื่อให้เห็นภาพรวมง่ายขึ้น
window.option_add('*Entry.width', 25)

history = [] # เก็บยอดเงิน (บวกคือรายรับ ลบคือรายจ่าย)

def add_record(type_name):
    item = ent_item.get()
    amount_str = ent_amount.get()
    
    # ตรวจสอบว่ากรอกข้อมูลครบไหม
    if item == "" or amount_str == "":
        return 

    try:
        amount = float(amount_str)
        if type_name == "รายจ่าย":
            amount = -amount # ถ้าเป็นรายจ่ายให้ติดลบ
        
        # เก็บเข้าตัวแปร list
        history.append(amount)
        
        # แสดงผลใน Listbox
        now = datetime.now().strftime('%H:%M')
        display_text = f"[{now}] {item}: {amount:,.2f}"
        listbox.insert(END, display_text)
        
        # อัปเดตสรุปยอด
        update_summary()
        
        # ล้างข้อมูลหลังบันทึก
        ent_item.delete(0, END)
        ent_amount.delete(0, END)
        
    except ValueError:
        print("กรุณากรอกเฉพาะตัวเลข")

def update_summary():
    total = sum(history)
    lb_total.config(text=f"ยอดเงินคงเหลือ: {total:,.2f} บาท")
    # เปลี่ยนสีตัวเลขตามสถานะการเงิน
    if total < 0:
        lb_total.config(fg="red")
    else:
        lb_total.config(fg="green")

# --- UI ส่วนบน: กรอกข้อมูล ---
Label(text="ชื่อรายการ : ").grid(row=0, column=0, sticky=E, pady=5)
ent_item = Entry()
ent_item.grid(row=0, column=1)

Label(text="จำนวนเงิน : ").grid(row=1, column=0, sticky=E, pady=5)
ent_amount = Entry()
ent_amount.grid(row=1, column=1)

# --- UI ส่วนกลาง: ปุ่มกด ---
fm_button = Frame(window)
fm_button.grid(row=2, column=0, columnspan=2, pady=20)

btn_income = Button(fm_button, text="รายรับ", bg="lightgreen", width=10, 
                    command=lambda: add_record("รายรับ"))
btn_income.grid(row=0, column=0, padx=5)

btn_expense = Button(fm_button, text="รายจ่าย", bg="#ff9999", width=10, 
                     command=lambda: add_record("รายจ่าย"))
btn_expense.grid(row=0, column=1, padx=5)

# --- UI ส่วนล่าง: แสดงประวัติและสรุปผล ---
listbox = Listbox(window, width=50, height=10)
listbox.grid(row=3, column=0, columnspan=2, pady=10)

lb_total = Label(text="ยอดเงินคงเหลือ: 0.00 บาท", font="tahoma 16 bold")
lb_total.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()