from tkinter import *
from tkinter.ttk import Treeview , Style , Scrollbar
from tkinter.font import Font

import sqlite3

window = Tk()
window.option_add('*font' , 'tahoma 11')


# --- Start : Search Widget --- #
fram_search = LabelFrame(window , text="Search")
fram_search.pack(padx=10 , pady=10 , fill=X)

lable_keyword = Label(fram_search , text="Search Employee")
lable_keyword.pack(side=LEFT , padx=10 , pady=10)

ent_keyword = Entry(fram_search)
ent_keyword.pack(side=LEFT , padx=10 , pady=10)

btn_keyword = Button(fram_search , text='Search' ,bg='lightgray' , command=lambda:search())
btn_keyword.pack(side=LEFT , padx=10 , pady=10)
# --- End : Search Widget --- #

# --- Start : Treeview Widget --- #
fram_tv = Frame(window)
fram_tv.pack(padx=10 , pady=10)

tv = Treeview(fram_tv , columns=(1,2,3) , show='headings' , height=5)
tv.pack(side=LEFT)

scroll = Scrollbar(fram_tv , command=tv.yview)
scroll.pack(side=LEFT , fill=Y)
tv.configure(yscrollcommand=scroll.set)

tv.heading(1 , text="Name")
tv.heading(2 , text="Position")
tv.heading(3 , text="Phone")

tv.tag_configure('odd' , background='#def')
tv.tag_configure('even' , background='#e1e1e1')

st = Style()
st.map('Treeview')
st.theme_use('default')
font_head = Font(family='tahoma' , size='11' , weight='bold')
st.configure('Treeview.Heading' , font=font_head)
font_row = Font(family='tahoma' , size='11')
st.configure('Treeview' , font=font_row)
st.configure('Treeview', rowheight=30)
# --- End : Treeview Widget --- #

# --- Start : Connect to databse --- #
conn = sqlite3.connect('database.db')
cur = conn.cursor()

def search():
    tv.delete(*tv.get_children())

    sql = 'SELECT name , position , phone FROM employee'
    kw = ent_keyword.get()
    dataset = None

    if kw != "" :
        sql += " WHERE name LIKE '%'||?||'%'"
        dataset = cur.execute(sql, [f'%{kw}%'])
    else :
        # sql = "SELECT name, position, phone FROM employee"
        dataset = cur.execute(sql)
    
    for i , row in enumerate(dataset):
        tg = 'even' if i % 2 == 0 else 'odd'
        tv.insert(parent='' , index=i , values=row , tags=tg)

btn_keyword.invoke()
# --- End : Connect to databse --- #


window.mainloop()