import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
FILE_NAME = 'expenses.txt'
FONT_MAIN = ("Arial", 12)
FONT_BOLD = ("Arial", 12, "bold")
edit_index = None  # ตัวแปรกลางสำหรับโหมดแก้ไข

# --- 🛠️ HELPER FUNCTIONS (ส่วนจัดการข้อมูลซ้ำๆ) ---

def read_file():
    """อ่านไฟล์แล้วคืนค่าเป็น List ของบรรทัดข้อมูล"""
    try:
        with open(FILE_NAME, mode='r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def write_file(lines):
    """เขียน List ข้อมูลกลับลงไฟล์"""
    with open(FILE_NAME, mode='w', encoding='utf-8') as f:
        f.writelines(lines)

def refresh_ui():
    """ฟังก์ชันกลางสำหรับอัปเดต Listbox (ใช้ซ้ำได้ทุกที่)"""
    listbox.delete(0, tk.END)
    search_term = entry_search.get().lower()
    
    for line in read_file():
        name, price = line.strip().split(',')
        if search_term in name.lower():
            listbox.insert(tk.END, f"{name} -- {float(price):,.2f} บาท")

# --- 🎮 ACTION FUNCTIONS (การทำงานของปุ่มต่างๆ) ---

def save_data():
    global edit_index
    item, price_str = entry_item.get(), entry_price.get()
    
    if not item or not price_str:
        messagebox.showwarning("เตือน", "กรอกข้อมูลให้ครบก่อนครับ")
        return

    try:
        new_line = f"{item},{float(price_str)}\n"
        lines = read_file()

        if edit_index is not None:  # ถ้าอยู่ในโหมดแก้ไข
            lines[edit_index] = new_line
            edit_index = None
            btn_save.config(text="บันทึกข้อมูล", bg="green")
        else:  # ถ้าเป็นการเพิ่มใหม่
            lines.append(new_line)

        write_file(lines)
        entry_item.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        refresh_ui()
    except ValueError:
        messagebox.showerror("ผิดพลาด", "ราคาต้องเป็นตัวเลข")

def delete_data():
    sel = listbox.curselection()
    if not sel: return
    
    if messagebox.askyesno("ยืนยัน", "ลบรายการนี้ใช่ไหม?"):
        lines = read_file()
        del lines[sel[0]]
        write_file(lines)
        refresh_ui()

def prepare_edit():
    global edit_index
    sel = listbox.curselection()
    if not sel: return
    
    index = sel[0]
    line = read_file()[index].strip().split(',')
    
    entry_item.delete(0, tk.END)
    entry_item.insert(0, line[0])
    entry_price.delete(0, tk.END)
    entry_price.insert(0, line[1])
    
    edit_index = index
    btn_save.config(text="ยืนยันการแก้ไข", bg="orange")


def clear_all():
    if messagebox.askyesno("ยืนยันขั้นเด็ดขาด", "คุณต้องการล้างข้อมูลทั้งหมดใช่ไหม?") :
        write_file([])
        refresh_ui()
        messagebox.showinfo("สำเร็จ", "ข้อมูลทั้งหมดถูกลบแล้ว")


def show_graph():
    plt.rcParams['font.family'] = 'Tahoma'
    data = [line.strip().split(',') for line in read_file()]
    if not data: return

    names = [d[0] for d in data]
    prices = [float(d[1]) for d in data]

    plt.figure(figsize=(8, 5))
    plt.bar(names, prices, color='skyblue')
    plt.title("สรุปรายจ่าย")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# --- 🎨 UI LAYOUT ---
root = tk.Tk()
root.title("My Expense Pro")
root.geometry("400x700")

# Input Section
tk.Label(root, text="รายการอาหาร", font=FONT_BOLD).pack(pady=10)

entry_item = tk.Label(root, text="รายการอาหาร", font=FONT_BOLD).pack(pady=10)
entry_item = tk.Entry(root, font=FONT_MAIN); entry_item.pack()

entry_price = tk.Label(root, text="ราคา", font=FONT_BOLD).pack(pady=10)
entry_price = tk.Entry(root, font=FONT_MAIN); entry_price.pack(pady=5)

btn_save = tk.Button(root, text="บันทึกข้อมูล", bg="green", fg="white", command=save_data)
btn_save.pack(pady=5)

# Search & List Section
tk.Label(root, text="🔍 ค้นหา:", font=FONT_BOLD).pack(pady=10)
entry_search = tk.Entry(root, font=FONT_MAIN)
entry_search.pack()
entry_search.bind("<KeyRelease>", lambda e: refresh_ui()) # ค้นหาอัตโนมัติ

listbox = tk.Listbox(root, font=("Tahoma", 11), height=10)
listbox.pack(pady=10, fill=tk.X, padx=20)

# Control Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="แก้ไขรายการ", command=prepare_edit, bg="orange").pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="ลบรายการ", command=delete_data, bg="red", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(root, text="📊 ดูสรุปกราฟ", command=show_graph, bg="purple", fg="white").pack(pady=10)



refresh_ui() # โหลดข้อมูลครั้งแรก

btn_clear = tk.Button(root, text="⚠️ ล้างข้อมูลทั้งหมด", font=("Arial", 9), command=clear_all, bg="#333", fg="white")
btn_clear.pack(side=tk.BOTTOM, pady=20)
root.mainloop()