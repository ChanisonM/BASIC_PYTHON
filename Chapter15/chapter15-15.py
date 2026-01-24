from tkinter import *
from datetime import datetime

window = Tk()
window.title('Date Time')
window.geometry('400x400')
window.resizable(0,0)
window.config(bg="lightgray")

lb_text = Label(font="times 16")
lb_text.grid(row=0 , column=0)

lb_clock = Label(font="times 16")
lb_clock.grid(row=1,column=1)

def tick():
    curtime = datetime.now().time()
    ftime = curtime.strftime('%H:%M:%S')
    lb_clock.config(text=ftime)
    lb_clock.after(1000 , tick)

def showDate():
    curdate = datetime.now()
    day = curdate.day
    month = curdate.month
    year = curdate.year + 543
    data_format = f'{day}/{month}/{year}'
    lb_text.config(text=data_format)

tick()
showDate()

window.mainloop()
