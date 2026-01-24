from tkinter import *
window = Tk()
window.title('Tk Interface')
window.geometry('200x160')
window.config(bg="lightgray")

btn1 = Button(text="One")
btn2 = Button(text="Two")
btn3 = Button(text="Three")


btn1.place(x=10 , y=20 , width=40 , height=60)
btn2.place(x=10 , y=60 , width=40 , height=60)
btn3.place(x=10 , y=120 , width=40 , height=60)
window.mainloop()