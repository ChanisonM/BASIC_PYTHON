from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import sqlite3

window = Tk()
window.title('Product System')
window.geometry('350x300')
window.resizable(0,0)
window.config(padx=5 , pady=20)
window.option_add('*font' , 'tahoma 10')
window.option_add('*Button.background' , 'lightgray')




Label(text="Product Name").grid(row=1 ,column=0 , padx=3 , ipadx=5 , sticky=W)
ent_name = Entry(width=30)
ent_name.grid(row=1 , column=1 , sticky=W)

Label(text="Price / Unit").grid(row=2 , column=0, padx=3 , ipadx=5 , sticky=W)
ent_price = Entry(width=15)
ent_price.grid(row=2 , column=1 , sticky=W)

Label(text="Total").grid(row=3 , column=0 , padx=3 , ipadx=5 , sticky=W)
ent_remain = Entry(width=15)
ent_remain.grid(row=3 , column=1 , sticky=W)

Label(text="Description").grid(row=4 , column=0 , padx=3 , ipadx=5 , sticky=W)
text_desc = ScrolledText(width=30 , height=3)
text_desc.grid(row=4 , column=1 , pady=6 , sticky=W)


# --- Start : Frame 1 ---#
frame1 = Frame(window)
frame1.grid(row=5 , column=0 , columnspan=2)

btn_first = Button(frame1 , text="|<" , command=lambda:btn_first_click())
btn_first.pack(side=LEFT , padx=3 , pady=10 , ipadx=5)

btn_prev = Button(frame1 , text="<" , command=lambda:btn_prev_click())
btn_prev.pack(side=LEFT , padx=3 , pady=10 , ipadx=5)

lbl_row = Label(frame1 , text="No. : 0/0")
lbl_row.pack(side=LEFT , padx=3 ,ipadx=5)

btn_next = Button(frame1 , text=">" , command=lambda:btn_next_click())
btn_next.pack(side=LEFT , padx=3 , pady=10 , ipadx=5)

btn_last = Button(frame1 , text=">|" , command=lambda:btn_last_click())
btn_last.pack(side=LEFT , padx=3 , pady=10 , ipadx=5)
# --- End : Frame 1 ---#

# --- Start : Frame 2 ---#
frame2 = Frame()
frame2.grid(row=6 , column=0 , columnspan=2)

btn_add = Button(frame2 , text="Add Product" , command=lambda:btn_add_product_click())
btn_add.pack(side=LEFT , padx=5 , pady=15 , ipadx=5)

btn_save = Button(frame2 , text="Save Product" , command=lambda:btn_save_product_click())
btn_save.pack(side=LEFT , padx=5 , pady=15 , ipadx=5)

btn_delete = Button(frame2 , text="Delete Product" , command=lambda:btn_delete_product_click())
btn_delete.pack(side=LEFT , padx=5 , pady=15 , ipadx=5)
# --- End : Frame 2 ---#

dataset = []
row_index = -1
product_id = -1
num_rows = 0
first_add = True

conn = sqlite3.connect('database.db')
cur = conn.cursor()
dataset = None

def read_data():
     global dataset , num_rows
     sql = 'SELECT * FROM product'
     cur.execute(sql)
     dataset = cur.fetchall()
     num_rows = len(dataset)

def show_data(index = 0):
     global dataset , row_index , num_rows , product_id
     row_index = index
     row = dataset[index]
     product_id = row[0]
     name = StringVar(value=row[1])
     ent_name.config(textvariable=name)

     p = row[2]
     if p % 1 == 0.0 : p = int(p)
     ent_price.config(textvariable=StringVar(value=p))
     ent_remain.config(textvariable=StringVar(value=row[3]))
     text_desc.delete(1.0 , END)
     text_desc.insert(END , row[4])
     lbl_row.config(text=f'No. : {row_index + 1} / {num_rows}')





def btn_first_click():
    global num_rows
    show_data(0)

def btn_prev_click():
     global row_index , num_rows
     if(row_index - 1) < 0 : return
     row_index -= 1
     show_data(row_index)

def btn_next_click():
     global row_index , num_rows 
     if(row_index + 1) >= num_rows : return
     row_index += 1
     show_data(row_index)

def btn_last_click():
     global num_rows
     show_data(num_rows - 1)


def btn_add_product_click():
     global row_index , first_add
     ent_name.delete(0 , END)
     ent_price.delete(0 , END)
     ent_remain.delete(0 , END)
     text_desc.delete(1.0 , END)
     row_index = -1
     lbl_row.config(text="No. : ? / ?")
     if first_add :
          messagebox.showinfo(message="Please Insert New Data ....")
          first_add = False
def btn_save_product_click():
     global dataset , row_index , product_id
     params = [
          ent_name.get(),
          ent_price.get(),
          ent_remain.get(),
          text_desc.get(1.0 , END).strip()

     ]

     if row_index == -1 :
          sql = 'INSERT INTO product VALUES(null,?,?,?,?)'
          r = cur.execute(sql , params)
          if r.rowcount > 0 :
               conn.commit()
               messagebox.showinfo(message="Save to database success !!")
               read_data()
               show_data()
          else :
               messagebox.showerror(message="Wrorning")
     else :
          mb = messagebox.askokcancel(
               title="Edit" , message="Confirm edit this data"
          )
          if mb == True :
               sql = f'''
                    UPDATE product SET
                    name = ? , price = ? , remain = ? , description = ? 
                    WHERE id = {product_id}
               '''
               r = cur.execute(sql , params)
               if r.rowcount > 0 :
                    conn.commit()
                    messagebox.showinfo(message="Edit Success")
                    read_data()
                    show_data(row_index)
               else :
                    messagebox.showerror(message="Error")
          else : return


def btn_delete_product_click():
     global row_index , product_id 
     if row_index == -1 : return
     mb = messagebox.askokcancel(
          title="Delete" ,
          message=f"Confirm Delete {ent_name.get()}"
     )

     if mb == True :
          sql = f'DELETE FROM product WHERE id = {product_id}'
          r = cur.execute(sql)
          if r.rowcount > 0 :
               conn.commit()
               messagebox.showinfo(message="Delete Success !!!")
               read_data()
               show_data()
          else :
               messagebox.showerror(message="Error")
     else : return
def renew():
     read_data()
     show_data()

renew()

window.mainloop()