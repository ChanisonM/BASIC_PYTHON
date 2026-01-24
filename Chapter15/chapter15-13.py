from tkinter import *

window = Tk()
window.title('XO')
window.geometry('200x200')
window.resizable(0,0)
window.config(bg="lightgray")
window.option_add("*Button.font" , "times 16 bold")
player = 0

def button_cilck(button):
    text = button.cget('text')
    print(f'You Click {text}')

def calculate(op):
    text = f'10 {op} 5 = ' + str(eval(f'10 {op} 5'))
    print(text) 
    

btOK = Button(text="OK" , command=lambda:button_cilck(btOK))
btOK.grid(row=0 , column=0)

btCancel = Button(text="Cancel" , command=lambda:button_cilck(btCancel))
btCancel.grid(row=1 , column=0)

bt_add = Button(text="Add" , command=lambda: calculate("+"))
bt_add.grid(row=2 , column=0)

bt_subtract = Button(text="Subtract" , command=lambda : calculate('-'))
bt_subtract.grid(row=3 , column=0)
window.mainloop()
