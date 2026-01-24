from tkinter import *

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Calculation (OOP Version)')
        self.master.geometry('450x120')
        self.master.resizable(0,0)
        
        # ตั้งค่า Option พื้นฐาน
        self.master.option_add('*font','tahama 10')
        self.master.option_add('*Entry.width', '10')
        self.master.option_add('*Button.width', '3')

        self.create_widgets()

    def create_widgets(self):
        # ส่วนแสดงผลและรับข้อมูล (Frame บน)
        self.fm1 = Frame(self.master, pady=10)
        self.fm1.pack(side=TOP)

        Label(self.fm1, text="จำนวนที่ 1 : ").pack(side=LEFT)
        self.ent1 = Entry(self.fm1)
        self.ent1.pack(side=LEFT)

        Label(self.fm1, text="จำนวนที่ 2 : ").pack(side=LEFT)
        self.ent2 = Entry(self.fm1)
        self.ent2.pack(side=LEFT)

        Label(self.fm1, text="ผลลัพธ์ : ").pack(side=LEFT)
        self.ent3 = Entry(self.fm1, background="lightgray")
        self.ent3.bind('<Key>', lambda e: "break") # กันการพิมพ์
        self.ent3.pack(side=LEFT)

        # ส่วนปุ่มกด (Frame ล่าง)
        self.fm2 = Frame(self.master)
        self.fm2.pack(side=TOP)

        ops = ['+', "-", "*", "/", '%', '//', '**']
        for o in ops:
            btn = Button(self.fm2, text=o, command=lambda op=o: self.calc(op))
            btn.pack(side=LEFT, padx=3)

    def calc(self, op):
        try:
            n1 = float(self.ent1.get())
            n2 = float(self.ent2.get())
            r = eval(f'{n1} {op} {n2}')
            
            # ตกแต่งตัวเลข
            if r % 1 == 0:
                r = int(r)
            elif isinstance(r, float):
                r = round(r, 4) # ปัดเศษทศนิยมให้สวยงาม
        except ZeroDivisionError:
            r = "Error: Div 0"
        except:
            r = "Error"

        # แสดงผลลัพธ์
        self.ent3.delete(0, END)
        self.ent3.insert(0, r)

# ส่วนการรันโปรแกรม
if __name__ == "__main__":
    root = Tk()
    app = CalculatorApp(root)
    root.mainloop()