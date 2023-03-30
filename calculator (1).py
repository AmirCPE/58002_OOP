from tkinter import *
class MyWindow:
    def __init__(self, win):

#widgets start from here
        self.lbl1 = Label(win, text = "1st No.")       #for label widget
        self.lbl1.place(x=100, y=50)
        self.lbl2 = Label(win, text = "2nd No.")
        self.lbl2.place(x=100, y=100)
        self.lbl3 = Label(win, text = "Result")
        self.lbl3.place(x=100, y=150)
        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=200, y=50)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=200, y=100)
        self.txt3 = Entry(win, bd=3)
        self.txt3.place(x=200, y=150)
        self.btnadd = Button(win, text = "Add")
        self.btnadd.place(x=100, y=300)
        self.btnadd.bind('<Button-1>', self.add)
        self.btnsub = Button(win, text="Subtract", command = self.sub)
        self.btnsub.place(x=150, y=300)
        self.btnmul = Button(win, text="Multiply", command = self.mul)
        self.btnmul.place(x=225, y=300)
        self.btndvd = Button(win, text="Divide", command = self.dvd)
        self.btndvd.place(x=300, y=300)
        self.btndvd = Button(win, text="C", command = self.clear)
        self.btndvd.place(x=100, y=350)





#add event-handling / bind () method

    def add(self):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END, str(result))


#sub event-handler using command parameter

    def sub(self):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

#sub event-handler using command parameter

    def mul(self):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1*num2
        self.txt3.insert(END, str(result))

#sub event-handler using command parameter

    def dvd(self):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 / num2
        self.txt3.insert(END, str(result))

#sub event-handler using command parameter

    def clear(self):
        self.txt1.delete(0, END)
        self.txt2.delete(0, END)
        self.txt3.delete(0, END)



























window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()
