from tkinter import *
from datetime import datetime

window = Tk()
window.title('Expense & Budget')
window.geometry('400x500')
window.config(padx=20 , pady=20)
window.option_add('font' , 'tahoma 20')
window.option_add('*Entry.width' , 40 )
history = []




def add_record(type_name):
    item = ent_item.get()
    amount = ent_amount.get()

    if item != "" and amount != "":
        try:
            amount = float(amount)
            # สร้างข้อความบันทึก: [เวลา] ประเภท: รายการ = จำนวน
            now = datetime.now().strftime('%H:%M')
            record = f"[{now}] {type_name}: {item} = {amount:,.2f} บาท"
            
            # เพิ่มลงใน List และแสดงผลใน Listbox
            history.append(amount if type_name == "รายรับ" else -amount)
            listbox.insert(END, record)
            
            # คำนวณสรุปยอดคงเหลือ
            update_summary()
            
            # ล้างช่องกรอก
            ent_item.delete(0, END)
            ent_amount.delete(0, END)
        except ValueError:
            print("กรุณากรอกตัวเลขในช่องจำนวนเงิน")

def update_summary():
    total = sum(history)
    lb_total.config(text=f"ยอดคงเหลือ: {total:,.2f} บาท", fg="blue" if total >= 0 else "red")


# --- การจัดวางหน้าจอ (UI) ---
Label(text="ชื่อรายการ:").pack(anchor=W)
ent_item = Entry()
ent_item.pack(pady=5)

Label(text="จำนวนเงิน:").pack(anchor=W)
ent_amount = Entry()
ent_amount.pack(pady=5)

# เฟรมสำหรับปุ่ม
fm_buttons = Frame(window)
fm_buttons.pack(pady=10)

btn_income = Button(fm_buttons , 
                    text="รายรับ" , 
                    bg="lightgreen" , 
                    width=10,
                    command=lambda: add_record("รายรับ"))
btn_income.pack(side=LEFT , padx=5)

btn_expense = Button(fm_buttons ,
                     text="รายจ่าย",
                     bg="#ff9999",
                     width=10 ,
                     command=lambda : add_record("รายจ่าย"))
btn_expense.pack(side=LEFT , padx=5)

# ส่วนแสดงประวัติการทำรายการ
Label(text="ประวัติรายการ").pack(anchor=W , pady=5)
listbox = Listbox(window , width=50 , height=50)
listbox.pack()

# ส่วนสรุปยอดคงเหลือ
lb_total = Label(text="ยอดคงเหลือ: 0.00 บาท" , pady=10)
lb_total.pack()

window.mainloop()
