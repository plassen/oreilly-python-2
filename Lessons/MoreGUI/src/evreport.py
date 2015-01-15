from tkinter import *

root = Tk()

def handler(event):
    print("Keystroke '{0}' ({1}) {2} ".format(event.char, len(event.char), event.keycode))
    
frame = Frame(root, width=100, height=100)
frame.bind("<Key>", handler)
frame.pack()
frame.focus()

root.mainloop()

