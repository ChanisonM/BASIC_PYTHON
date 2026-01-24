from tkinter import *
from datetime import datetime

window = Tk()
window.title('Calculation')
window.geometry('450x90')
window.resizable(0,0)
window.config(pady=10)
window.option_add('*font','tahama 10')
window.option_add('*Entry.width' , '10')
window.option_add('*Button.width' , '3')
window.option_add('Button.background' , 'lightgray')


fm1 = Frame(window)
fm1.pack(side=TOP)
fm2 = Frame(window)
fm2.pack(side=BOTTOM)

Label(fm1 , text="จำนวนที่ 1 : ").pack(side=LEFT)
ent1 = Entry(fm1)
ent1.pack(side=LEFT)

Label(fm1 , text="จำนวนที่ 2 : ").pack(side=LEFT)
ent2 = Entry(fm1)
ent2.pack(side=LEFT)

Label(fm1 , text="ผลลัพธ์ : ").pack(side=LEFT)
ent3 = Entry(fm1 , background="lightgray")
ent3.bind('<Key>' , 'break')
ent3.pack(side=LEFT)



def add_button(button , op):
    button.config(text=op , command=lambda:calc(op))
    button.pack(side=LEFT , padx=3)

ops = ['+' , "-" , "*" ,"/" , '%' , '//' , '**']

for o in ops :
    add_button(Button(fm2) , op=o)

def calc(op):
    try :
        n1 = float(ent1.get())
        n2 = float(ent2.get())
        r = eval(f'{n1} {op} {n2}')
        if r % 1 == 0 :
            r = int(r)
    except :
        r = ''

    finally :
        ent3.delete(first=0 , last=END)
        ent3.insert(0 , r)
window.mainloop()
