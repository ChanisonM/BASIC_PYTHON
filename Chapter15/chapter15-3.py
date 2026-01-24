from tkinter import *
window = Tk()
window.title('Tk Interface')
window.geometry('200x160')
window.config(bg="lightgray")

btn1 = Button(text="One")
btn2 = Button(text="Two")
btn3 = Button(text="Three")
btn4 = Button(text="Four")
btn5 = Button(text="Five")
btn6 = Button(text="Six")


btn1.pack(side=LEFT , padx=5)
btn2.pack(side=LEFT , padx=5)
btn3.pack(side=LEFT , padx=15)
btn4.pack(side=BOTTOM , pady= 5)
btn5.pack(side=BOTTOM , pady= 5)
btn6.pack(side=BOTTOM , pady= 15)


window.mainloop()