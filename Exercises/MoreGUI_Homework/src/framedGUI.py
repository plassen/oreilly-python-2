from tkinter import *

ALL = N+S+W+E

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master, bg="white")
        self.grid(sticky=ALL)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        
        f1 = Frame(self, bg="red")
        f1.bind("<Button-1>", lambda event, frame="Frame 1" : self.click_handler(event, frame))
        self.label1 = Label(f1, text="Frame 1", bg="red")
        self.label1.pack()
        
        f2 = Frame(self, bg="blue")
        f2.bind("<Button-1>", lambda event, frame="Frame 2" : self.click_handler(event, frame))
        self.label2 =Label(f2, text="Frame 2", bg="blue")
        self.label2.pack()
        
        f3 = Frame(self, bg="green")
        self.f3_text = Text(f3, height=2, width=5) 
        self.f3_text.insert(END, "Frame3")
        self.f3_text.pack(fill=BOTH, expand=1)
        self.f3_entry = Entry(f3, width=5)
        self.f3_entry.pack(fill=X)
        
        f1.grid(row=0, column=0, columnspan=2, sticky=ALL)
        f2.grid(row=1, column=0, columnspan=2, sticky=ALL)
        f3.grid(row=0, column=2, rowspan=2, columnspan=3, sticky=ALL)
        self.rowconfigure(0, weight=20)
        self.rowconfigure(1, weight=20)
        self.rowconfigure(2, weight=0)
        
        b1 = Button(self, text="Red")
        b1.grid(row=3, column=0, sticky=ALL)
        b1.bind("<Button-1>", self.callback_color)
        self.columnconfigure(0, weight=1)
        b2 = Button(self, text="Blue")
        b2.grid(row=3, column=1, sticky=ALL)
        b2.bind("<Button-1>", self.callback_color)
        self.columnconfigure(1, weight=1)
        b3 = Button(self, text="Green")
        b3.grid(row=3, column=2, sticky=ALL)
        b3.bind("<Button-1>", self.callback_color)
        self.columnconfigure(2, weight=1)
        b4 = Button(self, text="Black")
        b4.grid(row=3, column=3, sticky=ALL)
        b4.bind("<Button-1>", self.callback_color)
        self.columnconfigure(3, weight=1)
        b5 = Button(self, text="Open")
        b5.grid(row=3, column=4, sticky=ALL)
        b5.bind("<Button-1>", self.callback_open)
        self.columnconfigure(4, weight=1)  
        
    def callback_color(self, event):
        self.f3_text.configure(fg=event.widget.cget("text"))
        
    def callback_open(self, event):   
        try:
            filename = self.f3_entry.get()
            f = open(filename, 'r')
            content = f.read()
            f.close()
            self.f3_text.insert(END, content)
        except:
            pass
        
    def click_handler(self, event, frame):
        print(frame, " clicked at", event.x, event.y)  
        
root = Tk()

app = Application(master=root)
app.mainloop()