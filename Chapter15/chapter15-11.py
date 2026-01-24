from tkinter import *
window = Tk()
window.title('Tk Interface')
window.geometry('400x400')
window.config(bg="lightgray")

Button(text="One").grid(row=0 , column=0 , padx=5 , pady=5)
Button(text="Two").grid(row=0 , column=1 , padx=5 , pady=5 , sticky=W)
Button(text="There").grid(row=0 , column=2 , padx=5 , pady=5 , ipadx=50)
Button(text="Four").grid(row=1 , column=0 , padx=5 , pady=5 , sticky=N)
Button(text="Five").grid(row=1 , column=1 , columnspan=1,padx=5 , pady=5 , ipadx=40 , ipady=40)
Button(text="Six").grid(row=1 , column=2 , padx=5 , pady=5 , sticky=NW)
window.mainloop()