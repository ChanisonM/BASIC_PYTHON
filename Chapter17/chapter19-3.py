from tkinter import *
from tkinter.ttk import Treeview

window = Tk()
tv = Treeview(window , columns=(1 ,2 ,3) , show='headings' , height=5)
tv.pack(padx=5 , pady=5)

tv.heading(1 , text='Product')
tv.heading(2 , text='Price')
tv.heading(3 , text='Color')

# tv.column(1 , width=150)
# tv.column(2 , width=100  , anchor=E)
# tv.column(3 , width=80 , anchor=CENTER)


tv.insert(parent="" , index=0 , values=('Item1' , 350 , 'green'))
tv.insert(parent="" , index=0 , values=('Item2' , 350 , 'red'))
tv.insert(parent="" , index=0 , values=('Item3' , 350 , 'blue'))

window.mainloop()