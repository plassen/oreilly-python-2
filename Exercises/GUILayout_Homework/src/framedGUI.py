from tkinter import *

ALL = N+S+W+E

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master, bg="white")
        self.grid(sticky=ALL)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        
        f1 = Frame(self, bg="red")
        self.label1 = Label(f1, text="Frame 1", bg="red")
        self.label1.pack()
        
        f2 = Frame(self, bg="blue")
        self.label2 = Label(f2, text="Frame 2", bg="blue")
        self.label2.pack()
        
        f3 = Frame(self, bg="green")
        self.label3 = Label(f3, text="Frame 3", bg="green")
        self.label3.pack()
        
        f1.grid(row=0, column=0, columnspan=2, sticky=ALL)
        f2.grid(row=1, column=0, columnspan=2, sticky=ALL)
        f3.grid(row=0, column=2, rowspan=2, columnspan=3, sticky=ALL)
        self.rowconfigure(0, weight=20)
        self.rowconfigure(1, weight=20)
        self.rowconfigure(2, weight=0)
        
        for b in range(5):
            Button(self, text="Button {0}".format(b)).grid(row=3, column=b, sticky=ALL)
            self.columnconfigure(b, weight=1)
        
root = Tk()
app = Application(master=root)
app.mainloop()