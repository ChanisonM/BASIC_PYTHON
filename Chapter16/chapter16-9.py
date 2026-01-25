from tkinter import *
from tkinter.ttk import  Notebook , Style , Combobox
from tkinter.font import Font
from tkinter import messagebox



window = Tk()
window.geometry('500x500')
window.title('Radio Button')
window.resizable(0,0)
window.config(bg="lightgray")
window.option_add('*font' , 'tahoma 10')


# ---- Notebook & Tab ---- #
notebook = Notebook(window , width=200 , height=200 )
tab_font = Frame(notebook)
tab_color = Frame(notebook)
notebook.add(tab_font , text="ตัวอักษร")
notebook.add(tab_color , text="สี")
notebook.pack()

style = Style()
font = Font(family='tahoma' , size='16' , weight='bold')
style.configure('TNotebook.Tab' , font=font)
style.configure('TNotebook.Tab' , padding=[5 , 2])
style.configure('TNotebook.Tab' , foreground='navy')
win_bg = window.cget('bg')
style.configure('TNotebook.Tab' ,background=win_bg)

# ----- Tab : ตัวอักษร ----- #
fm_listbox = Frame(tab_font)
fm_listbox.pack(pady=30)
lbx1 = Listbox(fm_listbox , height=5 , width=15)
fonts = ['tahoma' , 'Angsana' , 'Leelawadee' , 'Times' , 'Segeo' , 'Arial']
lbx1.insert(0 , *fonts)
lbx1.grid(row=0 , column=0 , padx=10)

scroll = Scrollbar(fm_listbox , command=lbx1.yview)
scroll.grid(row=0 , column=1 , sticky=N+S)
lbx1.config(yscrollcommand=scroll.set)

# ----- Tab : Colors ----- #
items = ['Red' , 'Blue' , 'Green' , 'Pink' , 'Orange' ,'White' , 'Black' , 'Brown']
combo = Combobox(tab_color , values=items , width=15)
combo.bind('<<ComboboxSelected>>' , lambda e:combo_selected())

combo.current(0)
combo.pack(pady=30)


def combo_selected():
    print(combo.get())
    messagebox.showinfo(message=combo.get())
window.mainloop()