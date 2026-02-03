from tkinter import *
from tkinter import messagebox, filedialog
from database import AddressBookDB
from PIL import Image, ImageTk
from datetime import datetime
import os
import shutil
import re

class AddressBookApp:
    def __init__(self, root):
        self.root = root 
        self.root.title("Address Book OOP - Professional Edition")
        self.root.geometry('900x600')
        
        # 1. Initialize Backend & Folders
        self.db = AddressBookDB()
        self._prepare_storage()
        
        # 2. State Management
        self.dataset = []
        self.selected_image_path = ""
        
        # 3. Build UI
        self.setup_ui()
        self.refresh_grid()

    def validate_phone(self, action, value_if_allowed):
        # action '1' คือการพิมพ์เพิ่ม (insert)
        if action == '1':
            # ต้องเป็นตัวเลขเท่านั้น และความยาวรวมต้องไม่เกิน 10
            if not value_if_allowed.isdigit() or len(value_if_allowed) > 10:
                return False
        return True
    
    def is_valid_email(self, email):
        # รูปแบบมาตรฐาน: ตัวอักษร@ตัวอักษร.ตัวอักษร
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def _prepare_storage(self):
        """จัดการเตรียมโฟลเดอร์เก็บรูป"""
        if not os.path.exists("images"):
            os.makedirs("images")

    def setup_ui(self):
        """ส่วนหลักในการวาง Layout"""
        # Header
        Label(self.root, text="ระบบจัดการสมุดรายชื่อ", fg="#2c3e50", font=("Arial", 16, "bold")).pack(pady=10)

        # แบ่งหน้าจอเป็น 2 ฝั่ง (ซ้าย: รายการ, ขวา: ฟอร์ม)
        main_container = Frame(self.root)
        main_container.pack(fill=BOTH, expand=True, padx=10)

        self._setup_left_panel(main_container)
        self._setup_right_panel(main_container)

    def _setup_left_panel(self, parent):
        """ฝั่งซ้าย: ค้นหาและรายชื่อ"""
        left_frame = Frame(parent)
        left_frame.pack(side=LEFT, fill=Y, padx=10)

        Label(left_frame, text="ค้นหา:").pack(anchor=W)
        self.ent_search = Entry(left_frame, width=40)
        self.ent_search.pack(pady=5)
        self.ent_search.bind('<KeyRelease>', self.search_data)

        self.listbox = Listbox(left_frame, width=40, height=20, exportselection=0)
        self.listbox.bind('<<ListboxSelect>>', self.on_listbox_select)
        self.listbox.pack(pady=5)

    def _setup_right_panel(self, parent):
        """ฝั่งขวา: รายละเอียดข้อมูลและรูปภาพ"""
        self.frame_info = LabelFrame(parent, text=" ข้อมูลส่วนตัว ", padx=10, pady=10 )
        self.frame_info.pack(side=RIGHT, fill=BOTH, expand=True)

        # Input Fields Container
        fields_frame = Frame(self.frame_info)
        fields_frame.grid(row=0, column=0, sticky=NSEW )

        # สร้าง Entry Fields (จัด Group เพื่อความสวยงาม)
        self.ent_name = self._create_input(fields_frame, "ชื่อ:", 0)
        self.ent_address = self._create_input(fields_frame, "ที่อยู่:", 1)
        self.ent_phone = self._create_input(fields_frame, "เบอร์โทร:", 2)
        self.ent_email = self._create_input(fields_frame, "อีเมล:", 3)

        # Image Display Area
        self._setup_image_section()
        
        # Buttons Area
        self._setup_button_actions()

    def _create_input(self, parent, label_text, row):
        """Helper สร้าง Label + Entry แบบลดโค้ดซ้ำซ้อน"""
        Label(parent, text=label_text).grid(row=row, column=0, sticky=W, pady=5)
        

        # --- ส่วนที่เพิ่มเข้าไป ---
        if label_text == "เบอร์โทร:":
            vcmd = (self.root.register(self.validate_phone), '%d', '%P')
            entry = Entry(parent, width=35, validate='key', validatecommand=vcmd)
        else:
            entry = Entry(parent, width=35)
        # -----------------------
        # entry = Entry(parent, width=35)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    def _setup_image_section(self):
        """ส่วนแสดงรูปภาพ"""


        self.img_label = Label(self.frame_info, text="No Image", bg="lightgray") 
        self.img_label.grid(row=0, column=2, padx=0, pady=0, sticky=NW)
       
        
        Button(self.frame_info, text="เลือกรูปภาพ", command=self.browse_image).grid(row=1, column=2, pady=5)






    def _setup_button_actions(self):
        """ส่วนปุ่มคำสั่งหลัก"""
        btn_container = Frame(self.frame_info)
        btn_container.grid(row=4, column=0, columnspan=2, pady=20)
        
        Button(btn_container, text="บันทึกใหม่", command=self.save_data, bg="#27ae60", fg="white", width=10).pack(side=LEFT, padx=5)
        Button(btn_container, text="แก้ไข", command=self.edit_data, bg="#2980b9", fg="white", width=10).pack(side=LEFT, padx=5)
        Button(btn_container, text="ลบ", command=self.delete_data, bg="#c0392b", fg="white", width=10).pack(side=LEFT, padx=5)
        Button(btn_container, text="ล้างช่องกรอก", command=self.clear_entries, width=10).pack(side=LEFT, padx=5)

    # --- Logic Methods (ยังคงเดิมแต่จัดระเบียบใหม่) ---
    
    def upload_and_copy_image(self, source_path):
        if not source_path or not os.path.exists(source_path):
            return ""
        ext = os.path.splitext(source_path)[1]
        new_filename = f"img_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"
        destination = os.path.join('images', new_filename)
        shutil.copy(source_path, destination)
        return destination

    def refresh_grid(self):
        self.dataset = self.db.fetch_all()
        self.listbox.delete(0, END)
        for row in self.dataset:
            self.listbox.insert(END, row[1])

    def search_data(self, event=None):
        keyword = self.ent_search.get().strip()
        self.dataset = self.db.search(keyword) if keyword else self.db.fetch_all()
        self.listbox.delete(0, END)
        for row in self.dataset:
            self.listbox.insert(END, row[1])

    def save_data(self):
        name = self.ent_name.get().strip()
        phone = self.ent_phone.get().strip()
        email = self.ent_email.get().strip()
        
        if not name or not phone:
            messagebox.showwarning("คำเตือน", "กรุณากรอกชื่อและเบอร์โทร!")
            return
        

        if not phone.isdigit():
            messagebox.showerror("Error", "เบอร์โทรศัพท์ต้องเป็นตัวเลขเท่านั้น!")
            return  
        
        if len(phone) > 10 :
            messagebox.showerror("Error", "เบอร์โทรศัพท์ต้องไม่เกิน 10 หลัก!")
            return
        
        if len(phone) < 9 :
            messagebox.showerror("Error", "เบอร์โทรศัพท์สั้นเกินไป!")
            return

        if email and not self.is_valid_email(email):
            messagebox.showerror("Error", "รูปแบบอีเมลไม่ถูกต้อง! (ตัวอย่าง: name@email.com)")
            return


        new_path = self.upload_and_copy_image(self.selected_image_path)
        data = [name, self.ent_address.get().strip(), phone, self.ent_email.get().strip(), new_path]
        self.db.insert(data)
        
        messagebox.showinfo("สำเร็จ", "บันทึกข้อมูลแล้ว")
        self.refresh_grid()
        self.clear_entries()

    def edit_data(self):
        selection = self.listbox.curselection()
        email = self.ent_email.get().strip()
        phone = self.ent_phone.get().strip()
        name = self.ent_name.get().strip()
        if not selection: 
            messagebox.showwarning("Warning" , "กรุณาเลือกรายชื่อที่จะแก้ไข!")
            return
        
        index = selection[0]
        record_id = self.dataset[index][0]
        old_path = self.dataset[index][5]
        new_path = old_path

        if self.selected_image_path:
            new_path = self.upload_and_copy_image(self.selected_image_path)
            if old_path and os.path.exists(old_path):
                try: os.remove(old_path)
                except: pass
            self.selected_image_path = ""


        if not name or not phone:
            messagebox.showwarning("คำเตือน", "กรุณากรอกชื่อและเบอร์โทร!")
            return
        

        if not phone.isdigit():
            messagebox.showerror("Error", "เบอร์โทรศัพท์ต้องเป็นตัวเลขเท่านั้น!")
            return  
        
        if len(phone) > 10 :
            messagebox.showerror("Error", "เบอร์โทรศัพท์ต้องไม่เกิน 10 หลัก!")
            return
        
        if len(phone) < 9 :
            messagebox.showerror("Error", "เบอร์โทรศัพท์สั้นเกินไป!")
            return


        if email and not self.is_valid_email(email):
            messagebox.showerror("Error", "รูปแบบอีเมลไม่ถูกต้อง! (ตัวอย่าง: name@email.com)")
            return

        data = [self.ent_name.get().strip(), self.ent_address.get().strip(), 
                self.ent_phone.get().strip(), self.ent_email.get().strip(), new_path]

        if messagebox.askokcancel("ยืนยัน", "แก้ไขข้อมูลนี้ใช่หรือไม่?"):
            self.db.update(data, record_id)
            self.refresh_grid()
            messagebox.showinfo("สำเร็จ", "แก้ไขข้อมูลแล้ว")

    def delete_data(self):
        selection = self.listbox.curselection()
        if not selection: 
            messagebox.showwarning("Warning", "กรุณาเลือกรายชื่อที่จะลบ!")
            return
        
        index = selection[0]
        row = self.dataset[index]
        if messagebox.askokcancel("ลบข้อมูล", f"ต้องการลบ '{row[1]}' ?"):
            self.db.delete(row[0])
            if row[5] and os.path.exists(row[5]):
                try: os.remove(row[5])
                except: pass
            self.refresh_grid()
            self.clear_entries()

    def clear_entries(self):
        for entry in [self.ent_name, self.ent_address, self.ent_phone, self.ent_email]:
            entry.delete(0, END)
        self.img_label.config(image="", text="No Image")
        self.selected_image_path = ""

    def on_listbox_select(self, event):
        selection = self.listbox.curselection()
        if not selection: return
        row = self.dataset[selection[0]]
        self.clear_entries()
        self.ent_name.insert(0, row[1])
        self.ent_address.insert(0, row[2])
        self.ent_phone.insert(0, row[3])
        self.ent_email.insert(0, row[4])
        self.show_image(row[5])

    def browse_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if path:
            self.selected_image_path = path
            self.show_image(path)

    def show_image(self, path):
        try:
            if path and os.path.exists(path):
                img = Image.open(path).resize((120, 120))
                self.photo = ImageTk.PhotoImage(img)
                self.img_label.config(image=self.photo, text="")
            else:
                self.img_label.config(image="", text="No Image")
        except:
            self.img_label.config(image="", text="Error Loading")

if __name__ == "__main__":
    root = Tk()
    app = AddressBookApp(root)
    root.mainloop()