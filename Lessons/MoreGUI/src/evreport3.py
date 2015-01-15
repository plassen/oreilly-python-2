from tkinter import *

root = Tk()

def handler(event):
    print("Keystroke '{0}' ({1}) {2} ".format(event.char, len(event.char), event.keycode))
    
def handler2(event):
    print("RootKeystroke '{0}' ({1}) {2} ".format(event.char, len(event.char), event.keycode))
    
frame = Frame(root, width=100, height=100)
frame.bind("o", handler)
frame.bind("k", handler)
root.bind("<Key>", handler2)
frame.pack()
frame.focus()

root.mainloop()

