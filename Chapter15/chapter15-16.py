from tkinter import *
from datetime import datetime

window = Tk()
window.title('Date Time')
window.geometry('400x400')
window.resizable(0,0)
window.config(bg="lightgray")


def text_changed(*args):
    strvar2.set(strvar1.get())


strvar1 = StringVar()
strvar1.trace_add('write' , text_changed)


ent1 = Entry(textvariable=strvar1)
ent1.grid(row=0 , column=0)

strvar2 = StringVar()
ent2 = Entry(textvariable=strvar2 , state=DISABLED)
ent2.grid(row=1 , column=0)

window.mainloop()
