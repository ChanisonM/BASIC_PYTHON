from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('400x250')
window.title('Radio Button')
window.resizable(0,0)
window.config(bg="lightgray")
window.option_add('*font' , 'tahoma 10')


strvar = StringVar(value=' ')
radio1 = Radiobutton(text="Red" , variable=strvar , value="Red" , command=lambda:radio_select())
radio1.pack(side=LEFT , anchor=NW , padx=5 , pady=10)


radio2 = Radiobutton(text="Green" , variable=strvar , value="Green" , command=lambda:radio_select())
radio2.pack(side=LEFT , anchor=NW , padx=5 , pady=10)

radio3 = Radiobutton(text="Blue" , variable=strvar , value="Blue" , command=lambda:radio_select())
radio3.pack(side=LEFT , anchor=NW , padx=5 , pady=10)

radio4 = Radiobutton(text="Orange" , variable=strvar , value="Orange" , command=lambda:radio_select())
radio4.pack(side=LEFT , anchor=NW , padx=5 , pady=10)



def radio_select():
    value = strvar.get()
    # if value == "Red" : 
    #     window.config(bg=value)
    # elif value == 'Green':
    #     window.config(bg=value)
    # elif value == 'Blue':
    #     window.config(bg=value)
    # elif value == 'Orange':
    #     window.config(bg=value)


    messagebox.showinfo(message=value)
window.mainloop()