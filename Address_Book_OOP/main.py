from tkinter import *
from tkinter import messagebox
from database import AddressBookDB # ดึง databse ชื่อ Class AddressBookDB มาทำงาน
import os
import shutil
from tkinter import filedialog
from PIL import Image , ImageTk


class AddressBookApp:
    def __init__(self , root):
        self.root = root 
        self.root.title("Address Book OOP Version")
        self.root.geometry('900x550')
    
        # เรียกใช้งาน Database
        self.db = AddressBookDB()
        self.dataset = []

        # สร้าง UI
        self.setup_ui()

        # ทดสอบดึงข้อมูลมาแสดงทันทีที่เปิดโปรแกรม
        self.refresh_grid()

    
    def setup_ui(self):

        def add_grid(w , r , c):
            w.grid(row = r , column = c)


        # สร้าง Label ง่ายๆ มาทดสอบก่อน
        Label(self.root, text="ยินดีด้วย! หน้าจอเชื่อมต่อกับ Database สำเร็จแล้ว", fg="green").pack(pady=20)
        
        # สร้าง Listbox มาลองโชว์รายชื่อ
        self.listbox = Listbox(self.root, width=50 , exportselection=0)
        self.listbox.bind('<<ListboxSelect>>' , self.on_listbox_select)
        self.listbox.pack(pady=10)

        # เฟรมสำหรับข้อมูล (Information Frame)
        self.frame_info = LabelFrame(self.root , text="รายละเอียดข้อมูล")
        self.frame_info.pack(side=RIGHT , padx=20 , pady=10 , fill=BOTH , expand=TRUE)

        # สร้างฟิลด์กรอกข้อมูล
        self.label_name = Label(self.frame_info , text="ชื่อ : ")
        add_grid(self.label_name , r= 0 , c=0)
        self.ent_name = Entry(self.frame_info , width=30)
        add_grid(self.ent_name , r = 0 , c = 1)

        self.label_address = Label(self.frame_info , text="ที่อยู่ : ")
        add_grid(self.label_address , r= 1 , c=0)
        self.ent_address = Entry(self.frame_info , width=30)
        add_grid(self.ent_address , r=1 ,c=1)

        self.label_phone = Label(self.frame_info , text="เบอร์โทร : ")
        add_grid(self.label_phone , r= 2 , c=0)
        self.ent_phone = Entry(self.frame_info , width=30)
        add_grid(self.ent_phone , r=2 ,c=1)

        self.label_email = Label(self.frame_info , text="อีเมล : ")
        add_grid(self.label_email , r= 3 , c=0)
        self.ent_email = Entry(self.frame_info , width=30)
        add_grid(self.ent_email , r=3 ,c=1)


        btn_frame = Frame(self.frame_info)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10)
        Button(btn_frame, text="บันทึกใหม่", command=self.save_data).pack(side=LEFT, padx=2)
        Button(btn_frame, text="แก้ไข", command=self.edit_data).pack(side=LEFT, padx=2)
        Button(btn_frame, text="ลบ", command=self.delete_data, bg="red", fg="white").pack(side=LEFT, padx=2)
        Button(btn_frame, text="ล้างช่องกรอก", command=self.clear_entries).pack(side=LEFT, padx=2)
        

        self.img_label = Label(self.frame_info, text="No Image", bg="lightgray") 
        self.img_label.grid(row=0, column=2, rowspan=4, padx=20, pady=10, sticky=N)
        self.btn_browse = Button(self.frame_info , text="Upload" , command=self.browse_image)
        self.btn_browse.grid(row=4, column=2, pady=5)

        # ตัวแปรสำหรับเก็บ Path รูปที่เลือก
        self.selected_image_path = ""



    def refresh_grid(self):
        # ดึงข้อมูลจากฐานข้อมูลผ่านเครื่องยนต์ (db.fetch_all)
        self.dataset = self.db.fetch_all()
        
        # ล้าง Listbox และใส่ชื่อเข้าไปใหม่
        self.listbox.delete(0, END)
        for row in self.dataset:
            # row[1] คือคอลัมน์ NAME
            self.listbox.insert(END, row[1])

    def save_data(self):
        # 1. ดึงข้อมูลจากช่องกรอก (Entry/Text)
        name = self.ent_name.get().strip()
        address = self.ent_address.get().strip()
        phone = self.ent_phone.get().strip()
        email = self.ent_email.get().strip()

        # 2. ตรวจสอบเบื้องต้น
        if not name or not phone :
            messagebox.showwarning("Warning" , "กรุณากรอกชื่อและเบอร์โทร!")
            return
        # 3. สั่งเครื่องยนต์ (database.py) ให้ทำงาน
        data = [name  , address , phone , email , self.selected_image_path]
        self.db.insert(data)

        # 4. อัปเดตหน้าจอ
        messagebox.showinfo("Success" , "บันทึกข้อมูลเรียบร้อย!")
        self.refresh_grid()
        self.clear_entries()

    def edit_data(self):
        
        selection = self.listbox.curselection()
        if not selection :
            messagebox.showwarning("Warning" , "กรุณาเลือกรายชื่อที่จะแก้ไขจากด้านบน!")
            return 
        
        # ดึง ID ของแถวที่เลือกจาก dataset
        index = selection[0]
        print(f'Edit Index : {index}')
        record_id  = self.dataset[index][0]
        print(f"Record_ID : {record_id}")

        data = [
            self.ent_name.get().strip(),
            self.ent_address.get().strip(),
            self.ent_phone.get().strip(),
            self.ent_email.get().strip(),
            self.selected_image_path
        ]


        if messagebox.askokcancel("Confirm", "คุณต้องการแก้ไขข้อมูลนี้ใช่หรือไม่?") :
            self.db.update(data , record_id)
            messagebox.showinfo("Success" , "แก้ไขข้อมูลเรียบร้อย!")
            self.refresh_grid()
            print(f'Data : {data}')


    def delete_data(self):
        selection = self.listbox.curselection()
        if not selection :
            messagebox.showwarning("Warning", "กรุณาเลือกรายชื่อที่จะลบ!")      
            return

        index = selection[0]
        print(f"Index : {index}")
        row = self.dataset[index]
        print(f"ROW : {row}")
        record_id = row[0]
        print(f"RECORD ID : {record_id}")
        name = row[1]
        print(f"NAME : {name}")

        if messagebox.askokcancel("Confirm Delete", f"คุณต้องการลบคุณ '{name}' ใช่หรือไม่?"):
            self.db.delete(record_id)
            messagebox.showinfo("Deleted", "ลบข้อมูลเรียบร้อย!")
            self.refresh_grid()
            self.clear_entries()
     
    
    def clear_entries(self):
        self.ent_name.delete(0 , END)
        self.ent_address.delete(0 , END)
        self.ent_phone.delete(0 , END)
        self.ent_email.delete(0 , END)

    def on_listbox_select(self , even):
        # 1. ตรวจสอบว่ามีการเลือกข้อมูลจริงไหม
        selection = self.listbox.curselection()
        if not selection : return

        # 2. ดึง Index ที่เลือก และไปหยิบข้อมูลจาก self.dataset
        index = selection[0]
        row = self.dataset[index]

        # 3. ล้างช่องกรอกเดิมก่อน
        self.clear_entries()

        # 4. เอาข้อมูลใหม่ไปวางในแต่ละช่อง
        # หมายเหตุ: ถ้าใช้ ID เป็น Entry อย่าลืมใส่ id ไปด้วยถ้าคุณสร้างไว้
        self.ent_name.insert(0 , row[1])
        self.ent_address.insert(0,row[2])
        self.ent_phone.insert(0 , row[3])
        self.ent_email.insert(0 , row[4])
        self.show_image(row[5])



    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            self.selected_image_path = file_path
            self.show_image(file_path)
        
   
    def show_image(self, path):
        try:
            if path and os.path.exists(path):
                img = Image.open(path)
                img = img.resize((200, 200), Image.Resampling.LANCZOS) # ปรับขนาดรูป
                self.photo = ImageTk.PhotoImage(img)
                self.img_label.config(image=self.photo, text="")
            else:
                self.img_label.config(image="", text="No Image")
        except:
            self.img_label.config(image="", text="Error Loading")

if __name__ == "__main__" :
    root = Tk()
    app = AddressBookApp(root)
    root.mainloop()
