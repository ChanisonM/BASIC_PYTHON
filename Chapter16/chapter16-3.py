from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

window = Tk()
window.geometry('400x250')
window.title('Simple dialog')
window.resizable(0,0)
window.config(bg="lightgray")
window.option_add('*font' , 'tahoma 10')


booleanvar1 = BooleanVar()
check1 = Checkbutton(text="One" , variable=booleanvar1)
check1.pack(side=TOP , anchor=W , padx=10)

booleanvar2 = BooleanVar()
check2 = Checkbutton(text="Two" , variable=booleanvar2)
check2.pack(side=TOP , anchor=W , padx=10)

booleanvar3 = BooleanVar()
check3 = Checkbutton(text="Three" , variable=booleanvar3)
check3.pack(side=TOP , anchor=W , padx=10)


bt = Button(text="Check" , bg="lightgray" , command=lambda:bt_click())
bt.pack(side=TOP , anchor=W , padx=10 , pady=10)

def bt_click():
    select = []
    if booleanvar1.get() :
        select.append(check1.cget('text'))
    if booleanvar2.get():
        select.append(check2.cget('text'))
    if booleanvar3.get():
        select.append(check3.cget('text'))

    string ='.'.join(select)
    messagebox.showinfo(message=string)
    




window.mainloop()