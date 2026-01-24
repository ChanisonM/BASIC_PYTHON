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

# btn1.pack(anchor='center' , expand=YES)
# btn2.pack(anchor='sw' , expand=YES)
# btn3.pack(anchor='n' , expand=YES)
btn4.pack(side=BOTTOM , fill=X)
btn5.pack(side=RIGHT , fill=Y)


window.mainloop()