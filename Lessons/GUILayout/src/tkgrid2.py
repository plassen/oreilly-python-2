from tkinter import *

def colorgen():
    while True:
        yield "red"
        yield "blue"
        
class Application(Frame):
    
    def __init__(self, master=None):
        colors = colorgen()
        Frame.__init__(self, master)
        self.grid()
        for r in (1, 22, 333):
            for c in (1, 22, 333):
                txt = "Item {0}, {1}".format(r, c)
                l = Label(self, text=txt, bg=next(colors))
                l.grid(row=r, column=c, sticky=E+W)
                
root = Tk()
app = Application(master=root)
app.mainloop()
                