from tkinter import *


window = Tk()
window.geometry('500x500')
window.title('Radio Button')
window.resizable(0,0)
window.config(bg="lightgray")
window.option_add('*font' , 'tahoma 10')


img = PhotoImage(file='')
cv = Canvas(width=1 , height=1)
cv.pack(side=TOP)

bt_left = Button(text="bootstrap Logo" , command=lambda:draw_image(r'images\bootstrap.png'))
bt_left.pack(side=LEFT ,anchor=SW , expand=YES)
bt_left.after(1000 , bt_left.invoke)


bt_right = Button(text="Python Logo" , command=lambda:draw_image(r'images\python-logo.png'))
bt_right.pack(side=LEFT , anchor=SE , expand=YES)

def draw_image(file):
    img = PhotoImage(file=file)
    cv.config(width=img.width() , height=img.height())
    cv.create_image(5 , 5 ,anchor=NW , image=img)
    cv.image = img
    
window.mainloop()