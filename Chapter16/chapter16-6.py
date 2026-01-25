from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('400x250')
window.title('Radio Button')
window.resizable(0,0)
window.config(bg="lightgray")
window.option_add('*font' , 'tahoma 10')



frame = Frame(window)
lbx = Listbox(
    frame,
    height=5,
    width=20,
    selectmode=MULTIPLE,
    exportselection=0
)

colors = ['red' , 'green' , 'blue' , 'pink' , 'brown' , 'orange' , 'black']
lbx.insert(0 , *colors)
lbx.insert(END,*['Yellow' , 'White'])
lbx.insert(END , 'Skyblue')
lbx.grid(row=0 , column=0)

scroll = Scrollbar(frame , command=lbx.yview)
scroll.grid(row=0 , column=1 , sticky=N+S)

lbx.config(yscrollcommand=scroll.set)

frame.pack(anchor=W , padx=20 , pady=10)


bt = Button(text="Show Selected" , bg="lightgray" , command=lambda:bt_click())
bt.pack(anchor=W , padx=20 , pady=20)

def bt_click():
    seleted_items = []
    indices = lbx.curselection() # retrun Tuple
    for i in indices :
        seleted_items.append(lbx.get(i))
    print(seleted_items)

    msg = '.'.join(seleted_items)
    messagebox.showinfo(message=msg)

window.mainloop()