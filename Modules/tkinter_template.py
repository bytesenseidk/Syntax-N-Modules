from tkinter import *

class Tkinter_Template(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        hello = Label(master, 
                text="Follow python_genius on Instagram!",
                font=("Helvetica", 16))
        hello.grid()
        
if __name__ == '__main__':
    root = Tk()
    root.title("Tkinter Starter Template")
    root.geometry("350x50")
    Tkinter_Template(root)
    root.mainloop()

