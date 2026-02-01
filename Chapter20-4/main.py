import sqlite3
from tkinter import * 
from tkinter import messagebox , Scrollbar
from tkinter.scrolledtext import ScrolledText
import re

import csv
from tkinter import filedialog # สำหรับเปิดหน้าต่างเลือกที่บันทึกไฟล์




window = Tk()
window.title("Address Book")
window.geometry('700x600')
window.resizable(0,0)
window.option_add('*font' , 'tahoma 10')
window.option_add('*Button.background' ,'lightgray')


#  --- START :: Fram listbox --- #
frame_search = Frame()
frame_search.pack(side=TOP , padx=20 , pady=20 , anchor=W)
Label(frame_search, text="Search : (Name / Email / Phone)").grid(row=0 , column=0 ,padx=20)
ent_search = Entry(frame_search , width=100)
ent_search.grid(row=0 , column=1)
# Bind เหตุการณ์เมื่อมีการปล่อยคีย์บอร์ดให้ทำการค้นหาทันที
ent_search.bind('<KeyRelease>' , lambda e : search_data())
#  --- END :: Fram listbox --- #


#  --- START :: Fram listbox --- #
fram_listbox = Frame()
fram_listbox.pack(side=LEFT , padx=20 , pady=20 , anchor=NW)

listbox = Listbox(fram_listbox , height=15 , width=22 , selectmode=SINGLE ,exportselection=0)
listbox.bind('<<ListboxSelect>>' , lambda e : listbox_select())
listbox.grid(row=0 , column=0)

scroll = Scrollbar(fram_listbox , command=listbox.yview)
scroll.grid(row=0 , column=1 , sticky=N+S)
listbox.config(yscrollcommand=scroll.set)

#  --- END :: Fram listbox --- #

#  --- START :: Fram Infomation --- #
frame_info = LabelFrame(window , text="Infomation")
frame_info.pack(side=LEFT , padx=0 , pady=0 , anchor=NW)

def add_grid(w , r , c , span = 1):
    w.grid(row=r , column=c , columnspan=span , sticky=NW , padx=10 , pady=5)

def validate_phone(P):
    if(P.isdigit() or P == '') and len(P) <= 10:
        return True
    else : return False



add_grid(Label(frame_info , text="id:") , r=0 , c=0)
entry_id = Entry(frame_info , width=14 , state='readonly')
entry_id.bind('<Key>' , lambda e : 'break')
add_grid(entry_id , r=0 , c=1 , span=2)

add_grid(Label(frame_info , text="Name : ") , r=1 ,c=0)
entry_name = Entry(frame_info , width=24)
add_grid(entry_name , r=1 , c=1)

add_grid(Label(frame_info , text="Address : ") , r=2 ,c=0)
entry_address = ScrolledText(frame_info , width=24 , height=3)
add_grid(entry_address , r=2 , c=1)

add_grid(Label(frame_info , text="Phone : ") , r=3 ,c=0)
vcmd = (window.register(validate_phone) , '%P')
entry_phone = Entry(frame_info , width=24 , validate='key' , validatecommand=vcmd)
add_grid(entry_phone , r=3, c=1)

add_grid(Label(frame_info , text="Email : ") , r=4 ,c=0)
entry_email = Entry(frame_info , width=24)
add_grid(entry_email , r=4, c=1)

button_add = Button(frame_info , text="Add" , command=lambda:button_add_click())
button_add.grid(row=5 , column=0 , padx=10 , pady=10)

button_save = Button(frame_info , text="Save / Edit" , command=lambda:button_save_click())
button_save.grid(row=5 , column=1 , padx=10 , pady=10)

button_delete = Button(frame_info , text="Delete" , command=lambda:button_delete_click())
button_delete.grid(row=5 , column=2 , padx=10 , pady=10)

btn_export_csv = Button(frame_info, text='Export CSV' , command=lambda:export_csv())
add_grid(btn_export_csv , r=6 ,c=0)
#  --- END :: Fram Infomation --- #




# --- START :: Connect to database --- #

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
dataset = []
listbox_selected_index = -1


cursor.execute('''
    CREATE TABLE IF NOT EXISTS address_book (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        address TEXT,
        phone TEXT,
        email TEXT
    )
''')
# --- END :: Connect to database --- #


conn.commit()

# --- START :: Funtion --- #

def read_database():
    global dataset 
    dataset.clear()
    sql = 'SELECT * FROM address_book ORDER BY name COLLATE NOCASE ASC'
    cursor.execute(sql)
    dataset = cursor.fetchall()
    print(f'{dataset}')


def search_data():
        global dataset
        keyword = ent_search.get().strip()
        sql = '''
                SELECT * FROM address_book
                WHERE name LIKE ? OR phone LIKE ? OR email LIKE ?
                ORDER BY name COLLATE NOCASE ASC
            '''
        # ใช้ % ล้อมรอบ keyword เพื่อหาคำที่อยู่ส่วนไหนของประโยคก็ได้
        param = f'%{keyword}%'
        cursor.execute(sql , [param , param , param])
        dataset = cursor.fetchall()

        # อัปเดต Listbox ใหม่
        listbox_set_items()
        
def listbox_set_items():
    global dataset
    names = []
    listbox.delete(0 , END)
    for r in dataset :
        names.append(r[1])
    
    listbox.insert(0 , *names)



def listbox_select(e = None):
    global dataset , listbox_selected_index
    cur_selection = listbox.curselection() # pointer ชี้ index ปัจจุบัน
    if len(cur_selection) == 0 : return

    index = cur_selection[0]
    row = dataset[index]

    entries_clear()

    entry_id.config(state=NORMAL)
    entry_id.insert(0 , row[0])
    entry_id.config(state='readonly')


    entry_name.insert(0 , row[1])
    entry_address.insert(1.0 , row[2])
    entry_phone.insert(0 , row[3])
    entry_email.insert(0 , row[4])
    listbox_selected_index = index
 
listbox_select()

def button_add_click():
    entries_clear()
    # entry_id.insert(0 , '')
    listbox.select_clear(0 , END)

def button_save_click():
    if entry_id.get() == '' : insert()
    else :  update()

def button_delete_click():
    if entry_id.get() == '' :
        messagebox.showerror(message="Please select the items to delete!")
        return
    
    name_to_dalete = entry_name.get()
    bt = messagebox.askokcancel(title=f"Confrim Delete ?" , message=f'Are You Sure Delete : {name_to_dalete} ?')

    if bt is False : return

    sql = 'DELETE FROM address_book WHERE id = ?'
    r = cursor.execute(sql , [entry_id.get()])
    if r.rowcount == 1 :
        conn.commit()
        messagebox.showinfo(title=f'Deleted' , message=f'You {name_to_dalete} Deleted !!')
        refresh()
        entries_clear()
    else :
        messagebox.showerror(message="Wroning Not Data")



def entry_values():
    return [
        entry_name.get() ,
        entry_address.get(1.0 , "end-1c") ,
        entry_phone.get(),
        entry_email.get()
    ]


def validate_inputs():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if not name :
        messagebox.showwarning("Validation Error" , 'Please Input Your Name')
        entry_name.focus()
        return False
    if not phone :
        messagebox.showwarning('Validation Error' , 'Please Input Your Phone')
        entry_phone.focus()
        return False
    
    if not (phone.isdigit() and len(phone) == 10):
        messagebox.showwarning("Validation Error", "Require Phone Number 10 Digis Only !!")
        entry_phone.focus()
        return False
    
    if email :
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern , email) :
            messagebox.showwarning("Validation Error", "Pattern Email :  (ตัวอย่าง: name@gmail.com)")
            entry_email.focus()
            return False
        
    return True


def insert():

    if not validate_inputs() : return
    global listbox_selected_index
    sql = 'INSERT INTO address_book VALUES(null , ? , ? , ? , ?)'
    params = entry_values()
    r = cursor.execute(sql, params)
    if r.rowcount == 1 :
        conn.commit()
        messagebox.showinfo(message="Save data !!")
        listbox_selected_index = listbox.size()
        refresh()
    else :
        messagebox.showerror("Error" ,"Wroning Data not Save !!!")

def update():

    if not validate_inputs() : return


    bt = messagebox.askokcancel(message=f"Confrim UPDATE ?")

    if bt is False : return

    sql = f'''
        UPDATE address_book SET 
        name = ? , address = ? , phone = ? , email = ? 
        WHERE id = ?
    '''
    params = entry_values() + [entry_id.get()] # เพิ่ม ID ต่อท้าย List
    # params = entry_values()
    r = cursor.execute(sql , params)

    if r.rowcount == 1 :
        conn.commit()
        messagebox.showinfo(message="UPDATE SUCCESS !!!")
        refresh()
    else :
        messagebox.showerror('Error' , 'Wroning Data not Update !!!')
def refresh():
    read_database()
    listbox_set_items()
    listbox_invoke(listbox_selected_index)

def entries_clear() :
    entry_id.config(state=NORMAL)
    entry_id.delete(0 , END)
    entry_id.config(state='readonly')

    ent_search.delete(0 , END)
    entry_name.delete(0 , END)
    entry_name.focus()
    entry_address.delete(1.0 , END)
    entry_phone.delete(0 , END)
    entry_email.delete(0 , END)

def listbox_invoke(index):
    listbox.select_set(index)
    listbox_select()


def export_csv():
    # 1. อ่านข้อมูลล่าสุดจากฐานข้อมูล
    read_database()

    if not dataset:
        messagebox.showwarning(title="Export" ,message= "No Data for Export")
        return
    
    # 2. เปิดหน้าต่างถามว่าจะเซฟไฟล์ไว้ที่ไหน
    file_patch = filedialog.asksaveasfilename(
        defaultextension='.csv',
        filetypes=[("CSV files" ,"*.csv"),
                   ('ALL files' , "*.*")],
                   title='Save to CSV File'
    )

    if file_patch :
        try :
            # ใช้ encoding='utf-8-sig' เพื่อให้ Excel อ่านภาษาไทยออกและแยกคอลัมน์
            with open(file_patch , 'w' ,newline='' , encoding='utf-8-sig') as f:
                # กำหนด delimiter=',' (นี่คือหัวใจสำคัญที่ทำให้แยกคอลัมน์)
                writer = csv.writer(f , delimiter=',')

                # เขียน Header (หัวตาราง)
                writer = csv.writer(f)
                writer.writerow(['ID' , 'NAME' , 'ADDRESS' , 'PHONE' , 'EMAIL'])

                # เขียนข้อมูลทั้งหมดจาก dataset
                writer.writerows(dataset)

            messagebox.showinfo(title="Export Success" , message=f'Export {file_patch}')
        except Exception as e :
            messagebox.showerror(title='Export Error' , message=f'Error {e}')

# --- END :: Funtion --- #




read_database()
listbox_set_items()
if listbox.size() > 0 :
    listbox_invoke(0)
window.mainloop()
conn.close()