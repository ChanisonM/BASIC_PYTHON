from tkinter import *
from tkinter.ttk import Treeview , Style , Scrollbar
from tkinter.font import Font

import sqlite3

# Connect database 
conn = sqlite3.connect('database.db')
cur = conn.cursor()
sql = 'SELECT name , position , salary , phone FROM employee'
daataset = cur.execute(sql)

window = Tk()
frame = Frame(window)
frame.pack(padx=10 , pady=10)

tv = Treeview(frame , columns=(1,2,3,4) ,show='headings' , height=5)
tv.pack(side=LEFT)
scroll = Scrollbar(frame , command=tv.yview)
scroll.pack(side=LEFT , fill=Y)
tv.config(yscrollcommand=scroll.set)

tv.heading(1 , text="Name")
tv.heading(2 , text="Position")
tv.heading(3 , text="Price")
tv.heading(4 , text="Phone")

# tv.column(1 , width=100)

tv.tag_configure('odd' , background="#def")
tv.tag_configure('even' , background="#e1e1e1")

for i , row in enumerate(daataset):
    row = list(row)
    row[2] = f'{row[2]:,.0f}'

    tg = 'even' if i % 2 == 0 else 'odd'
    tv.insert(parent='' , index=1 , values=row , tags=tg)

    st = Style()
    st.map('Treeview')
    st.theme_use('default')
    font_head = Font(family='tahoma' , size='11' , weight='bold')
    st.configure('Treeview.Heading' , font=font_head)
    font_row = Font(family='tahoma' , size='11')
    st.configure('Treeview' , font=font_row)
    st.configure('Treeview' , rowheight=30)

cur.close()
window.mainloop()



