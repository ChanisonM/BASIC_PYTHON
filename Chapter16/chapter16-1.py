from tkinter import *
from tkinter import simpledialog

window = Tk()
window.geometry('400x400')
window.title('Simple dialog')
window.config(bg="lightgray")

lbl = Label(pady=10 , bg='lightgray')
lbl.pack()

Button(text="Integer" , command=lambda:ask('i')).pack(pady=5)
Button(text="Float" , command=lambda:ask('f')).pack(pady=5)
Button(text="String" , command=lambda:ask('s')).pack(pady=5)

def ask(type):
    if type == 'i' :
        r = simpledialog.askinteger('int' , 'Integer')
    elif type == 'f' :
        r = simpledialog.askfloat('float' , 'Float')
    elif type == 's' :
        r = simpledialog.askstring('string' , "String")
    
    if r != None : lbl.config(text=r)

window.mainloop()