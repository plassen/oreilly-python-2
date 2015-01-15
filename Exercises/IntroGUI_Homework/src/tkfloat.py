from tkinter import *

class Application(Frame):
    """Application mainwindow class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
        self.value1_input = Entry(top_frame)
        self.value2_input = Entry(top_frame)
        self.label1 = Label(top_frame, text="+")
        
        self.value1_input.pack(side=LEFT)
        self.label1.pack(side=LEFT)
        self.value2_input.pack(side=LEFT)
        top_frame.pack(side=TOP)
        
        middle_frame = Frame(self)
        self.label2 = Label(middle_frame, text="Output")
        self.label2.pack()
        middle_frame.pack(side=TOP)
        
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit)
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(bottom_frame, text="Sum", command=self.handle)
        self.handleb.pack(side=LEFT)
        
    def handle(self):
        """Handle a click of the button by processing any values the
        user has placed in the entry widgets."""  
        output = ""
        try:
            value1 = float(self.value1_input.get()) 
        except ValueError:
            output = "***ERROR***"       
        try:
            value2 = float(self.value2_input.get())
        except ValueError:
            output = "***ERROR***"        
        if output == "":
            output = value1 + value2      
        self.label2.config(text=output)

root = Tk()
app = Application(master=root)
app.mainloop()