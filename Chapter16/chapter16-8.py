from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('500x500')
window.title('Radio Button')
window.resizable(0,0)
window.config(bg="lightgray")
window.option_add('*font' , 'tahoma 10')


menu_bt =Menubutton(text="Font Size" , relief=RAISED)
menu_bt.pack(side=TOP , pady=20)

menu = Menu(menu_bt , tearoff=False)
menu_bt.config(menu=menu)

menu.add_command(label="Small" , command=lambda:menu_click('Small'))
menu.add_command(label="Medium" , command=lambda:menu_click('Medium'))
menu.add_command(label="Large" , command=lambda:menu_click('Large'))

def menu_click(menu):
    messagebox.showinfo(message=menu)


window.mainloop()