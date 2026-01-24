from tkinter import *
window = Tk()
window.title('Tk Interface')
window.geometry('500x500')
window.config(bg="lightgray")
window.option_add("*background" , "yellow")
window.option_add("*foreground" , "green")
window.option_add("*font" , 'tahoma 20 bold')
window.option_add("*Button.font" , "times 30 bold")

fm1 = Frame(window , bg='red')
fm2 = Frame(window , bg='blue')

fm1.pack(side=LEFT)
fm2.pack(side=LEFT , padx=20)

def func_sayHi():
    tx = btn1.cget('text')
    print("Thank Your" , tx)
    btn1.bell()

btn1 = Button(fm1 , text="One" , bg="brown" , fg="white" , font="tahoma 18 bold" , command=func_sayHi).pack(side=TOP)
Button(fm1 , text="TWO" , bg="orange" , fg="white" , font="times 14 bold").pack(side=TOP)
Button(fm1 , text="Three").pack(side=TOP)

Button(fm2 , text="Four").grid(row=0 , column=0 )
Button(fm2 , text="Five").grid(row=0 , column=1 )
Button(fm2 , text="Six").grid(row=1 , column=0 )
Button(fm2 , text="Seven").grid(row=1 , column=1 )

window.mainloop()
