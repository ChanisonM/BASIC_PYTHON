import tkinter as tk
from tkinter import messagebox # เพิ่มตัวนี้เพื่อทำ Pop-up แจ้งเตือน



title = 'Expense Input Test'

# 1. สร้างหน้าต่างหลัก
root = tk.Tk()
root.title(title)
root.geometry('400x500')

# ไฟล์
file_name = 'expenses.txt'



# --- 1. ฟังก์ชันโหลดข้อมูลลง Listbox ---
def load_to_listbox() :
    listbox.delete(0,tk.END)
    try :
        with open(file_name , mode='r' , encoding='utf-8') as f :
            for line in f :
                name , price = line.strip().split(',')
                display_text = f'{name} -- {float(price):,.2f} บาท'
                listbox.insert(tk.END , display_text)

    except FileNotFoundError:
        pass
    

# --- 2. ปรับฟังก์ชัน save_data ให้สั่งอัปเดต Listbox ด้วย ---
def save_data() :
    # ใช้ .get() เพื่อดึงสิ่งที่ผู้ใช้พิมพ์ออกมา 
    item = entry_item.get()
    price_str = entry_price.get()

    # 1. ตรวจสอบว่ากรอกข้อมูลครบไหม
    if item == "" or price_str == "" :
        messagebox.showwarning("คำเตือน" , "กรุณากรอกข้อมูลให้ครบทุกช่องนะ!")
        return
    try :
        # 2. แปลงราคาเป็นตัวเลข
        price = float(price_str)

        # 3. บันทึกลงไฟล์ (ใช้ความรู้เดิมของคุณเลย!)
        with open(file_name , mode='a' , encoding='utf-8') as f :
            f.write(f'{item},{price}\n')

        load_to_listbox()
        
        # 4. แจ้งเตือนเมื่อสำเร็จ
        messagebox.showinfo("สำเร็จ" ,f"บันทึก {item} เรียกร้อย")
        
        # 5. ล้างช่องพิมพ์
        entry_item.delete(0,tk.END)
        entry_price.delete(0,tk.END)

    except ValueError:
        messagebox.showerror("ผิดพลาด", "ราคาต้องเป็นตัวเลขเท่านั้น (เช่น 100 หรือ 50.5)")
        


def view_data():
    all_text = ''
    total = 0
    try : 
        with open(file_name , mode='r' , encoding='utf-8') as f :
            for line in f :
                name , price = line.strip().split(',')
                all_text += f'• {name} : {float(price):,.2f} บาท\n'
                total += float(price)

            # ถ้ามีข้อมูล ให้โชว์ใน messagebox
            if all_text :
                all_text += f'\n{'*'*10}\n ยอดรวมทั้งหมด : {total:,.2f} บาท'
                messagebox.showinfo("รายการทั้งหมด" , all_text)
            else :
                messagebox.showinfo("ว่างเปล่า" , "ยังไม่มีข้อมูลบันทึกไว้")
            
    except FileNotFoundError:
        messagebox.showwarning("ไม่พบไฟล์", "ยังไม่มีไฟล์ข้อมูล (ลองบันทึกรายการแรกก่อน)")


# --- 1. ฟังก์ชันสำหรับลบรายการที่เลือก ---
def delete_selected():
    
    try : 
        # ดึงลำดับ (Index) ที่ผู้ใช้เลือกไว้จาก Listbox
        selected_index = listbox.curselection()

        if not selected_index :
            messagebox.showinfo("คำเตือน", "กรุณาคลิกเลือกรายการที่จะลบก่อนครับ")
            return
        
        # ถามเพื่อยืนยันการลบ
        confirm = messagebox.askyesno("ยืนยัน", "คุณแน่ใจใช่ไหมว่าจะลบรายการนี้?")
        if confirm :
            index_to_delete = selected_index[0]

            with open(file_name , mode='r' , encoding='utf-8') as f :
                lines = f.readlines()
            
            del lines[index_to_delete]

            # เขียนข้อมูลที่เหลือกลับลงไฟล์ (Write ทับ)
            with open(file_name , mode='w' , encoding='utf-8') as f :
                f.writelines(lines)
            
            # รีเฟรชหน้าจอ Listbox ใหม่
            load_to_listbox()
            messagebox.showinfo("สำเร็จ", "ลบรายการเรียบร้อยแล้ว")

    except Exception as e:
        messagebox.showerror("ผิดพลาด", f"ไม่สามารถลบได้: {e}")



# ประกาศตัวแปร global ไว้ที่ส่วนบนของโค้ด (ข้างนอกฟังก์ชัน)

def edit_selected():
    try:
        selected_index = listbox.curselection()
        if not selected_index:
            messagebox.showwarning("คำเตือน", "กรุณาเลือกรายการที่จะแก้ไขก่อนครับ")
            return
        
        index = selected_index[0]
        
        # อ่านไฟล์เพื่อเอาข้อมูลดิบ (ชื่อ,ราคา) ของบรรทัดนั้น
        with open("expenses.txt", mode='r', encoding="utf-8") as f:
            lines = f.readlines()
            
        target_line = lines[index].strip().split(',')
        name_to_edit = target_line[0]
        price_to_edit = target_line[1]
        
        # ล้างช่องพิมพ์เก่า แล้วเอาค่าที่จะแก้ใส่เข้าไปแทน
        entry_item.delete(0, tk.END)
        entry_item.insert(0, name_to_edit)
        
        entry_price.delete(0, tk.END)
        entry_price.insert(0, price_to_edit)
        
        # เก็บตำแหน่ง Index ไว้ในตัวแปรชั่วคราว (เพื่อใช้ตอนกดบันทึกทับ)
        global edit_index
        edit_index = index
        
        btn_save.config(text="ยืนยันการแก้ไข", bg="orange", command=update_data)
        
    except Exception as e:
        messagebox.showerror("ผิดพลาด", f"ไม่สามารถดึงข้อมูลได้: {e}")

def update_data():
    try:
        new_item = entry_item.get()
        new_price = entry_price.get()
        
        with open("expenses.txt", mode='r', encoding="utf-8") as f:
            lines = f.readlines()
            
        # แก้ไขข้อมูลใน List ตามตำแหน่งที่เราเก็บไว้
        lines[edit_index] = f"{new_item},{float(new_price)}\n"
        
        with open("expenses.txt", mode='w', encoding="utf-8") as f:
            f.writelines(lines)
            
        # คืนค่าปุ่มให้เป็น "บันทึกข้อมูล" ตามปกติ
        btn_save.config(text="บันทึกข้อมูล", bg="green", command=save_data)
        
        entry_item.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        load_to_listbox()
        messagebox.showinfo("สำเร็จ", "แก้ไขข้อมูลเรียบร้อยแล้ว")
        
    except ValueError:
        messagebox.showerror("ผิดพลาด", "กรุณากรอกราคาเป็นตัวเลข")






# --- 3. ส่วนการจัดวางหน้าจอ (UI) ---
tk.Label(root , text="บันทึกรายการจ่าย" , font=("Arial", 18 , "bold")).pack(pady=10)

tk.Label(root , text="รายการ" , font=("Arial", 18 , "bold")).pack()
entry_item = tk.Entry(root , font=("Arial", 18 , "bold"))
entry_item.pack(pady=5)


tk.Label(root , text="ราคา" , font=("Arial", 18 , "bold")).pack()
entry_price = tk.Entry(root , font=("Arial", 18 , "bold"))
entry_price.pack(pady=5)

# สร้างบันทึกข้อมูล
btn_save = tk.Button(root , text="บันทึกข้อมูล" , font=("Arial", 18) , command=save_data , bg="green" , fg="white" ,)
btn_save.pack(pady=10)

# สร้างปุ่มลบ
btn_delete = tk.Button(root, text="ลบรายการที่เลือก", font=("Arial", 18) , command=delete_selected, bg="red", fg="white")
btn_delete.pack(pady=5)

btn_edit = tk.Button(root, text="ดึงข้อมูลมาแก้ไข", font=("Arial", 18) , command=edit_selected, bg="orange", fg="black")
btn_edit.pack(pady=5)


# --- 4. ส่วนของ Listbox (หัวใจหลักของรอบนี้) ---
tk.Label(root , text="รายการทั้หมด : ", font=("Arial", 18)).pack()
# สร้าง Listbox และปรับฟอนต์ให้ใหญ่ขึ้นที่นี่!
listbox = tk.Listbox(root , width=40 , height=40 , font=("Tahoma" , 12))
listbox.pack(pady=10 , padx=10)

# สั่งให้โหลดข้อมูลขึ้นมาโชว์ทันทีที่เปิดโปรแกรม
load_to_listbox()


root.mainloop()