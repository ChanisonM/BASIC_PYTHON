from tkinter import *
from tkinter.scrolledtext import ScrolledText

window = Tk()
window.geometry('400x250')
window.title('Simple dialog')
window.resizable(0,0)
window.config(bg="lightgray")
window.option_add('*font' , 'tahoma 10')
# --- Frame 1 ---
fm1 = LabelFrame(window , text="ข้อมูลส่วนต้ว")
fm1.pack(side=TOP , fill=X , padx=10 , pady=10)

Label(fm1 , text="ชื่อ - นามสกุล").grid(row=0 , column=0 , sticky=W , padx=5 , pady=5)
Entry(fm1 , width=25).grid(row=0 , column=1 , padx=5 , pady=5)

Label(fm1 , text="ที่อยู่และการติดต่อ").grid(row=1 , column=0 , sticky=NW , padx=5 , pady=5)
ScrolledText(fm1 , width=22 , height=3).grid(row=1 , column=1 , padx=5 , pady=5)

# --- Frame 2 ---
fm2 = LabelFrame(window , text="ข้อมูลการศึกษา")
fm2.pack(side=TOP , fill=X , padx=10 , pady=10)
Label(fm2 , text="การศึกษาขั้นสูงสุด").grid(row=0 , column=0 , sticky=W , padx=5 , pady=5)
Entry(fm2 , width=25).grid(row=0 , column=1 , padx=5 , pady=5)

Label(fm2 , text="ชื่อสถาบัน").grid(row=1 , column=0 , sticky=W , padx=5 , pady=5)
Entry(fm2 , width=25).grid(row=1 , column=1 , padx=5 , pady=5)









window.mainloop()