from tkinter import *
from tkinter.scrolledtext import ScrolledText


window = Tk()
window.geometry('350x220')

fm1 = Frame(window)
fm1.pack(side=TOP , fill=BOTH , expand=YES)

text = ScrolledText(fm1, height=10 , bg="powderblue" , font="tahoma 10")
text.insert(1.0 ,'one\ntwo\nthree')
text.pack(side=LEFT , fill=BOTH , expand=YES)

fm2 = Frame(window)
fm2.pack(side=TOP, fill=BOTH , expand=YES)

btnRead = Button(fm2 , text="Read" , command=lambda:btRead_click())
btnRead.pack(side=LEFT , padx=10 ,pady=3)

btnClear = Button(fm2 , text="Clear" , command=lambda:btClear_click())
btnClear.pack(side=RIGHT , padx=10 , pady=3)

def btRead_click():
    print(text.get(1.0 , END))
def btClear_click():
    text.delete(1.0 , END)



window.mainloop()
