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
ent_total = Entry(width=15)
ent_total.grid(row=3 , column=1 , sticky=W)

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

def btn_first_click():
    print("btn_first_click")

def btn_prev_click():
     print("btn_prev_click")

def btn_next_click():
     print("btn_next_click")

def btn_last_click():
     print("btn_last_click")

def btn_add_product_click():
     print("btn_add_product_click")

def btn_save_product_click():
     print("btn_save_product_click")

def btn_delete_product_click():
     print("btn_delete_product_click")



window.mainloop()