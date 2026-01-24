from tkinter import *
window = Tk()
window.title('Tk Interface')
window.geometry('200x160')
window.config(bg="lightgray")

Label(text="User").grid(row=0 ,column=0 , padx=5)
Entry().grid(row=0 , column=1 , columnspan=2 , pady=5)

Label(text="Pasword").grid(row=1 , column=0 , padx=5)
Entry().grid(row=1 , column=1 , columnspan=2 , pady=5)

Button(text="Ok").grid(row=2 , column=1 , pady=5)
Button(text="Cancel").grid(row=2 , column=2, pady=5)
window.mainloop()