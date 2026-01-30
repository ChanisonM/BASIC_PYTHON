import sqlite3
from tkinter import * 
from tkinter import messagebox , Scrollbar
from tkinter.scrolledtext import ScrolledText

window = Tk()
window.title("Address Book")
window.geometry('600x300')
window.resizable(0,0)
window.option_add('*font' , 'tahoma 10')
window.option_add('*Button.background' ,'lightgray')


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

add_grid(Label(frame_info , text="id:") , r=0 , c=0)
entry_id = Entry(frame_info , width=14 , bg="lightgray" )
entry_id.bind('<Key>' , lambda e : 'break')
add_grid(entry_id , r=0 , c=1 , span=2)

add_grid(Label(frame_info , text="Name : ") , r=1 ,c=0)
entry_name = Entry(frame_info , width=24)
add_grid(entry_name , r=1 , c=1)

add_grid(Label(frame_info , text="Address : ") , r=2 ,c=0)
entry_address = ScrolledText(frame_info , width=24 , height=3)
add_grid(entry_address , r=2 , c=1)

add_grid(Label(frame_info , text="Phone : ") , r=3 ,c=0)
entry_phone = Entry(frame_info , width=24)
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
    sql = 'SELECT * FROM address_book'
    cursor.execute(sql)
    dataset = cursor.fetchall()
    print(f'{dataset}')


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

    entry_id.insert(0 , row[0])
    entry_name.insert(0 , row[1])
    entry_address.insert(1.0 , row[2])
    entry_phone.insert(0 , row[3])
    entry_email.insert(0 , row[4])
    listbox_selected_index = index
 
    
    


listbox_select()
def button_add_click():
    entries_clear()
    entry_id.insert(0 , '')
    listbox.select_clear(0 , END)

def button_save_click():
    if entry_id.get() == '' : insert()
    else :  update()

def button_delete_click():
    if entry_id.get() == '' :
        messagebox.showerror(message="Please select the items to delete!")
        return
    
    bt = messagebox.askokcancel(message=f"Confrim Delete ?")

    if bt is False : return

    sql = 'DELETE FROM address_book WHERE id = ?'
    r = cursor.execute(sql , [entry_id.get()])
    if r.rowcount == 1 :
        conn.commit()
        messagebox.showinfo(message="Deleted !!")
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

def insert():
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
    entry_id.delete(0 , END)
    entry_name.delete(0 , END)
    entry_name.focus()
    entry_address.delete(1.0 , END)
    entry_phone.delete(0 , END)
    entry_email.delete(0 , END)

def listbox_invoke(index):
    listbox.select_set(index)
    listbox_select()


# --- END :: Funtion --- #




read_database()
listbox_set_items()
if listbox.size() > 0 :
    listbox_invoke(0)
window.mainloop()
conn.close()