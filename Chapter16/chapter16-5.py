from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

window = Tk()
window.geometry('400x250')
window.title('Radio Button')
window.resizable(0,0)
window.config(bg="lightgray")
window.option_add('*font' , 'tahoma 10')


items = ['Black' , 'Orange' , 'Pink' , 'Yellow']
combo =Combobox(values=items , width=15)
combo.bind('<<ComboboxSelected>>' , lambda e:combo_select())
combo.current(0)
combo.pack()

def combo_select():
    get_combo = combo.get()
    print(get_combo)
    if get_combo == "Black" : 
        window.config(bg=get_combo)
    elif get_combo == 'Orange':
        window.config(bg=get_combo)
    elif get_combo == 'Pink':
        window.config(bg=get_combo)
    elif get_combo == 'Yellow':
        window.config(bg=get_combo)

    messagebox.showinfo(message=get_combo)

window.mainloop()